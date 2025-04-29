cmx update flex.cfg mlperf --meta.storage_for_models="d:\Work2\!!MLPerf-artifacts"
ft "use model" --model_tags=generic,hf --j --v --repo="regisss/llama2-70b-fused-qkv-mlperf"  --directory=data --renew --connect

rem cmx run . --path="D:\Work2\!!MLPerf-artifacts" --j --renew
