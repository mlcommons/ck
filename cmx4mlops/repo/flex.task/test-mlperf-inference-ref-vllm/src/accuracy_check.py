import argparse
import json
from pathlib import Path

import evaluate
import nltk
import numpy as np
import pandas as pd
from datasets import load_dataset
from main import DEFAULT_DATASET, DEFAULT_MODEL
from tqdm import tqdm
from transformers import AutoTokenizer


def get_args():
    parser = argparse.ArgumentParser(description="Analyze MLPerf inference results")
    parser.add_argument("--model-path", default=DEFAULT_MODEL)
    parser.add_argument("--dataset-path", default=DEFAULT_DATASET)
    parser.add_argument(
        "--mlperf-accuracy-file",
        default="mlperf-logs/mlperf_log_accuracy.json",
        help="Path to mlperf_log_accuracy.json",
    )
    parser.add_argument("--split", default="test", help="Dataset split to evaluate")
    parser.add_argument(
        "--output-path",
        default="accuracy_results.csv",
        help="Path to save detailed results DataFrame",
    )
    parser.add_argument(
        "--dtype",
        default="int64",
        choices=["int32", "int64", "float"],
        help="dtype of the accuracy log",
    )
    return parser.parse_args()


def process_mlperf_results(accuracy_file, dtype):
    """Process MLPerf accuracy logs into a clean dictionary."""
    with open(accuracy_file, "r") as f:
        results = json.load(f)

    processed = {}
    for pred in results:
        idx = pred["qsl_idx"]
        if idx not in processed:
            processed[idx] = np.frombuffer(
                bytes.fromhex(pred["data"]), dtype=getattr(np, dtype)
            )
    return processed


def main():
    args = get_args()
    nltk.download("punkt", quiet=True)

    print("Loading dataset and model...")
    dataset = load_dataset(args.dataset_path, split=args.split)
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)

    print("Processing MLPerf results...")
    results = process_mlperf_results(args.mlperf_accuracy_file, args.dtype)

    df = pd.DataFrame(
        {
            "query_idx": list(results.keys()),
            "problem": [dataset[idx]["problem"] for idx in results.keys()],
            "solution": [dataset[idx]["solution"] for idx in results.keys()],
            "prediction_tokens": list(results.values()),
        }
    )

    df["prediction"] = [
        tokenizer.decode(tokens, skip_special_tokens=True)
        for tokens in tqdm(df.prediction_tokens, desc="Decoding predictions")
    ]
    df["prediction_length"] = [len(tokens) for tokens in df.prediction_tokens]

    print("\nCalculating metrics...")

    def _preproc(s: str) -> str:
        s = s.strip()
        return "\n".join(nltk.sent_tokenize(s))

    metric = evaluate.load("rouge")
    rouge_scores = metric.compute(
        predictions=df["prediction"].map(_preproc),
        references=df["solution"].map(_preproc),
        use_stemmer=True,
        use_aggregator=False,
    )

    for metric_name, scores in rouge_scores.items():
        df[metric_name] = scores

    print("\nAnalysis Summary")
    print("-" * 50)
    print(f"Total samples evaluated: {len(df)}")
    print(f"Average prediction length: {df.prediction_length.mean():.1f} tokens")
    print("\nROUGE Scores:")
    for metric_name, scores in rouge_scores.items():
        print(f"{metric_name}: {np.mean(scores)*100:.2f}")

    output_path = Path(args.output_path)
    output_path.parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nDetailed results saved to {output_path}")


if __name__ == "__main__":
    main()
