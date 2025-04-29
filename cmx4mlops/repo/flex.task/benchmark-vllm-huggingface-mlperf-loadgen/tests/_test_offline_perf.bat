cmx update flex.cfg huggingface --meta.env.hf_home="/mnt/common/gfursin"
ft "benchmark vllm huggingface mlperf loadgen" --compute_tags=cuda,nvcc --model_path=deepseek-ai/DeepSeek-R1-Distill-Llama-8B --dataset_path=Open-Orca/OpenOrca --dataset_split=train --total_sample_count=500 --scenario=Offline --target_qps=10 --api_server="http://localhost:8008" --v
