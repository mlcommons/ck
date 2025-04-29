from datetime import datetime
from pathlib import Path

import mlperf_loadgen as lg

from accuracy_check import run_accuracy_check
from SUT import SUTOffline, SUTServer
from utils import get_logger

DEFAULT_MODEL = "meta-llama/Llama-2-70b-chat-hf"
DEFAULT_DATASET = "ctuning/MLPerf-OpenOrca"

log = get_logger(__name__)


def get_args():
    import argparse

    parser = argparse.ArgumentParser(description="MLPerf Inference")
    parser.add_argument(
        "--model-path",
        default=DEFAULT_MODEL,
        help="HuggingFace model path (e.g., meta-llama/Llama-2-70b-chat-hf)",
    )
    parser.add_argument(
        "--dataset-path",
        default=DEFAULT_DATASET,
        help="HuggingFace dataset path (e.g., AI-MO/NuminaMath-TIR, Open-Orca/OpenOrca) "
        "or local path to a preprocessed pickle file (.pkl or .pkl.gz)",
    )
    parser.add_argument(
        "--dataset-split",
        default="train",
        help="Dataset split to use (e.g., train, validation, test)",
    )
    parser.add_argument(
        "--total-sample-count",
        type=int,
        default=None,
        help="Number of samples to use from dataset. If None (default), uses all available samples",
    )
    parser.add_argument(
        "--scenario",
        choices=["Offline", "Server"],
        required=True,
        help="Benchmark scenario - Offline (batch processing) or Server (real-time serving)",
    )
    parser.add_argument(
        "--target-qps",
        type=float,
        required=True,
        help="Target queries per second for the benchmark",
    )
    parser.add_argument(
        "--accuracy",
        action="store_true",
        help="Run accuracy evaluation instead of performance benchmark",
    )
    parser.add_argument(
        "--api-server",
        default="http://localhost:8000",
        help="URL of the vLLM API server (e.g., http://localhost:8000).",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Override output directory (default: results/{timestamp})",
    )
    return parser.parse_args()


def setup_logging(output_dir: Path) -> lg.LogSettings:
    """Setup logging with the provided output directory"""
    output_dir.mkdir(parents=True, exist_ok=True)
    log_output_settings = lg.LogOutputSettings()
    log_output_settings.outdir = str(output_dir)
    log_output_settings.copy_summary_to_stdout = True

    log_settings = lg.LogSettings()
    log_settings.log_output = log_output_settings
    log_settings.enable_trace = False
    log.info(f"MLPerf logs directory: {output_dir}")
    return log_settings


def setup_test_settings(
    scenario: str, accuracy: bool, target_qps: float | None
) -> lg.TestSettings:
    """Setup test settings based on the provided arguments"""
    test_settings = lg.TestSettings()
    test_settings.scenario = getattr(lg.TestScenario, scenario)
    test_settings.FromConfig("user.conf", "llama2-70b", scenario)
    test_settings.mode = (
        lg.TestMode.AccuracyOnly if accuracy else lg.TestMode.PerformanceOnly
    )
    if target_qps is not None:
        test_settings.offline_expected_qps = target_qps
        test_settings.server_target_qps = target_qps
        log.info(f"Test settings: {scenario=}, {accuracy=}, {target_qps=}")
    else:
        with open("user.conf") as f:
            for line in f:
                if f"{scenario}.target_qps" in line:
                    target_qps = float(line.split("=")[1].strip())
        if target_qps is None:
            raise ValueError("target_qps must be provided in user.conf or as an argument to the script")
        log.info(f"Using target_qps from user.conf: {target_qps}")
    return test_settings


def setup_results_dir(output: str | None) -> Path:
    """Setup results directory based on the provided output path"""
    if output:
        results_dir = Path(output)
    else:
        results_dir = Path("results") / datetime.now().strftime("%Y%m%d-%H%M%S")
    results_dir.mkdir(parents=True, exist_ok=True)
    log.info(f"Results directory: {results_dir}")
    return results_dir


def main():
    args = get_args()

    results_dir = setup_results_dir(args.output)
    test_settings = setup_test_settings(args.scenario, args.accuracy, args.target_qps)
    log_settings = setup_logging(results_dir / "mlperf_logs")

    sut_class = {"Server": SUTServer, "Offline": SUTOffline}[args.scenario]
    log.info(f"Using SUT class: {sut_class}")

    sut = sut_class(
        model_path=args.model_path,
        dataset_path=args.dataset_path,
        dataset_split=args.dataset_split,
        api_server=args.api_server,
        total_sample_count=args.total_sample_count,
    )
    log.info(f"Using model: {args.model_path}")
    log.info(f"Using dataset: {args.dataset_path} ({args.dataset_split})")
    log.info(f"Total sample count: {args.total_sample_count}")

    lg.StartTestWithLogSettings(sut.sut, sut.qsl, test_settings, log_settings)

    sut.stop()
    lg.DestroySUT(sut.sut)
    lg.DestroyQSL(sut.qsl)

    if args.accuracy:
        run_accuracy_check(
            mlperf_accuracy_file=results_dir / "mlperf_logs" / "mlperf_log_accuracy.json",
            model_path=args.model_path,
            dataset_path=args.dataset_path,
            dataset_split=args.dataset_split,
            output_path=results_dir / "accuracy",
            json_export=True,
        )


if __name__ == "__main__":
    main()
