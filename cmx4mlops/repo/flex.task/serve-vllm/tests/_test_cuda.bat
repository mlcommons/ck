cmx update flex.cfg huggingface --meta.env.hf_home="/mnt/common"
ft "serve vllm" --compute=cuda,nvcc --env.CUDA_VISIBLE_DEVICE=0 --state.flow.set_hf_home.path=/mnt/common --state.flow.pip_vllm.version=0.7.3 --state.flow.pip_torch.version=2.5.1 --state.flow.pip_torch_vision.version=0.20.1 --model_path=deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --v --output_state -save_to_json_file=output.json
