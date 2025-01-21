#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

if [ -z "$max_process_num" ]; then
  printf "\033[0;31m<--max_process_num> is not specified. Please specify it using --max_process_num=[nthreads]\033[0m\n"
  exit 1
fi
echo "Max number of processes: ${max_process_num}"

echo "Changing to G10 repo: ${CM_GIT_REPO_G10_CHECKOUT_PATH}"
cd "${CM_GIT_REPO_G10_CHECKOUT_PATH}"

cd src
make clean
make -j"$(nproc)"

cd resources
${CM_PYTHON_BIN_WITH_PATH} genconfigs.py

tmux kill-server > /dev/null 2> /dev/null

# First run experiments for figure 11-14
./run.sh -p "(BERT\/256|VIT\/1280|Inceptionv3\/1536|ResNet152\/1280|SENet154\/1024)-sim_(deepUM|prefetch_lru|FlashNeuron|G10GDSSSD|G10GDSFULL|lru)\.config" -dr -j $max_process_num
# The time for running this is about 104m33.975s (for max_process_num=6)

# Then run experiments for figure 15
./run.sh -p "(BERT\/(128|256|512|768|1024)|VIT\/(256|512|768|1024|1280)|Inceptionv3\/(512|768|1024|1280|1536|1792)|ResNet152\/(256|512|768|1024|1280)|SENet154\/(256|512|768|1024))-sim_(deepUM|prefetch_lru|FlashNeuron|lru)\.config" -dr -j $max_process_num
# The time for running this is about 155m11.104s (for max_process_num=6)

# Then run experiments for figure 16
./run.sh -p "(BERT\/(256|384|512|640)|VIT\/(768|1024|1280|1536)|Inceptionv3\/(512|1024|1280|1536)|ResNet152\/(768|1024|1280|1536)|SENet154\/(256|512|768|1024))-sim_prefetch_lru(-cpu(0|16|32|64|96|192|256))?\.config" -dr -j $max_process_num
# The time for running this is about 406m30.954s (for max_process_num=6)

# Then run experiments for figure 17
./run.sh -p "(VIT\/1024|Inceptionv3\/1280)-sim_(deepUM|prefetch_lru|FlashNeuron)-cpu(0|16|32|64|256)\.config" -dr -j $max_process_num
# The time for running this is about 24m8.144s (for max_process_num=6)

# Then run experiments for figure 18
./run.sh -p "(BERT\/512|VIT\/1280|Inceptionv3\/1536|ResNet152\/1280|SENet154\/1024)-sim_(deepUM|prefetch_lru|FlashNeuron|lru)-ssd(6_4|12_8|19_2|25_6|32)-.*\.config" -dr -j $max_process_num
# The time for running this is about 354m40.747s (for max_process_num=6)

# Then run experiments for figure 19
./run.sh -p "(BERT\/256|VIT\/1280|Inceptionv3\/1536|ResNet152\/1280|SENet154\/1024)-sim_prefetch_lru-var0_(05|10|15|20|25)\.config" -dr -j $max_process_num
# The time for running this is about 124m17.909s (for max_process_num=6)]
