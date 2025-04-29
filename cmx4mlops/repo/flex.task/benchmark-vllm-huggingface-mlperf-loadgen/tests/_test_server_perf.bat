cmx update flex.cfg huggingface --meta.env.hf_home="/mnt/common/gfursin"
time ft "benchmark vllm huggingface mlperf loadgen" --compute_tags=cuda,nvcc --model_path=deepseek-ai/DeepSeek-R1-Distill-Llama-8B --dataset_path=Open-Orca/OpenOrca --dataset_split=train --total_sample_count=2 --scenario=Server --target_qps=2 --api_server="http://localhost:8008" --v
