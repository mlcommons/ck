import array
import json
import os
import queue
import threading
from abc import ABC, abstractmethod
from math import log10

import mlperf_loadgen as lg
import numpy as np
import requests
from transformers import AutoTokenizer

from dataset import Dataset
from utils import get_logger

log = get_logger(__name__)


class SUT(ABC):
    def __init__(
        self,
        model_path: str,
        dataset_path: str,
        dataset_split: str,
        api_server: str,
        total_sample_count: int | None,
    ):
        log.info(f"Initializing SUT with:\n{locals()}")
        self.model_path = (
            os.path.abspath(model_path) if os.path.exists(model_path) else model_path
        )
        self.api_server = api_server

        self.dataset_path = dataset_path
        self.dataset = Dataset(
            self.model_path,
            total_sample_count=total_sample_count,
            dataset_path=self.dataset_path,
            dataset_split=dataset_split,
        )
        self.total_sample_count = total_sample_count or len(self.dataset.prompts)

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path,
            use_fast=True,
            add_prefix_space=None if self.dataset.model_type == "deepseek" else False,
            padding_size="left",
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.max_tokens = min(
            self.tokenizer.model_max_length,
            self.dataset.config["max_length"] or float("inf"),
        )

        self.sample_counter = 0
        self.sample_counter_lock = threading.Lock()

    @abstractmethod
    def start(self) -> None:
        """Start the SUT processing."""
        ...

    @abstractmethod
    def stop(self) -> None:
        """Stop the SUT and clean up resources."""
        ...

    @abstractmethod
    def issue_queries(self, query_samples: list[lg.QuerySample]) -> None:
        """Issue queries to the SUT."""
        ...

    def submit_lg_response(
        self, token_ids: list[int], query_id: int, first_token: bool = False
    ) -> None:
        """Submit token response to MLPerf loadgen."""
        tokens_arr = np.array(token_ids, dtype=np.int32)
        resp_arr = array.array("B", tokens_arr.tobytes())
        bi = resp_arr.buffer_info()
        response = lg.QuerySampleResponse(query_id, bi[0], bi[1], len(tokens_arr))
        if first_token:
            lg.FirstTokenComplete([response])
        else:
            lg.QuerySamplesComplete([response])

    def log_progress(self, sample_counter: int) -> None:
        """Log current progress of sample processing."""
        percent = sample_counter / self.total_sample_count * 100
        log_interval = 10 ** int(log10(self.total_sample_count - 1))

        if (
            self.total_sample_count < 100
            or sample_counter == 1
            or sample_counter % log_interval == 0
            or sample_counter == self.total_sample_count
        ):
            log.info(
                f"Progress: {sample_counter}/{self.total_sample_count} samples "
                f"({percent:.1f}%)"
            )

    @property
    def sut(self):
        """Return MLPerf loadgen System Under Test object."""
        return lg.ConstructSUT(self.issue_queries, self.flush_queries)

    @property
    def qsl(self):
        """Return MLPerf loadgen Query Sample Library object."""
        return lg.ConstructQSL(
            self.total_sample_count,
            self.total_sample_count,
            self.dataset.LoadSamplesToRam,
            self.dataset.UnloadSamplesFromRam,
        )

    def flush_queries(self):
        """Flush pending queries (required by MLPerf loadgen)."""
        pass


class SUTOffline(SUT):
    def __init__(self, batch_size: int | None = None, **kwargs):
        """Initialize offline SUT with optional batch size."""
        super().__init__(**kwargs)
        self.batch_size = batch_size or self.total_sample_count
        self.worker_threads: list[threading.Thread] = []
        self.query_queue = queue.Queue()

    def start(self) -> None:
        """Start worker threads for offline batch processing."""
        log.info("Starting SUT offline mode processing threads")
        num_workers = os.cpu_count()
        for _ in range(num_workers):
            worker = threading.Thread(target=self.process_queries)
            worker.start()
            self.worker_threads.append(worker)

    def stop(self) -> None:
        """Stop all worker threads and clean up resources."""
        log.info("Stopping SUT and cleaning up resources")
        for _ in range(len(self.worker_threads)):
            self.query_queue.put(None)

        for thread in self.worker_threads:
            if thread and thread.is_alive():
                thread.join()

    def issue_queries(self, query_samples: lg.QuerySample) -> None:
        """Process query samples in batches using worker threads."""
        if not self.worker_threads:
            self.start()

        while len(query_samples) > 0:
            batch = query_samples[: self.batch_size]
            self.query_queue.put(batch)
            query_samples = query_samples[self.batch_size :]

    def process_queries(self) -> None:
        """Worker thread function to process batches from queue."""
        while True:
            batch = self.query_queue.get()
            if batch is None:
                break

            log.debug(f"Processing batch of {len(batch)} queries")
            inputs_txt = [self.dataset.prompts[q.index] for q in batch]
            outputs_txt = self.query_api_vllm(inputs_txt)

            for i, output_txt in enumerate(outputs_txt):
                query_sample, input_txt = batch[i], inputs_txt[i]
                token_ids = self.tokenizer.encode(output_txt, add_special_tokens=False)

                if not token_ids:
                    log.warning(
                        f"No output tokens generated for query {query_sample.id}."
                    )
                    log.debug(f"INPUT: {repr(input_txt)}\n\nOUTPUT: {repr(output_txt)}")

                self.submit_lg_response(token_ids, query_sample.id)

                with self.sample_counter_lock:
                    self.sample_counter += 1
                    self.log_progress(self.sample_counter)

    def query_api_vllm(self, inputs: list[str]) -> list[str]:
        """Query vLLM API with batched inputs."""
        log.debug(f"Querying vLLM API with batch of {len(inputs)} inputs")
        headers = {"Content-Type": "application/json"}
        json_data = {
            "model": self.model_path,
            "prompt": inputs,
            "min_tokens": 1,
            "max_tokens": self.max_tokens,
            "temperature": 0,
            "stream": False,
        }

        with requests.Session() as s:
            with s.post(
                f"{self.api_server}/v1/completions",
                headers=headers,
                json=json_data,
                verify=False,
            ) as resp:
                return [choice["text"] for choice in resp.json()["choices"]]


class SUTServer(SUT):
    def __init__(self, **kwargs):
        """Initialize server SUT for streaming responses."""
        super().__init__(**kwargs)
        self.first_token_queue = queue.Queue()

    def start(self) -> None:
        """Start first token processing thread."""
        log.info("Starting SUT server mode processing threads")
        self.ft_resp_thread = threading.Thread(target=self.process_first_tokens)
        self.ft_resp_thread.start()

    def stop(self) -> None:
        """Stop first token processing thread."""
        if hasattr(self, "ft_resp_thread"):
            self.first_token_queue.put(None)
            self.ft_resp_thread.join()

    def issue_queries(self, query_samples: list[lg.QuerySample]) -> None:
        """Process queries individually in separate threads."""
        if not hasattr(self, "ft_resp_thread"):
            self.start()

        for sample in query_samples:
            threading.Thread(target=self.process_query, args=(sample,)).start()

    def process_query(self, query_sample: lg.QuerySample) -> None:
        """Process a single query with streaming response."""
        input_txt = self.dataset.prompts[query_sample.index]
        output_txt = self.stream_api_vllm(input_txt, query_sample.id)
        token_ids = self.tokenizer.encode(output_txt, add_special_tokens=False)

        self.submit_lg_response(token_ids, query_sample.id)

        with self.sample_counter_lock:
            self.sample_counter += 1
            self.log_progress(self.sample_counter)

    def process_first_tokens(self) -> None:
        """Process and submit first tokens from streaming responses."""
        while True:
            item = self.first_token_queue.get()
            if item is None:
                break
            first_token_txt, query_id = item
            first_token_id = self.tokenizer.encode(
                first_token_txt,
                add_special_tokens=False,
            )
            self.submit_lg_response(first_token_id, query_id, first_token=True)

    def stream_api_vllm(self, input_txt: str, resp_id: int) -> str:
        """Stream tokens from vLLM API for a single input."""
        headers = {"Content-Type": "application/json"}
        json_data = {
            "model": self.model_path,
            "prompt": input_txt,
            "min_tokens": 1,
            "max_tokens": self.max_tokens,
            "temperature": 0,
            "stream": True,
        }

        text_cache = ""
        first_token_sent = False

        with requests.Session() as s:
            with s.post(
                f"{self.api_server}/v1/completions",
                headers=headers,
                json=json_data,
                verify=False,
                stream=True,
            ) as resp:
                for line in resp.iter_lines():
                    if not line or b"[DONE]" in line:
                        continue

                    decoded = line.decode()

                    if not decoded.startswith("data"):
                        continue

                    token_data = json.loads(decoded[6:])
                    token_txt = token_data["choices"][0]["text"]

                    if not token_txt:
                        continue

                    if not first_token_sent:
                        self.first_token_queue.put((token_txt, resp_id))
                        first_token_sent = True

                    text_cache += token_txt
        return text_cache
