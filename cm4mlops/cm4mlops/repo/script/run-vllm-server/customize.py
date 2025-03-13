#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os
import subprocess


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    cmd_args = ""

    model_name = env.get("CM_VLLM_SERVER_MODEL_NAME", False)
    if not model_name:
        return {'return': 1, 'error': 'Model name not specified'}
    else:
        cmd_args += f" --model {env['CM_ML_MODEL_PATH']} --served-model-name {model_name}"

    tp_size = env.get("CM_VLLM_SERVER_TP_SIZE", False)
    if tp_size:
        cmd_args += f" --tensor-parallel-size {tp_size}"

    pp_size = env.get("CM_VLLM_SERVER_PP_SIZE", False)
    if pp_size:
        cmd_args += f" --pipeline-parallel-size {pp_size}"

    api_key = env.get("CM_VLLM_SERVER_API_KEY", "root")
    if pp_size:
        cmd_args += f" --api-key {api_key}"

    distributed_executor_backend = env.get(
        "CM_VLLM_SERVER_DIST_EXEC_BACKEND", False)
    if distributed_executor_backend:
        cmd_args += f" --distributed-executor-backend {distributed_executor_backend}"

    host = env.get("CM_VLLM_SERVER_HOST", False)
    if host:
        cmd_args += f" --host {host}"

    port = env.get("CM_VLLM_SERVER_PORT", False)
    if port:
        cmd_args += f" --port {port}"

    uvicorn_log_level = env.get("CM_VLLM_SERVER_UVICORN_LOG_LEVEL", False)
    if uvicorn_log_level:
        cmd_args += f" --uvicorn-log-level {uvicorn_log_level}"

    allow_credentials = env.get("CM_VLLM_SERVER_ALLOW_CREDENTIALS", False)
    if allow_credentials:
        cmd_args += f" --allow-credentials"

    allowed_origins = env.get("CM_VLLM_SERVER_ALLOWED_ORIGINS", False)
    if allowed_origins:
        cmd_args += f" --allowed-origins {allowed_origins}"

    allowed_methods = env.get("CM_VLLM_SERVER_ALLOWED_METHODS", False)
    if allowed_methods:
        cmd_args += f" --allowed-methods {allowed_methods}"

    allowed_headers = env.get("CM_VLLM_SERVER_ALLOWED_HEADERS", False)
    if allowed_headers:
        cmd_args += f" --allowed-headers {allowed_headers}"

    lora_modules = env.get("CM_VLLM_SERVER_LORA_MODULES", False)
    if lora_modules:
        cmd_args += f" --lora-modules {lora_modules}"

    prompt_adapters = env.get("CM_VLLM_SERVER_PROMPT_ADAPTERS", False)
    if prompt_adapters:
        cmd_args += f" --prompt-adapters {prompt_adapters}"

    chat_template = env.get("CM_VLLM_SERVER_CHAT_TEMPLATE", False)
    if chat_template:
        cmd_args += f" --chat-template {chat_template}"

    response_role = env.get("CM_VLLM_SERVER_RESPONSE_ROLE", False)
    if response_role:
        cmd_args += f" --response-role {response_role}"

    ssl_keyfile = env.get("CM_VLLM_SERVER_SSL_KEYFILE", False)
    if ssl_keyfile:
        cmd_args += f" --ssl-keyfile {ssl_keyfile}"

    ssl_certfile = env.get("CM_VLLM_SERVER_SSL_CERTFILE", False)
    if ssl_certfile:
        cmd_args += f" --ssl-certfile {ssl_certfile}"

    ssl_ca_certs = env.get("CM_VLLM_SERVER_SSL_CA_CERTS", False)
    if ssl_ca_certs:
        cmd_args += f" --ssl-ca-certs {ssl_ca_certs}"

    ssl_cert_reqs = env.get("CM_VLLM_SERVER_SSL_CERT_REQS", False)
    if ssl_cert_reqs:
        cmd_args += f" --ssl-cert-reqs {ssl_cert_reqs}"

    root_path = env.get("CM_VLLM_SERVER_ROOT_PATH", False)
    if root_path:
        cmd_args += f" --root-path {root_path}"

    middleware = env.get("CM_VLLM_SERVER_MIDDLEWARE", False)
    if middleware:
        cmd_args += f" --middleware {middleware}"

    tokenizer = env.get("CM_VLLM_SERVER_TOKENIZER", False)
    if tokenizer:
        cmd_args += f" --tokenizer {tokenizer}"

    skip_tokenizer_init = env.get("CM_VLLM_SERVER_SKIP_TOKENIZER_INIT", False)
    if skip_tokenizer_init:
        cmd_args += f" --skip-tokenizer-init"

    revision = env.get("CM_VLLM_SERVER_REVISION", False)
    if revision:
        cmd_args += f" --revision {revision}"

    code_revision = env.get("CM_VLLM_SERVER_CODE_REVISION", False)
    if code_revision:
        cmd_args += f" --code-revision {code_revision}"

    tokenizer_revision = env.get("CM_VLLM_SERVER_TOKENIZER_REVISION", False)
    if tokenizer_revision:
        cmd_args += f" --tokenizer-revision {tokenizer_revision}"

    tokenizer_mode = env.get("CM_VLLM_SERVER_TOKENIZER_MODE", False)
    if tokenizer_mode:
        cmd_args += f" --tokenizer-mode {tokenizer_mode}"

    trust_remote_code = env.get("CM_VLLM_SERVER_TRUST_REMOTE_CODE", False)
    if trust_remote_code:
        cmd_args += f" --trust-remote-code"

    download_dir = env.get("CM_VLLM_SERVER_DOWNLOAD_DIR", False)
    if download_dir:
        cmd_args += f" --download-dir {download_dir}"

    load_format = env.get("CM_VLLM_SERVER_LOAD_FORMAT", False)
    if load_format:
        cmd_args += f" --load-format {load_format}"

    dtype = env.get("CM_VLLM_SERVER_DTYPE", False)
    if dtype:
        cmd_args += f" --dtype {dtype}"

    kv_cache_dtype = env.get("CM_VLLM_SERVER_KV_CACHE_DTYPE", False)
    if kv_cache_dtype:
        cmd_args += f" --kv-cache-dtype {kv_cache_dtype}"

    quantization_param_path = env.get(
        "CM_VLLM_SERVER_QUANTIZATION_PARAM_PATH", False)
    if quantization_param_path:
        cmd_args += f" --quantization-param-path {quantization_param_path}"

    max_model_len = env.get("CM_VLLM_SERVER_MAX_MODEL_LEN", False)
    if max_model_len:
        cmd_args += f" --max-model-len {max_model_len}"

    guided_decoding_backend = env.get(
        "CM_VLLM_SERVER_GUIDED_DECODING_BACKEND", False)
    if guided_decoding_backend:
        cmd_args += f" --guided-decoding-backend {guided_decoding_backend}"

    worker_use_ray = env.get("CM_VLLM_SERVER_WORKER_USE_RAY", False)
    if worker_use_ray:
        cmd_args += f" --worker-use-ray"

    max_parallel_loading_workers = env.get(
        "CM_VLLM_SERVER_MAX_PARALLEL_LOADING_WORKERS", False)
    if max_parallel_loading_workers:
        cmd_args += f" --max-parallel-loading-workers {max_parallel_loading_workers}"

    ray_workers_use_nsight = env.get(
        "CM_VLLM_SERVER_RAY_WORKERS_USE_NSIGHT", False)
    if ray_workers_use_nsight:
        cmd_args += f" --ray-workers-use-nsight"

    block_size = env.get("CM_VLLM_SERVER_BLOCK_SIZE", False)
    if block_size:
        cmd_args += f" --block-size {block_size}"

    enable_prefix_caching = env.get(
        "CM_VLLM_SERVER_ENABLE_PREFIX_CACHING", False)
    if enable_prefix_caching:
        cmd_args += f" --enable-prefix-caching"

    disable_sliding_window = env.get(
        "CM_VLLM_SERVER_DISABLE_SLIDING_WINDOW", False)
    if disable_sliding_window:
        cmd_args += f" --disable-sliding-window"

    use_v2_block_manager = env.get(
        "CM_VLLM_SERVER_USE_V2_BLOCK_MANAGER", False)
    if use_v2_block_manager:
        cmd_args += f" --use-v2-block-manager"

    num_lookahead_slots = env.get("CM_VLLM_SERVER_NUM_LOOKAHEAD_SLOTS", False)
    if num_lookahead_slots:
        cmd_args += f" --num-lookahead-slots {num_lookahead_slots}"

    seed = env.get("CM_VLLM_SERVER_SEED", False)
    if seed:
        cmd_args += f" --seed {seed}"

    swap_space = env.get("CM_VLLM_SERVER_SWAP_SPACE", False)
    if swap_space:
        cmd_args += f" --swap-space {swap_space}"

    gpu_memory_utilization = env.get(
        "CM_VLLM_SERVER_GPU_MEMORY_UTILIZATION", False)
    if gpu_memory_utilization:
        cmd_args += f" --gpu-memory-utilization {gpu_memory_utilization}"

    num_gpu_blocks_override = env.get(
        "CM_VLLM_SERVER_NUM_GPU_BLOCKS_OVERRIDE", False)
    if num_gpu_blocks_override:
        cmd_args += f" --num-gpu-blocks-override {num_gpu_blocks_override}"

    max_num_batched_tokens = env.get(
        "CM_VLLM_SERVER_MAX_NUM_BATCHED_TOKENS", False)
    if max_num_batched_tokens:
        cmd_args += f" --max-num-batched-tokens {max_num_batched_tokens}"

    max_num_seqs = env.get("CM_VLLM_SERVER_MAX_NUM_SEQS", False)
    if max_num_seqs:
        cmd_args += f" --max-num-seqs {max_num_seqs}"

    max_logprobs = env.get("CM_VLLM_SERVER_MAX_LOGPROBS", False)
    if max_logprobs:
        cmd_args += f" --max-logprobs {max_logprobs}"

    disable_log_stats = env.get("CM_VLLM_SERVER_DISABLE_LOG_STATS", False)
    if disable_log_stats:
        cmd_args += f" --disable-log-stats"

    quantization = env.get("CM_VLLM_SERVER_QUANTIZATION", False)
    if quantization:
        cmd_args += f" --quantization {quantization}"

    rope_scaling = env.get("CM_VLLM_SERVER_ROPE_SCALING", False)
    if rope_scaling:
        cmd_args += f" --rope-scaling {rope_scaling}"

    rope_theta = env.get("CM_VLLM_SERVER_ROPE_THETA", False)
    if rope_theta:
        cmd_args += f" --rope-theta {rope_theta}"

    enforce_eager = env.get("CM_VLLM_SERVER_ENFORCE_EAGER", False)
    if enforce_eager:
        cmd_args += f" --enforce-eager"

    max_context_len_to_capture = env.get(
        "CM_VLLM_SERVER_MAX_CONTEXT_LEN_TO_CAPTURE", False)
    if max_context_len_to_capture:
        cmd_args += f" --max-context-len-to-capture {max_context_len_to_capture}"

    max_seq_len_to_capture = env.get(
        "CM_VLLM_SERVER_MAX_SEQ_LEN_TO_CAPTURE", False)
    if max_seq_len_to_capture:
        cmd_args += f" --max-seq-len-to-capture {max_seq_len_to_capture}"

    disable_custom_all_reduce = env.get(
        "CM_VLLM_SERVER_DISABLE_CUSTOM_ALL_REDUCE", False)
    if disable_custom_all_reduce:
        cmd_args += f" --disable-custom-all-reduce"

    tokenizer_pool_size = env.get("CM_VLLM_SERVER_TOKENIZER_POOL_SIZE", False)
    if tokenizer_pool_size:
        cmd_args += f" --tokenizer-pool-size {tokenizer_pool_size}"

    tokenizer_pool_type = env.get("CM_VLLM_SERVER_TOKENIZER_POOL_TYPE", False)
    if tokenizer_pool_type:
        cmd_args += f" --tokenizer-pool-type {tokenizer_pool_type}"

    tokenizer_pool_extra_config = env.get(
        "CM_VLLM_SERVER_TOKENIZER_POOL_EXTRA_CONFIG", False)
    if tokenizer_pool_extra_config:
        cmd_args += f" --tokenizer-pool-extra-config {tokenizer_pool_extra_config}"

    enable_lora = env.get("CM_VLLM_SERVER_ENABLE_LORA", False)
    if enable_lora:
        cmd_args += f" --enable-lora"

    max_loras = env.get("CM_VLLM_SERVER_MAX_LORAS", False)
    if max_loras:
        cmd_args += f" --max-loras {max_loras}"

    max_lora_rank = env.get("CM_VLLM_SERVER_MAX_LORA_RANK", False)
    if max_lora_rank:
        cmd_args += f" --max-lora-rank {max_lora_rank}"

    lora_extra_vocab_size = env.get(
        "CM_VLLM_SERVER_LORA_EXTRA_VOCAB_SIZE", False)
    if lora_extra_vocab_size:
        cmd_args += f" --lora-extra-vocab-size {lora_extra_vocab_size}"

    lora_dtype = env.get("CM_VLLM_SERVER_LORA_DTYPE", False)
    if lora_dtype:
        cmd_args += f" --lora-dtype {lora_dtype}"

    long_lora_scaling_factors = env.get(
        "CM_VLLM_SERVER_LONG_LORA_SCALING_FACTORS", False)
    if long_lora_scaling_factors:
        cmd_args += f" --long-lora-scaling-factors {long_lora_scaling_factors}"

    max_cpu_loras = env.get("CM_VLLM_SERVER_MAX_CPU_LORAS", False)
    if max_cpu_loras:
        cmd_args += f" --max-cpu-loras {max_cpu_loras}"

    fully_sharded_loras = env.get("CM_VLLM_SERVER_FULLY_SHARDED_LORAS", False)
    if fully_sharded_loras:
        cmd_args += f" --fully-sharded-loras"

    enable_prompt_adapter = env.get(
        "CM_VLLM_SERVER_ENABLE_PROMPT_ADAPTER", False)
    if enable_prompt_adapter:
        cmd_args += f" --enable-prompt-adapter"

    max_prompt_adapters = env.get("CM_VLLM_SERVER_MAX_PROMPT_ADAPTERS", False)
    if max_prompt_adapters:
        cmd_args += f" --max-prompt-adapters {max_prompt_adapters}"

    max_prompt_adapter_token = env.get(
        "CM_VLLM_SERVER_MAX_PROMPT_ADAPTER_TOKEN", False)
    if max_prompt_adapter_token:
        cmd_args += f" --max-prompt-adapter-token {max_prompt_adapter_token}"

    device = env.get("CM_VLLM_SERVER_DEVICE", False)
    if device:
        cmd_args += f" --device {device}"

    scheduler_delay_factor = env.get(
        "CM_VLLM_SERVER_SCHEDULER_DELAY_FACTOR", False)
    if scheduler_delay_factor:
        cmd_args += f" --scheduler-delay-factor {scheduler_delay_factor}"

    enable_chunked_prefill = env.get(
        "CM_VLLM_SERVER_ENABLE_CHUNKED_PREFILL", False)
    if enable_chunked_prefill:
        cmd_args += f" --enable-chunked-prefill"

    speculative_model = env.get("CM_VLLM_SERVER_SPECULATIVE_MODEL", False)
    if speculative_model:
        cmd_args += f" --speculative-model {speculative_model}"

    num_speculative_tokens = env.get(
        "CM_VLLM_SERVER_NUM_SPECULATIVE_TOKENS", False)
    if num_speculative_tokens:
        cmd_args += f" --num-speculative-tokens {num_speculative_tokens}"

    speculative_draft_tensor_parallel_size = env.get(
        "CM_VLLM_SERVER_SPECULATIVE_DRAFT_TENSOR_PARALLEL_SIZE", False)
    if speculative_draft_tensor_parallel_size:
        cmd_args += f" --speculative-draft-tensor-parallel-size {speculative_draft_tensor_parallel_size}"

    speculative_max_model_len = env.get(
        "CM_VLLM_SERVER_SPECULATIVE_MAX_MODEL_LEN", False)
    if speculative_max_model_len:
        cmd_args += f" --speculative-max-model-len {speculative_max_model_len}"

    speculative_disable_by_batch_size = env.get(
        "CM_VLLM_SERVER_SPECULATIVE_DISABLE_BY_BATCH_SIZE", False)
    if speculative_disable_by_batch_size:
        cmd_args += f" --speculative-disable-by-batch-size {speculative_disable_by_batch_size}"

    ngram_prompt_lookup_max = env.get(
        "CM_VLLM_SERVER_NGRAM_PROMPT_LOOKUP_MAX", False)
    if ngram_prompt_lookup_max:
        cmd_args += f" --ngram-prompt-lookup-max {ngram_prompt_lookup_max}"

    ngram_prompt_lookup_min = env.get(
        "CM_VLLM_SERVER_NGRAM_PROMPT_LOOKUP_MIN", False)
    if ngram_prompt_lookup_min:
        cmd_args += f" --ngram-prompt-lookup-min {ngram_prompt_lookup_min}"

    spec_decoding_acceptance_method = env.get(
        "CM_VLLM_SERVER_SPEC_DECODING_ACCEPTANCE_METHOD", False)
    if spec_decoding_acceptance_method:
        cmd_args += f" --spec-decoding-acceptance-method {spec_decoding_acceptance_method}"

    typical_acceptance_sampler_posterior_threshold = env.get(
        "CM_VLLM_SERVER_TYPICAL_ACCEPTANCE_SAMPLER_POSTERIOR_THRESHOLD", False)
    if typical_acceptance_sampler_posterior_threshold:
        cmd_args += f" --typical-acceptance-sampler-posterior-threshold {typical_acceptance_sampler_posterior_threshold}"

    typical_acceptance_sampler_posterior_alpha = env.get(
        "CM_VLLM_SERVER_TYPICAL_ACCEPTANCE_SAMPLER_POSTERIOR_ALPHA", False)
    if typical_acceptance_sampler_posterior_alpha:
        cmd_args += f" --typical-acceptance-sampler-posterior-alpha {typical_acceptance_sampler_posterior_alpha}"

    model_loader_extra_config = env.get(
        "CM_VLLM_SERVER_MODEL_LOADER_EXTRA_CONFIG", False)
    if model_loader_extra_config:
        cmd_args += f" --model-loader-extra-config {model_loader_extra_config}"

    preemption_mode = env.get("CM_VLLM_SERVER_PREEMPTION_MODE", False)
    if preemption_mode:
        cmd_args += f" --preemption-mode {preemption_mode}"

    served_model_name = env.get("CM_VLLM_SERVER_SERVED_MODEL_NAME", False)
    if served_model_name:
        cmd_args += f" --served-model-name {served_model_name}"

    qlora_adapter_name_or_path = env.get(
        "CM_VLLM_SERVER_QLORA_ADAPTER_NAME_OR_PATH", False)
    if qlora_adapter_name_or_path:
        cmd_args += f" --qlora-adapter-name-or-path {qlora_adapter_name_or_path}"

    otlp_traces_endpoint = env.get(
        "CM_VLLM_SERVER_OTLP_TRACES_ENDPOINT", False)
    if otlp_traces_endpoint:
        cmd_args += f" --otlp-traces-endpoint {otlp_traces_endpoint}"

    engine_use_ray = env.get("CM_VLLM_SERVER_ENGINE_USE_RAY", False)
    if engine_use_ray:
        cmd_args += f" --engine-use-ray"

    disable_log_requests = env.get(
        "CM_VLLM_SERVER_DISABLE_LOG_REQUESTS", False)
    if disable_log_requests:
        cmd_args += f" --disable-log-requests"

    max_log_len = env.get("CM_VLLM_SERVER_MAX_LOG_LEN", False)
    if max_log_len:
        cmd_args += f" --max-log-len {max_log_len}"

    cmd = f"{env['CM_PYTHON_BIN_WITH_PATH']} -m vllm.entrypoints.openai.api_server {cmd_args}"
    print(cmd)

    env['CM_VLLM_RUN_CMD'] = cmd

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
