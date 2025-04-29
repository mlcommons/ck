import os
import re
import textwrap
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import load_dataset
from tqdm import tqdm

from utils import get_logger

log = get_logger(__name__)


class Dataset:
    """Dataset handler for MLPerf inference tasks."""

    PROMPT_TEMPLATES = {
        "llama2": textwrap.dedent(
            """
            <s>[INST] <<SYS>>
            {system_prompt}
            <</SYS>>

            {user_message} [/INST]
            """
        ),
        "llama3": textwrap.dedent(
            """
            <|begin_of_text|><|start_header_id|>system<|end_header_id|>

            {system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

            {user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
            """
        ),
        "deepseek": textwrap.dedent(
            """
            {system_prompt}

            {user_message}
            """
        ),
    }

    DATASET_CONFIGS = {
        "AI-MO/NuminaMath-TIR": {
            "input_column": "problem",
            "output_column": "solution",
            "max_length": None,
        },
        "Open-Orca/OpenOrca": {
            "input_column": "question",
            "output_column": "response",
            "system_prompt_column": "system_prompt",
            "max_length": 1024,
        },
        "ctuning/MLPerf-OpenOrca": {
            "input_column": "question",
            "output_column": "response",
            "system_prompt_column": "system_prompt",
            "max_length": 1024,
        },
        "pickle": {
            "input_column": "question",
            "output_column": "response",
            "system_prompt_column": "system_prompt",
            "max_length": 1024,
        },
    }

    def __init__(
        self,
        model_name: str,
        dataset_path: str,
        dataset_split: str = "train",
        total_sample_count: int | None = None,
    ) -> None:
        """Initialize dataset with model and data configurations."""
        log.info(f"Initializing dataset from {dataset_path}")
        self.model_type = self._get_model_type(model_name)
        log.info(f"Model type: {self.model_type}. This is required to format prompts.")
        self.total_sample_count = total_sample_count

        if dataset_path.endswith(".pkl.gz") or dataset_path.endswith(".pkl"):
            self.config = self.DATASET_CONFIGS["pickle"]
            self.prompts = self._load_from_pickle(dataset_path)
        else:
            self.config = self.DATASET_CONFIGS[dataset_path]
            self.prompts = self._load_from_huggingface(dataset_path, dataset_split)

        log.info(
            f"Dataset initialized with {len(self.prompts)} samples. Downsampling happens in the SUT."
        )

    def _get_model_type(self, model_name: str) -> str:
        """Determine model type from model name or path."""
        if os.path.exists(model_name):
            config_path = Path(model_name) / "config.json"
            if config_path.exists():
                with open(config_path) as f:
                    import json

                    config = json.load(f)
                    model_name = config.get("_name_or_path", model_name)

        model_name = re.sub(r"\W+", "", model_name.lower())
        if "deepseek" in model_name:
            return "deepseek"
        if "llama2" in model_name:
            return "llama2"
        if "llama3" in model_name:
            return "llama3"
        log.warning(f"Model type not recognized for {model_name}")
        return "unknown"

    def _format_prompt(self, sample: dict) -> str:
        """Format a prompt using the appropriate template and sample data."""
        config = self.config
        if "system_prompt_column" in config and sample.get(
            config["system_prompt_column"]
        ):
            return (
                self.PROMPT_TEMPLATES.get(self.model_type, "{}\n\n{}")
                .format(
                    system_prompt=sample[config["system_prompt_column"]],
                    user_message=sample[config["input_column"]],
                )
                .strip()
            )
        return sample[config["input_column"]]

    def _load_from_pickle(self, filepath: str) -> list[str]:
        """Load preprocessed dataset from pickle file."""
        if not Path(filepath).is_file():
            raise FileNotFoundError(f"Processed pickle file {filepath} not found.")

        log.info("Loading dataset from pickle file...")
        data = pd.read_pickle(filepath)

        return [
            self._format_prompt(row)
            for _, row in tqdm(data.iterrows(), desc="Formatting prompts")
        ]

    def _load_from_huggingface(self, dataset_path: str, split: str) -> list[str]:
        """Load and format data from HuggingFace dataset."""
        dataset = load_dataset(dataset_path, split=split)
        return [
            self._format_prompt(sample)
            for sample in tqdm(dataset, desc="Formatting prompts")
        ]

    def LoadSamplesToRam(self, sample_list):
        """MLPerf LoadGen callback - not used but required."""
        pass

    def UnloadSamplesFromRam(self, sample_list):
        """MLPerf LoadGen callback - not used but required."""
        pass

    def postProcess(
        self,
        out_tokens,
        input_seq_lens=None,
        query_id_list=None,
        sample_index_list=None,
    ):
        """Post-process output predictions."""
        return np.array(
            out_tokens, dtype=str if isinstance(out_tokens[0], str) else np.int32
        )
