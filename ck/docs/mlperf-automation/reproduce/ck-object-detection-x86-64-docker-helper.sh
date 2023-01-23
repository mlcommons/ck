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

ck benchmark program:object-detection-tflite-loadgen \
     --env.CK_SILENT_MODE=YES \
     --skip_print_timers \
     --dep_add_tags.compiler=gcc \
     --dep_add_tags.python=v3 \
     --dep_add_tags.mlperf-inference-src=r1.0 \
     --dep_add_tags.weights=ssd-mobilenet \
     --dep_add_tags.dataset=dataset,object-detection,preprocessed,full,using-pillow \
     --dep_add_tags.library=tflite,v2.4.1,with.ruy \
     --env.CK_LOADGEN_DATASET_SIZE=50 \
     --env.USE_NMS=regular \
     --env.CK_VERBOSE=1 \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --skip_stat_analysis \
     --process_multi_keys \
     --repetitions=1 \
     --record \
     --record_repo=ck-experiments \
     --record_uoa=mlperf-closed-amd-tflite-v2.4.1-ruy-ssd-mobilenet-non-quantized-singlestream-accuracy-target-latency-20 \
     --tags=mlperf,division.closed,task.object-detection,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.accuracy,workload.ssd-mobilenet-non-quantized,preprocessed_using.pillow,target_latency.20

echo "======================================================================="
cat `ck find program:object-detection-tflite-loadgen`/tmp/accuracy.txt 
echo "======================================================================="
