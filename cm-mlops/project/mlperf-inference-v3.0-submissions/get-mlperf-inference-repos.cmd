cm run script "get git repo _repo.https://github.com/ctuning/mlperf_inference_submissions_v3.0" --extra_cache_tags=mlperf-inference-results,version-3.0
cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v2.1" --env.CM_GIT_CHECKOUT=master --extra_cache_tags=mlperf-inference-results,version-2.1
cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v2.0" --env.CM_GIT_CHECKOUT=master --extra_cache_tags=mlperf-inference-results,version-2.0
