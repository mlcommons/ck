cmx update flex.cfg huggingface --meta.env.hf_home="/mnt/common/gfursin"
ft "run mlperf inference benchmark" @_test2.yaml --dataset=$PWD/open_orca_gpt4_tokenized_llama.sampled_24576.pkl.gz
#open_orca_gpt4_tokenized_llama.sampled_24576.pkl.gz
