import argparse
import contextlib
import logging
import os
import re
import typing

import mlperf_loadgen
import psutil

from loadgen.harness import Harness, ModelRunner
from loadgen.runners import (
    ModelRunnerInline,
    ModelRunnerMultiProcessingPool,
    ModelRunnerProcessPoolExecutor,
    ModelRunnerThreadPoolExecutor,
    ModelRunnerThreadPoolExecutorWithTLS,
)

logger = logging.getLogger(__name__)


def main(
    backend: str,
    model_path: str,
    model_code: str,
    model_cfg: str,
    model_sample_pickle: str,
    output_path: typing.Optional[str],
    runner_name: str,
    runner_concurrency: int,
    execution_provider: str,
    execution_mode: str,
    intraop_threads: int,
    interop_threads: int,
    samples: int,
    loadgen_expected_qps: float,
    loadgen_duration_sec: float
):
    
    print ('=====================================================================')
    
    if backend == 'onnxruntime':
        from backend_onnxruntime import XModelFactory
        from backend_onnxruntime import XModelInputSampler
    elif backend == 'pytorch':
        from backend_pytorch import XModelFactory
        from backend_pytorch import XModelInputSampler
    else:
        raise Exception("Error: backend is not recognized.")

    # Load model cfg
    model_cfg_dict = {}
    if model_cfg!='':
        import json

        with open(model_cfg) as mc:
            model_cfg_dict = json.load(mc)
    
    model_factory = XModelFactory(
         model_path,
         execution_provider,
         execution_mode,
         interop_threads,
         intraop_threads,
         model_code,
         model_cfg_dict,
         model_sample_pickle
    )
    
    model_dataset = XModelInputSampler(model_factory)
    
    runner: ModelRunner = None
    if runner_name == "inline":
        runner = ModelRunnerInline(model_factory)
    elif runner_name == "threadpool":
        runner = ModelRunnerThreadPoolExecutor(
            model_factory, max_concurrency=runner_concurrency
        )
    elif runner_name == "threadpool+replication":
        runner = ModelRunnerThreadPoolExecutorWithTLS(
            model_factory, max_concurrency=runner_concurrency
        )
    elif runner_name == "processpool":
        runner = ModelRunnerProcessPoolExecutor(
            model_factory, max_concurrency=runner_concurrency
        )
    elif runner_name == "processpool+mp":
        runner = ModelRunnerMultiProcessingPool(
            model_factory, max_concurrency=runner_concurrency
        )
    else:
        raise ValueError(f"Invalid runner {runner}")

    settings = mlperf_loadgen.TestSettings()

    settings.scenario = mlperf_loadgen.TestScenario.Offline
    settings.mode = mlperf_loadgen.TestMode.PerformanceOnly
    settings.offline_expected_qps = loadgen_expected_qps
    settings.min_query_count = samples
    settings.max_query_count = samples
    settings.min_duration_ms = loadgen_duration_sec * 1000
    # Duration isn't enforced in offline mode
    # Instead, it is used to determine total sample count via
    # target_sample_count = Slack (1.1) * TargetQPS (1) * TargetDuration ()
    # samples_per_query = Max(min_query_count, target_sample_count)

    output_path = "results" if not output_path else output_path
    output_path = os.path.join(output_path, os.path.basename(model_path), runner_name)
    os.makedirs(output_path, exist_ok=True)

    output_settings = mlperf_loadgen.LogOutputSettings()
    output_settings.outdir = output_path
    output_settings.copy_summary_to_stdout = True

    log_settings = mlperf_loadgen.LogSettings()
    log_settings.log_output = output_settings
    log_settings.enable_trace = False

    logger.info(f"Model: {model_path}")
    logger.info(f"Runner: {runner_name}, Concurrency: {runner_concurrency}")
    logger.info(f"Results: {output_path}")

    with contextlib.ExitStack() as stack:
        stack.enter_context(runner)
        harness = Harness(model_dataset, runner)

        query_sample_libary = mlperf_loadgen.ConstructQSL(
            samples,  # Total sample count
            samples,  # Num to load in RAM at a time
            harness.load_query_samples,
            harness.unload_query_samples,
        )
        system_under_test = mlperf_loadgen.ConstructSUT(
            harness.issue_query, harness.flush_queries
        )

        print ('=====================================================================')
        logger.info("Test Started")

        mlperf_loadgen.StartTestWithLogSettings(
            system_under_test, query_sample_libary, settings, log_settings
        )

        logger.info("Test Finished")
        print ('=====================================================================')

        # Parse output file
        output_summary = {}
        output_summary_path = os.path.join(output_path, "mlperf_log_summary.txt")
        with open(output_summary_path, "r") as output_summary_file:
            for line in output_summary_file:
                m = re.match(r"^\s*([\w\s.\(\)\/]+)\s*\:\s*([\w\+\.]+).*", line)
                if m:
                    output_summary[m.group(1).strip()] = m.group(2).strip()
        logger.info("Observed QPS: " + output_summary.get("Samples per second"))
        logger.info("Result: " + output_summary.get("Result is"))

        mlperf_loadgen.DestroySUT(system_under_test)
        mlperf_loadgen.DestroyQSL(query_sample_libary)
        logger.info("Test Completed")
        print ('=====================================================================')


if __name__ == "__main__":
    print ('')
    
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(threadName)s - %(name)s %(funcName)s: %(message)s",
    )

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "model_path", help="path to input model", default="models/yolov5s.onnx"
    )
    parser.add_argument("-b", "--backend", help="backend", default="onnxruntime")
    parser.add_argument("-o", "--output", help="path to store loadgen results")
    parser.add_argument(
        "-r",
        "--runner",
        help="model runner",
        choices=[
            "inline",
            "threadpool",
            "threadpool+replication",
            "processpool",
            "processpool+mp",
        ],
        default="inline",
    )
    parser.add_argument(
        "--concurrency",
        help="concurrency count for runner",
        default=psutil.cpu_count(False),
        type=int,
    )
    parser.add_argument(
        "--ep", help="Execution Provider", default="CPUExecutionProvider"
    )
    parser.add_argument("--intraop", help="IntraOp threads", default=0, type=int)
    parser.add_argument("--interop", help="InterOp threads", default=0, type=int)
    parser.add_argument(
        "--execmode",
        help="Execution Mode",
        choices=["sequential", "parallel"],
        default="sequential",
    )
    parser.add_argument(
        "--samples",
        help="number of samples",
        default=100,
        type=int,
    )
    parser.add_argument("--loadgen_expected_qps", help="Expected QPS", default=1, type=float)
    parser.add_argument("--loadgen_duration_sec", help="Expected duration in sec.", default=1, type=float)
    parser.add_argument("--model_code", help="(for PyTorch models) path to model code with cmc.py", default="")
    parser.add_argument("--model_cfg", help="(for PyTorch models) path to model's configuration in JSON file", default="")
    parser.add_argument("--model_sample_pickle", help="(for PyTorch models) path to a model sample in pickle format", default="")

    args = parser.parse_args()
    main(
        args.backend,
        args.model_path,
        args.model_code,
        args.model_cfg,
        args.model_sample_pickle,
        args.output,
        args.runner,
        args.concurrency,
        args.ep,
        args.execmode,
        args.intraop,
        args.interop,
        args.samples,
        args.loadgen_expected_qps,
        args.loadgen_duration_sec
    )
