cmx update flex.cfg huggingface --meta.env.hf_home="/mnt/common/gfursin"
ft "run mlperf submission checker" --path=$PWD/mlperf-inference-5.0-flexai-final --benchmark=inference --version=5.0 --extra_flags=--skip-extra-files-in-root-check --truncate_accuracy_log --submitter=FlexAI

