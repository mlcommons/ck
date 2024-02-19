[ [Back to MLPerf inference benchmarks index](../README.md) ]

# MLPerf inference benchmark

## Text summarization with Llama2-70b

### Notes

Llama2-70b has two variants - `llama2-70b-99` and `llama2-70b-99.9` where the `99` and `99.9` specify the required accuracy constraint 
with respect to the reference fp32 model. Llama2-70b applies only to datacenter category and includes both Offline and Server scenarios.

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.

### Run using the [MLCommons CM framework](https://github.com/mlcommons/ck)

*From Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*

### A few ready-to-use CM commands

Install MLCommons CM automation framework with automation recipes for MLPerf as described [here](../../../installation.md).

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons Reference implementation in Python](README_reference.md)

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
