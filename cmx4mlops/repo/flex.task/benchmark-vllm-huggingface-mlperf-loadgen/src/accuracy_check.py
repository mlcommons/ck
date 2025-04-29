import json
import os
from multiprocessing import Pool, cpu_count
from pathlib import Path

import evaluate
import nltk
import numpy as np
import pandas as pd
from datasets import load_dataset
from tqdm import tqdm
from transformers import AutoTokenizer

from dataset import Dataset
from utils import get_logger

log = get_logger(__name__)

os.environ["TOKENIZERS_PARALLELISM"] = "true"


def normalize_text(text: str | list[str]) -> str | list[str]:
    """Normalize text by stripping and formatting into sentences."""
    if isinstance(text, list):
        return [normalize_text(t) for t in text]
    return "\n".join(nltk.sent_tokenize(text.strip()))


def compute_rouge_chunk(args):
    """Compute ROUGE scores for a chunk of predictions and references."""
    metric, preds, targets = args
    result = metric.compute(
        predictions=preds, references=targets, use_stemmer=True, use_aggregator=False
    )
    return result


def compute_rouge_scores(preds: list[str], refs: list[str]) -> tuple[dict, int]:
    """Compute ROUGE scores and token statistics."""
    metric = evaluate.load("rouge")

    n_workers = cpu_count()
    chunk_size = len(preds) // n_workers + 1
    chunks = [
        (metric, preds[i : i + chunk_size], refs[i : i + chunk_size])
        for i in range(0, len(preds), chunk_size)
    ]

    with Pool() as pool:
        results_list = pool.map(compute_rouge_chunk, chunks)

    scores = {k: [] for k in results_list[0].keys()}
    for result in results_list:
        for k, v in result.items():
            scores[k].extend(v)

    return scores, sum(len(p) for p in preds)


def get_references(
    dataset_path: str, dataset_split: str = "train"
) -> dict[str, list[str]]:
    """Load reference outputs, system prompts and inputs from either HF dataset or pickle file."""
    if dataset_path.endswith(".pkl.gz") or dataset_path.endswith(".pkl"):
        data = pd.read_pickle(dataset_path)
        output_col = next(col for col in ["output", "response"] if col in data)
        return {
            "references": data[output_col].tolist(),
            "system_prompts": data["system_prompt"].tolist(),
            "inputs": data["question"].tolist(),
        }

    mapping = Dataset.DATASET_CONFIGS[dataset_path]
    dataset = load_dataset(dataset_path, split=dataset_split)
    return {
        "references": [item[mapping["output_column"]] for item in dataset],
        "system_prompts": [
            item.get(mapping.get("system_prompt_column", "")) for item in dataset
        ],
        "inputs": [item[mapping["input_column"]] for item in dataset],
    }


def get_accuracy_paths(output_path: str | Path) -> tuple[Path, Path]:
    """Create and return accuracy-related paths."""
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path / "accuracy.txt", output_path / "accuracy_details.json"


def run_accuracy_check(
    model_path: str,
    dataset_path: str,
    mlperf_accuracy_file: str | Path,
    output_path: str | Path,
    json_export: bool = True,
    dataset_split: str = "train",
    dtype: str = "int32",
) -> None:
    """Run accuracy checking programmatically."""
    log.info("Starting accuracy evaluation")

    if isinstance(mlperf_accuracy_file, str):
        mlperf_accuracy_file = Path(mlperf_accuracy_file)

    output_path = output_path or mlperf_accuracy_file.parent.parent / "accuracy"
    accuracy_txt, accuracy_json = get_accuracy_paths(output_path)

    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)

    log.info(f"Loading tokenizer from {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        padding_side="left",
        use_fast=True,
        add_prefix_space=None if "deepseek" in model_path.lower() else False,
    )

    log.info(
        f"Loading references from {dataset_path} ({dataset_split}) ... "
        f"This may take a while if the original dataset is large."
    )
    data = get_references(dataset_path, dataset_split)
    log.info(f"Loaded {len(data['references'])} references")

    samples = []
    gen_tok_len = 0

    tokens_list = []
    valid_indices = []
    for pred in tqdm(
        json.load(open(mlperf_accuracy_file)),
        desc="Decoding predictions (hex -> token_id)",
    ):
        idx = pred["qsl_idx"]
        if idx >= len(data["references"]) or any(
            s["reference"] == data["references"][idx] for s in samples
        ):
            continue

        tokens = [
            t
            for t in np.frombuffer(bytes.fromhex(pred["data"]), dtype)
            if 0 <= t <= tokenizer.vocab_size
        ]
        gen_tok_len += len(tokens)
        tokens_list.append(tokens)
        valid_indices.append(idx)

    log.info(
        f"Decoding {len(tokens_list)} predictions (token_id -> text) using tokenizer... "
        "This may take a while."
    )
    predictions_decoded = tokenizer.batch_decode(tokens_list, skip_special_tokens=True)

    samples = [
        {
            "system_prompt": data["system_prompts"][idx],
            "input": data["inputs"][idx],
            "reference": data["references"][idx],
            "prediction": normalize_text(pred_text),
        }
        for idx, pred_text in zip(valid_indices, predictions_decoded)
    ]

    log.info(f"Computing ROUGE scores for {len(samples)} predictions")
    predictions = [s["prediction"] for s in samples]
    targets = [normalize_text(s["reference"]) for s in samples]
    scores, total_len = compute_rouge_scores(predictions, targets)

    metrics = {
        **{k: round(np.mean(v) * 100, 4) for k, v in scores.items()},
        "gen_len": total_len,
        "gen_num": len(samples),
        "gen_tok_len": gen_tok_len,
        "tokens_per_sample": round(gen_tok_len / len(samples), 1),
    }

    with open(accuracy_txt, "w") as f:
        f.write("\nResults\n\n" + str(metrics))
        log.info(f"Results exported to {accuracy_txt}")
    log.info(f"Results: {metrics}")

    if json_export:
        pd.DataFrame(
            [
                {
                    **sample,
                    "prediction": pred,
                    **{k: round(v[i] * 100, 4) for k, v in scores.items()},
                }
                for i, (sample, pred) in enumerate(zip(samples, predictions))
            ]
        ).to_json(accuracy_json, indent=2, orient="records")
        log.info(f"Detailed results exported to {accuracy_json}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run accuracy evaluation")
    parser.add_argument(
        "--mlperf-accuracy-file", type=str, help="Path to the MLPerf accuracy file"
    )
    parser.add_argument("--model-path", type=str, help="Path to the model")
    parser.add_argument("--dataset-path", type=str, help="Path to the dataset")
    parser.add_argument(
        "--dataset-split", type=str, default="train", help="Dataset split to use"
    )
    parser.add_argument("--output-path", type=str, help="Path to the output directory")
    parser.add_argument(
        "--json-export", action="store_true", help="Export detailed results to JSON"
    )
    parser.add_argument(
        "--dtype", type=str, default="int32", help="Data type for token IDs"
    )
    args = parser.parse_args()

    run_accuracy_check(
        args.model_path,
        args.dataset_path,
        args.mlperf_accuracy_file,
        args.output_path,
        args.json_export,
        args.dataset_split,
        args.dtype,
    )
