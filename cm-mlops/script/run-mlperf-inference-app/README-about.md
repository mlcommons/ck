This portable CM (CK2) script provides a unified and portable interface to the MLPerf inference benchmark 
modularized by other [portable CM scripts](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md)
being developed by the open [MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md).

It is a higher-level wrapper that automatically generates the command line for the [universal MLPerf inference script](../app-mlperf-inference)
to run MLPerf scenarios for a given ML task, model, runtime and device, and prepare and validate submissions.

Check these [tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md) from the Student Cluster Competition
at Supercomputing'22 to understand how to use this script to run the MLPerf inference benchmark and automate submissions.
