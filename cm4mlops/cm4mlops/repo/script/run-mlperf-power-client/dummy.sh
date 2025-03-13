#!/usr/bin/env bash

mkdir -p loadgen_logs

# Create mock files with the same names that loadgen does

echo power_begin $(date --utc +"%m-%d-%Y %T.%3N") | tee loadgen_logs/mlperf_log_detail.txt
touch loadgen_logs/mlperf_log_accuracy.json
touch loadgen_logs/mlperf_log_summary.txt
touch loadgen_logs/mlperf_log_trace.json
sleep 25
echo power_end $(date --utc +"%m-%d-%Y %T.%3N") | tee -a loadgen_logs/mlperf_log_detail.txt
