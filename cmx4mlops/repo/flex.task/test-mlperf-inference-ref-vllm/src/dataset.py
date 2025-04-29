import logging

from datasets import load_dataset
from transformers import AutoTokenizer

logger = logging.getLogger("DeepSeek-R1-Dataset")


class Dataset:
    MAX_LENGTH = 1024
    SPECIAL_TOKENS = {
        "begin": "<｜begin▁of▁sentence｜>",
        "end": "<｜end▁of▁sentence｜>",
    }

    def __init__(
        self,
        model_name,
        total_sample_count,
        dataset_path,
        device="cpu",
        perf_count_override=None,
    ):
        self.model_name = model_name
        self.dataset_path = dataset_path
        self.device = device
        self.target_sample_count = total_sample_count

        self.tokenizer = self._setup_tokenizer()
        self.input_ids, self.attention_masks = self._process_dataset()

        self.total_sample_count = min(len(self.input_ids), self.target_sample_count)
        self.perf_count = perf_count_override or self.total_sample_count

    def _setup_tokenizer(self):
        tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            model_max_length=self.MAX_LENGTH,
            padding_side="right",
            use_fast=False,
            truncation_side="left",
        )
        tokenizer.pad_token = tokenizer.eos_token
        return tokenizer

    def _process_dataset(self):
        dataset = load_dataset(self.dataset_path, split="train").select(
            range(self.target_sample_count)
        )

        prompts = [
            f"{self.SPECIAL_TOKENS['begin']}You will be given a problem. Please reason step by step, "
            f"and put your final answer within \\boxed{{}}:\n{problem}{self.SPECIAL_TOKENS['end']}"
            for problem in dataset["problem"]
        ]

        encodings = self.tokenizer(
            prompts,
            padding=True,
            truncation=True,
            max_length=self.MAX_LENGTH,
            return_tensors="pt",
            add_special_tokens=False,
        )

        assert (
            encodings.input_ids.size(1) <= self.MAX_LENGTH
        ), f"Input sequence length exceeds {self.MAX_LENGTH}"
        return encodings.input_ids, encodings.attention_mask

    def LoadSamplesToRam(self, sample_list):
        return self.input_ids[sample_list]

    def UnloadSamplesFromRam(self, sample_list):
        pass
