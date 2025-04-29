import argparse
import os

import mlperf_loadgen as lg
from SUT_API import SUT, SUTServer

# Define defaults that will be used across all files
DEFAULT_MODEL = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
DEFAULT_DATASET = "AI-MO/NuminaMath-TIR"
DEFAULT_SAMPLE_COUNT = 24576
DEFAULT_BATCH_SIZE = 32


def get_args():
    parser = argparse.ArgumentParser(description="MLPerf Inference")
    parser.add_argument("--model-path", default=DEFAULT_MODEL)
    parser.add_argument("--dataset-path", default=DEFAULT_DATASET)
    parser.add_argument("--total-sample-count", type=int, default=DEFAULT_SAMPLE_COUNT)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--scenario", choices=["Offline", "Server"], required=True)
    parser.add_argument("--accuracy", action="store_true")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--vllm", action="store_true")
    parser.add_argument("--api-server", default=None)
    return parser.parse_args()


def setup_logging(args):
    log_dir = "mlperf-logs"
    os.makedirs(log_dir, exist_ok=True)

    log_output_settings = lg.LogOutputSettings()
    log_output_settings.outdir = log_dir
    log_output_settings.copy_summary_to_stdout = True

    log_settings = lg.LogSettings()
    log_settings.log_output = log_output_settings
    log_settings.enable_trace = False

    return log_settings


def setup_test_settings(args):
    settings = lg.TestSettings()
    settings.scenario = getattr(lg.TestScenario, args.scenario)
    settings.mode = (
        lg.TestMode.AccuracyOnly if args.accuracy else lg.TestMode.PerformanceOnly
    )

    # Server scenario settings
    if args.scenario == "Server":
        settings.server_target_qps = 1.0
        settings.server_target_latency_ns = 100000000
        settings.server_target_latency_percentile = 0.9
        settings.server_coalesce_queries = True

    # Offline scenario settings
    else:  # args.scenario == "Offline"
        settings.offline_expected_qps = 1.0

    return settings


def main():
    args = get_args()

    settings = setup_test_settings(args)
    log_settings = setup_logging(args)

    sut_args = {
        "model_path": args.model_path,
        "api_server": args.api_server if args.vllm else None,
        "device": args.device,
        "batch_size": args.batch_size,
        "total_sample_count": args.total_sample_count,
        "dataset_path": args.dataset_path,
    }

    sut_class = SUTServer if args.scenario == "Server" else SUT
    sut = sut_class(**sut_args)
    sut.start()

    lg.StartTestWithLogSettings(sut.get_sut(), sut.get_qsl(), settings, log_settings)


if __name__ == "__main__":
    main()
