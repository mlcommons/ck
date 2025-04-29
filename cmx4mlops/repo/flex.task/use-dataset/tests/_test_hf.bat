cmx update flex.cfg mlperf --meta.storage_for_datasets="d:\Work2\!!MLPerf-artifacts"
ft "use dataset" --dataset_tags=generic,hf --j --v --repo="regisss/scrolls_gov_report_preprocessed_mlperf_2" --directory=data

rem cmx run . --path="D:\Work2\!!MLPerf-artifacts" --j --renew
