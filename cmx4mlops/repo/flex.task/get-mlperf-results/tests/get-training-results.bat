cmx update flex.cfg mlperf --meta.storage_for_raw_results="d:\Work2\!!MLPerf-results"

flextask "get mlperf results" --benchmark=training --version=4.1 --extra_cache_meta.live ^
   --extra_cache_tags=live --submission --url="git@github.com:mlcommons/submissions_training_v4.1" --j
flextask "get mlperf results" --benchmark=training --version=4.0 --j
flextask "get mlperf results" --benchmark=training --version=3.1 --j
flextask "get mlperf results" --benchmark=training --version=3.0 --j
