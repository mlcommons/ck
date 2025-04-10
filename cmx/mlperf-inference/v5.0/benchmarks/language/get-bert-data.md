---
hide:
  - toc
---

# Question Answering using Bert-Large

## Dataset

The benchmark implementation run command will automatically download the validation and calibration datasets and do the necessary preprocessing. In case you want to download only the datasets, you can use the below commands.

=== "Validation"
    BERT validation run uses the SQuAD v1.1 dataset.

    ### Get Validation Dataset
    ```
    pip install cmx4mlperf
    cr get,dataset,squad,validation -j
    ```

## Model
The benchmark implementation run command will automatically download the required model and do the necessary conversions. In case you want to only download the official model, you can use the below commands.

Get the Official MLPerf Bert-Large Model

=== "Pytorch"

    ### Pytorch
    ```
    pip install cmx4mlperf
    cr get,ml-model,bert-large,_pytorch -j
    ```
=== "Onnx"

    ### Onnx
    ```
    pip install cmx4mlperf
    cr get,ml-model,bert-large,_onnx -j
    ```
=== "Tensorflow"

    ### Tensorflow
    ```
    pip install cmx4mlperf
    cr get,ml-model,bert-large,_tensorflow -j
    ```

