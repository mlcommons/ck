#!/bin/bash
cd ${CM_MLPERF_TRAINING_SOURCE}/recommendation_v2_torchrec_dlrm/
${CM_PYTHON_BIN_WITH_PATH} materialize_synthetic_multihot_dataset.py \
    --in_memory_binary_criteo_path $PREPROCESSED_CRITEO_1TB_CLICK_LOGS_DATASET_PATH \
    --output_path $MATERIALIZED_DATASET_PATH \
    --num_embeddings_per_feature 40000000,39060,17295,7424,20265,3,7122,1543,63,40000000,3067956,405282,10,2209,11938,155,4,976,14,40000000,40000000,40000000,590152,12973,108,36 \
    --multi_hot_sizes 3,2,1,2,6,1,1,1,1,7,3,8,1,6,9,5,1,1,1,12,100,27,10,3,1,1 \
    --multi_hot_distribution_type uniform
test $? -eq 0 || exit $?
