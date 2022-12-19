# Run MLPerf Inference Submission Checker
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) runs the [MLPerf Inference submission checker](https://github.com/mlcommons/inference/blob/master/tools/submission/submission-checker.py) on a given submission folder.

## How To
```bash
cm run script --tags=run,mlperf,inference,submission,checker --submitter=[SUBMITTER_NAME] --submission_dir=[SUBMISSION_FOLDER]
```

### Additional Options
* `[--skip_compliance]:` Skips the compliance tests
