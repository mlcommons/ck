# MLPerf Inference Accuracy Log Truncator
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) runs the [MLPerf Inference accuracy log truncator](https://github.com/mlcommons/inference/blob/master/tools/submission/truncate_accuracy_log.py) on a given submission folder.

## How To
```bash
cm run script --tags=run,mlperf,inference,accuracy,truncator --submitter=[SUBMITTER_NAME] --submission_dir=[SUBMISSION_FOLDER]
```
