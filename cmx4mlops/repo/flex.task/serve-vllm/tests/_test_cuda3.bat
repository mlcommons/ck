cmx update flex.cfg huggingface --meta.env.hf_home="/mnt/common/gfursin"
ft "serve vllm" @_test_cuda3.yaml 
#--compute=cuda,nvcc --env.CUDA_VISIBLE_DEVICES=4 --state.flow.pip_vllm.version=0.7.2 --state.flow.pip_torch.version=2.5.1 --state.flow.pip_torch_vision.version=0.20.1 --model_path=deepseek-ai/DeepSeek-R1-Distill-Llama-8B --port=8008 --v