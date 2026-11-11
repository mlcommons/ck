import threading
from abc import ABC, abstractmethod
from pathlib import Path

import requests
from transformers import AutoTokenizer

from flexbench.config import BenchmarkConfig
from flexbench.dataset.text import TextDataset
from flexbench.utils import get_logger

log = get_logger(__name__)


class BaseRunner(ABC):
    """Base class for benchmark runners."""

    def __init__(self, config: BenchmarkConfig):
        self.config = config

        self.results_dir = Path(config.output_dir) if config.output_dir else Path("results")
        self.results_dir.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    async def run(self) -> dict:
        """Run benchmark and return results."""
        pass


class BaseBackend(ABC):
    """Base class for benchmark backends (text-only)."""

    def __init__(self, config: BenchmarkConfig):
        self.config = config
        # Only support text datasets now
        self.dataset = TextDataset(
            dataset_config=config.dataset_config,
            model_path=config.model_path,
            max_generated_tokens=config.max_generated_tokens,
            max_input_tokens=config.max_input_tokens,
            fixed_input_length=config.fixed_input_length,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            config.tokenizer_path_override or config.model_path,
            use_fast=True,
            padding_side="right",
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self._active = False
        self.total_sample_count = config.total_sample_count or len(self.dataset)
        self.sample_counter = 0
        self.sample_counter_lock = threading.Lock()

    @abstractmethod
    def start(self):
        """Start the backend."""
        self._active = True

    @abstractmethod
    def stop(self):
        """Stop the backend."""
        self._active = False

    @abstractmethod
    def process_query(self, query: dict) -> dict:
        """Process a single query."""
        pass

    def _update_counter(self) -> None:
        """Update and log sample counter in a thread-safe way."""
        with self.sample_counter_lock:
            self.sample_counter += 1
            self.log_progress(self.sample_counter)

    def log_progress(self, count: int):
        """Log processing progress."""
        percent = count / self.total_sample_count * 100
        if count == 1 or count % max(1, self.total_sample_count // 10) == 0:
            log.info(f"Progress: {count}/{self.total_sample_count} ({percent:.1f}%)")

    def _make_api_request(
        self, inputs: str | dict | list, stream: bool = False
    ) -> dict | requests.Response:
        """Make API request to vLLM server with proper headers and error handling."""

        with requests.Session() as s:
            resp = s.post(
                url=f"{self.config.api_server}/v1/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": (
                        f"Bearer {self.config.api_token}" if self.config.api_token else None
                    ),
                },
                json={
                    "model": self.config.remote_model_path,
                    "prompt": inputs,
                    "max_tokens": self.config.max_generated_tokens,
                    "temperature": 0,
                    "stream": stream,
                    "min_tokens": 1,
                },
                stream=stream,
            )
            resp.raise_for_status()
            return resp if stream else resp.json()

    def _process_response(self, response: dict | str, streaming: bool = False) -> str:
        """Process API response and extract text content."""
        if isinstance(response, str):
            return response

        if streaming:
            return response["choices"][0]["text"]
        return "".join(choice["text"] for choice in response["choices"])
