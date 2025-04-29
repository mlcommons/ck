cmx update flex.cfg mlperf --meta.storage_for_raw_results=""

flextask "get mlperf results" --benchmark=inference --version=scc24-live --url=https://github.com/mlcommons/cm4mlperf-inference --branch=mlperf-inference-results-scc24 --extra_cache_meta.live --extra_cache_tags=live --submission --j
