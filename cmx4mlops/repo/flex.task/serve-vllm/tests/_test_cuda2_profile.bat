cmx update flex.cfg huggingface --meta.env.hf_home="/mnt/common"
ft "serve vllm" --use_gpus=2 --compute=cuda,nvcc --env.CUDA_VISIBLE_DEVICES=0 --state.flow.pip_vllm.version=0.7.2 --state.flow.pip_torch.version=2.5.1 --state.flow.pip_torch_vision.version=0.20.1 --model_path=deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --max_model_len=1024 --port=8000 --v --profile
