rm input_output_aligned_scales.patch
wget -nc https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/resnet50/pytorch-cpu/input_output_aligned_scales.patch
test $? -eq 0 || exit $?
git apply input_output_aligned_scales.patch
test $? -eq 0 || exit $?
