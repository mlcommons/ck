import importlib.metadata
import json
import os
import platform
import typing as tp
from datetime import datetime
from pathlib import Path

import psutil
import torch
from huggingface_hub import model_info


def get_gpu_info() -> dict:
    if not torch.cuda.is_available():
        return {"available": False}

    return {
        "available": True,
        "name": torch.cuda.get_device_name(0),
        "count": torch.cuda.device_count(),
        "memory_total": torch.cuda.get_device_properties(0).total_memory,
        "compute_capability": f"{torch.cuda.get_device_capability()}",
    }


def get_cuda_info() -> dict:
    """Get detailed CUDA information"""
    if not torch.cuda.is_available():
        return {"available": False}

    try:
        import pynvml

        pynvml.nvmlInit()
        driver_version = pynvml.nvmlSystemGetDriverVersion().decode()
    except Exception:
        driver_version = None

    return {
        "version": torch.version.cuda,
        "cudnn_version": torch.backends.cudnn.version(),
        "driver_version": driver_version,
        "available": True,
        "devices": [
            {
                "name": torch.cuda.get_device_name(i),
                "memory_total": torch.cuda.get_device_properties(i).total_memory,
                "compute_capability": f"{torch.cuda.get_device_capability(i)}",
                "memory_allocated": torch.cuda.memory_allocated(i),
                "memory_reserved": torch.cuda.memory_reserved(i),
                "multi_processor_count": torch.cuda.get_device_properties(
                    i
                ).multi_processor_count,
            }
            for i in range(torch.cuda.device_count())
        ],
    }


def get_system_info() -> dict:
    memory = psutil.virtual_memory()
    return {
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "cpu_count": psutil.cpu_count(),
        "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
        "memory_total": memory.total,
        "memory_available": memory.available,
        "gpu": get_gpu_info(),
    }


def get_vllm_env_vars() -> dict:
    """Get all relevant environment variables for vLLM.
    Source: https://docs.vllm.ai/en/v0.4.3/serving/env_vars.html"""

    environment_variables: tp.Dict[str, tp.Callable[[], tp.Any]] = {
        # ================== Installation Time Env Vars ==================
        # Target device of vLLM, supporting [cuda (by default), rocm, neuron, cpu]
        "VLLM_TARGET_DEVICE": lambda: os.getenv("VLLM_TARGET_DEVICE", "cuda"),
        # Maximum number of compilation jobs to run in parallel.
        # By default this is the number of CPUs
        "MAX_JOBS": lambda: os.getenv("MAX_JOBS", None),
        # Number of threads to use for nvcc
        # By default this is 1.
        # If set, `MAX_JOBS` will be reduced to avoid oversubscribing the CPU.
        "NVCC_THREADS": lambda: os.getenv("NVCC_THREADS", None),
        # If set, vllm will build with Neuron support
        "VLLM_BUILD_WITH_NEURON": lambda: bool(
            os.environ.get("VLLM_BUILD_WITH_NEURON", False)
        ),
        # If set, vllm will use precompiled binaries (*.so)
        "VLLM_USE_PRECOMPILED": lambda: bool(os.environ.get("VLLM_USE_PRECOMPILED")),
        # If set, vllm will install Punica kernels
        "VLLM_INSTALL_PUNICA_KERNELS": lambda: bool(
            int(os.getenv("VLLM_INSTALL_PUNICA_KERNELS", "0"))
        ),
        # CMake build type
        # If not set, defaults to "Debug" or "RelWithDebInfo"
        # Available options: "Debug", "Release", "RelWithDebInfo"
        "CMAKE_BUILD_TYPE": lambda: os.getenv("CMAKE_BUILD_TYPE"),
        # If set, vllm will print verbose logs during installation
        "VERBOSE": lambda: bool(int(os.getenv("VERBOSE", "0"))),
        # Root directory for VLLM configuration files
        # Note that this not only affects how vllm finds its configuration files
        # during runtime, but also affects how vllm installs its configuration
        # files during **installation**.
        "VLLM_CONFIG_ROOT": lambda: os.environ.get("VLLM_CONFIG_ROOT", None)
        or os.getenv("XDG_CONFIG_HOME", None)
        or os.path.expanduser("~/.config"),
        # ================== Runtime Env Vars ==================
        # used in distributed environment to determine the master address
        "VLLM_HOST_IP": lambda: os.getenv("VLLM_HOST_IP", "")
        or os.getenv("HOST_IP", ""),
        # used in distributed environment to manually set the communication port
        # '0' is used to make mypy happy
        "VLLM_PORT": lambda: (
            int(os.getenv("VLLM_PORT", "0")) if "VLLM_PORT" in os.environ else None
        ),
        # If true, will load models from ModelScope instead of Hugging Face Hub.
        # note that the value is true or false, not numbers
        "VLLM_USE_MODELSCOPE": lambda: os.environ.get(
            "VLLM_USE_MODELSCOPE", "False"
        ).lower()
        == "true",
        # Instance id represents an instance of the VLLM. All processes in the same
        # instance should have the same instance id.
        "VLLM_INSTANCE_ID": lambda: os.environ.get("VLLM_INSTANCE_ID", None),
        # path to cudatoolkit home directory, under which should be bin, include,
        # and lib directories.
        "CUDA_HOME": lambda: os.environ.get("CUDA_HOME", None),
        # Path to the NCCL library file. It is needed because nccl>=2.19 brought
        # by PyTorch contains a bug: https://github.com/NVIDIA/nccl/issues/1234
        "VLLM_NCCL_SO_PATH": lambda: os.environ.get("VLLM_NCCL_SO_PATH", None),
        # when `VLLM_NCCL_SO_PATH` is not set, vllm will try to find the nccl
        # library file in the locations specified by `LD_LIBRARY_PATH`
        "LD_LIBRARY_PATH": lambda: os.environ.get("LD_LIBRARY_PATH", None),
        # flag to control if vllm should use triton flash attention
        "VLLM_USE_TRITON_FLASH_ATTN": lambda: (
            os.environ.get("VLLM_USE_TRITON_FLASH_ATTN", "True").lower()
            in ("true", "1")
        ),
        # local rank of the process in the distributed setting, used to determine
        # the GPU device id
        "LOCAL_RANK": lambda: int(os.environ.get("LOCAL_RANK", "0")),
        # used to control the visible devices in the distributed setting
        "CUDA_VISIBLE_DEVICES": lambda: os.environ.get("CUDA_VISIBLE_DEVICES", None),
        # timeout for each iteration in the engine
        "VLLM_ENGINE_ITERATION_TIMEOUT_S": lambda: int(
            os.environ.get("VLLM_ENGINE_ITERATION_TIMEOUT_S", "60")
        ),
        # API key for VLLM API server
        "VLLM_API_KEY": lambda: os.environ.get("VLLM_API_KEY", None),
        # S3 access information, used for tensorizer to load model from S3
        "S3_ACCESS_KEY_ID": lambda: os.environ.get("S3_ACCESS_KEY_ID", None),
        "S3_SECRET_ACCESS_KEY": lambda: os.environ.get("S3_SECRET_ACCESS_KEY", None),
        "S3_ENDPOINT_URL": lambda: os.environ.get("S3_ENDPOINT_URL", None),
        # Usage stats collection
        "VLLM_USAGE_STATS_SERVER": lambda: os.environ.get(
            "VLLM_USAGE_STATS_SERVER", "https://stats.vllm.ai"
        ),
        "VLLM_NO_USAGE_STATS": lambda: os.environ.get("VLLM_NO_USAGE_STATS", "0")
        == "1",
        "VLLM_DO_NOT_TRACK": lambda: (
            os.environ.get("VLLM_DO_NOT_TRACK", None)
            or os.environ.get("DO_NOT_TRACK", None)
            or "0"
        )
        == "1",
        "VLLM_USAGE_SOURCE": lambda: os.environ.get("VLLM_USAGE_SOURCE", "production"),
        # Logging configuration
        # If set to 0, vllm will not configure logging
        # If set to 1, vllm will configure logging using the default configuration
        #    or the configuration file specified by VLLM_LOGGING_CONFIG_PATH
        "VLLM_CONFIGURE_LOGGING": lambda: int(os.getenv("VLLM_CONFIGURE_LOGGING", "1")),
        "VLLM_LOGGING_CONFIG_PATH": lambda: os.getenv("VLLM_LOGGING_CONFIG_PATH"),
        # this is used for configuring the default logging level
        "VLLM_LOGGING_LEVEL": lambda: os.getenv("VLLM_LOGGING_LEVEL", "INFO"),
        # Trace function calls
        # If set to 1, vllm will trace function calls
        # Useful for debugging
        "VLLM_TRACE_FUNCTION": lambda: int(os.getenv("VLLM_TRACE_FUNCTION", "0")),
        # Backend for attention computation
        # Available options:
        # - "TORCH_SDPA": use torch.nn.MultiheadAttention
        # - "FLASH_ATTN": use FlashAttention
        # - "XFORMERS": use XFormers
        # - "ROCM_FLASH": use ROCmFlashAttention
        "VLLM_ATTENTION_BACKEND": lambda: os.getenv("VLLM_ATTENTION_BACKEND", None),
        # CPU key-value cache space
        # default is 4GB
        "VLLM_CPU_KVCACHE_SPACE": lambda: int(os.getenv("VLLM_CPU_KVCACHE_SPACE", "0")),
        # If the env var is set, it uses the Ray's compiled DAG API
        # which optimizes the control plane overhead.
        # Run vLLM with VLLM_USE_RAY_COMPILED_DAG=1 to enable it.
        "VLLM_USE_RAY_COMPILED_DAG": lambda: bool(
            os.getenv("VLLM_USE_RAY_COMPILED_DAG", 0)
        ),
        # Use dedicated multiprocess context for workers.
        # Both spawn and fork work
        "VLLM_WORKER_MULTIPROC_METHOD": lambda: os.getenv(
            "VLLM_WORKER_MULTIPROC_METHOD", "spawn"
        ),
    }
    return {k: v() for k, v in environment_variables.items()}


def get_packages_info() -> dict:
    """Get infos of all relevant packages"""

    def pkg_version(pkg: str) -> str | tp.NoReturn:
        try:
            return importlib.metadata.version(pkg)
        except importlib.metadata.PackageNotFoundError:
            return None

    packages = {
        "vllm": pkg_version("vllm"),
        "torch": pkg_version("torch"),
        "cuda": torch.version.cuda,
        "cudnn_version": (
            torch.backends.cudnn.version() if torch.cuda.is_available() else None
        ),
        "cuda_available": torch.cuda.is_available(),
        "mps_available": torch.backends.mps.is_available(),
        "parallel_mode": os.environ.get("WORLD_SIZE"),
        "hip_version": torch.version.hip if hasattr(torch.version, "hip") else None,
        "openmp_version": (
            torch.version.openmp if hasattr(torch.version, "openmp") else None
        ),
        "mkl_version": torch.version.mkl if hasattr(torch.version, "mkl") else None,
        "transformers": pkg_version("transformers"),
        "flash-attn": pkg_version("flash-attn"),
        "triton": pkg_version("triton"),
        "bitsandbytes": pkg_version("bitsandbytes"),
        "ninja": pkg_version("ninja"),
        "xformers": pkg_version("xformers"),
        "numpy": pkg_version("numpy"),
        "datasets": pkg_version("datasets"),
        "accelerate": pkg_version("accelerate"),
        "safetensors": pkg_version("safetensors"),
        "sentencepiece": pkg_version("sentencepiece"),
        "tokenizers": pkg_version("tokenizers"),
        "mlperf_loadgen": pkg_version("mlcommons_loadgen"),
    }
    return packages


def get_model_info(model_name) -> dict:
    info = model_info(model_name)
    return {
        "name": info.modelId,
        "sha": info.sha,
        "last_modified": str(info.lastModified),
        "tags": info.tags,
        "pipeline_tag": info.pipeline_tag,
    }


def collect_experiment_info(args) -> dict:
    """Collect all relevant information about the experiment"""
    info = {
        "timestamp": datetime.now().isoformat(),
        "system": get_system_info(),
        "vllm_env_vars": get_vllm_env_vars(),
        "packages": get_packages_info(),
        "model": get_model_info(args.model_path),
        "config": {
            "scenario": args.scenario,
            "model_path": args.model_path,
            "dataset": args.dataset_path,
            "accuracy_mode": args.accuracy,
            "total_sample_count": args.total_sample_count,
            "api_server": args.api_server,
        },
    }
    return info


def setup_experiment(args, output_dir=None) -> dict[str, Path]:
    """Setup experiment directory and save experiment information
    Args:
        args: Experiment arguments
        output_dir: Optional output directory override (default: results/{timestamp})
    Returns:
        dict: Paths to experiment directories and files
    """
    if output_dir:
        base_dir = Path(output_dir)
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_dir = Path("results") / timestamp

    base_dir.mkdir(parents=True, exist_ok=True)
    mlperf_dir = base_dir / "mlperf-logs"
    mlperf_dir.mkdir(exist_ok=True)

    info = collect_experiment_info(args)
    info_file = base_dir / "system_info.json"
    with open(info_file, "w") as f:
        json.dump(info, f, indent=4)

    return {
        "base": base_dir,
        "mlperf_logs": mlperf_dir,
        "system_info": info_file,
    }
