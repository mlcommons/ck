# Generate MLPerf Inference Submission Folder
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) takes in a MLPerf Inference results folder (same folder structure assumed as produced by MLPerf inference reference implementation) and produces a valid submission folder as required by the [MLPerf Inference submission checker](https://github.com/mlcommons/inference/blob/master/tools/submission/submission-checker.py).

## How To
```bash
cm run script --tags=generate,mlperf-inference-submission --results_dir=[MLPERF_RESULT_DIR] --submission_dir=[SUBMISSION_FOLDER]
```

### Additional Options
* `[--run_checker]:` Runs the MLPerf Inference submission checker on the produced submission folder
* `[--skip_truncation]:` If on will not run the truncation of the accuracy logs (useful for testing)
* `[--run_style]:` If set to "valid" will indicate the result folder is from a full and valid MLPerf inference run and will trigget the accuracy truncation script unless `--skip_truncation` flag is set.
