rm runtime_ignore_dequant_check.patch
wget -nc https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/retinanet/pytorch-cpu/runtime_ignore_dequant_check.patch
test $? -eq 0 || exit $?
git apply runtime_ignore_dequant_check.patch
test $? -eq 0 || exit $?
