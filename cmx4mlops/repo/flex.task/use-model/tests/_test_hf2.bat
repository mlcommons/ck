cmx update flex.cfg mlperf --meta.storage_for_models="d:\Work2\!!MLPerf-artifacts"
ft "use model" --model_tags=generic,hf --repo= --j --v --env.TEST=ABC

rem cmx run . --path="D:\Work2\!!MLPerf-artifacts" --j --renew
