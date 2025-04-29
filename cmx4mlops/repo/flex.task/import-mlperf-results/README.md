# Flow

* This script calls flex.task "run-mlperf-submission-checker" to create CSV file with MLPerf results.
  * The subtask is calling flex.task "process-mlperf-csv-results" to convert CSV file into the CMX JSON format
* Next, it calls flex.common automation "summarize_keys" to create summary.json in the CMX format
* Finally, it creates flex.experiment for further analysis and visualization via FlexBoard
