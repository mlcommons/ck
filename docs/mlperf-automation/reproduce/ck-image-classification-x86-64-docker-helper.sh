echo "======================================================================="
echo "Fixing access to datasets and ck-experiments ..."
echo ""
time sudo chmod -R 777 datasets
time sudo chmod -R 777 ck-experiments

echo "====================================================================="
echo "Adding external ck-experiments repository ..."
echo ""

ck add repo:ck-experiments --path=/home/ckuser/ck-experiments --quiet

ck ls repo

pwd

ls

ck install package --tags=model,tflite,resnet50,no-argmax 

ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_DATASET_SIZE=500 \
     --dep_add_tags.weights=resnet50 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --record \
     --record_repo=local \
     --record_uoa=mlperf-closed-image-classification-amd-tflite-v2.4.1-ruy-resnet-50-singlestream-performance-target-latency-75 \
     --tags=mlperf,division.closed,task.image-classification,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.performance,workload \
     --print_files=accuracy.txt
