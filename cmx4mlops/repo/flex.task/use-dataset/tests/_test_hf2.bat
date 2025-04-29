cmx update flex.cfg mlperf --meta.storage_for_datasets="d:\Work2\!!MLPerf-artifacts"
ft "use dataset" --dataset_tags=generic,hf --j --v --env.TEST=ABC

rem cmx run . --path="D:\Work2\!!MLPerf-artifacts" --j --renew
