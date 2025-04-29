cmx update flex.cfg mlperf --meta.storage_for_models="d:\Work2\!!MLPerf-artifacts"
ft "use model" --model_tags=generic,hf --j --v --repo="ChufanSuki/LeNet5" --directory=data --renew

rem cmx run . --path="D:\Work2\!!MLPerf-artifacts" --j --renew
