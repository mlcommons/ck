cmx update flex.cfg mlperf --meta.storage_for_raw_results="/persistent_storage/mlperf-raw-results"

flextask "get mlperf results" --benchmark=inference --version=scc24-live --url=https://github.com/mlcommons/cm4mlperf-inference --branch=mlperf-inference-results-scc24 --extra_cache_meta.live --extra_cache_tags=live --submission --j

flextask "get mlperf results" --benchmark=inference --version=4.1 --s
flextask "get mlperf results" --benchmark=inference --version=4.0 --s
flextask "get mlperf results" --benchmark=inference --version=3.1 --s
# flextask "get mlperf results" --benchmark=inference --version=3.1 --s --depth=1 --renew --v
