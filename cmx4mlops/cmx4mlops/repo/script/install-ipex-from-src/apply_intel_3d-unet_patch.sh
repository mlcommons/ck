rm -rf unet3d.patch
wget -nc https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/3d-unet-99/pytorch-cpu/unet3d.patch
test $? -eq 0 || exit $?
git apply unet3d.patch
test $? -eq 0 || exit $?
