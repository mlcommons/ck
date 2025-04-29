cmx update flex.cfg huggingface --meta.env.hf_home="/mnt/common"
ft "serve vllm" --compute=generic,cpu --state.flow.pip_torch.version=2.5.1 --state.flow.pip_torch_vision.version=0.20.1 --model_path=deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --v --output_state -save_to_json_file=output.json
