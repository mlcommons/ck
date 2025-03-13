cd ${CM_HARNESS_CODE_ROOT}

cd utils
cmd=" python -m pip install ."

echo "$cmd"
eval "$cmd"
test "$?" -eq 0 || exit "$?"

cd ../tools
wget https://raw.githubusercontent.com/mlcommons/inference/master/text_to_image/tools/coco.py
test "$?" -eq 0 || exit "$?"
cd ..

mkdir -p coco2014/captions
wget -P coco2014/captions/ https://raw.githubusercontent.com/mlcommons/inference/master/text_to_image/coco2014/captions/captions_source.tsv
test "$?" -eq 0 || exit "$?"

mkdir -p coco2014/latents
wget -P coco2014/latents/ https://github.com/mlcommons/inference/raw/master/text_to_image/tools/latents.pt
test "$?" -eq 0 || exit "$?"

cd tools/
bash download-coco-2014-calibration.sh --download-path ${PWD}/../coco2014/warmup_dataset --num-workers 1
test "$?" -eq 0 || exit "$?"
cd ..

