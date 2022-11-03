{
  "alias": "app-mlperf-inference-reference",
  "automation_alias": "script",
  "automation_uid": "5b4e0237da074764",
  "default_env": {
    "CM_BATCH_COUNT": "1",
    "CM_BATCH_SIZE": "1",
    "CM_LOADGEN_MODE": "accuracy",
    "CM_LOADGEN_SCENARIO": "Offline",
    "CM_OUTPUT_FOLDER_NAME": "test_results",
    "CM_MLPERF_RUN_STYLE": "test",
    "CM_TEST_QUERY_COUNT": "10"
  },
  "deps": [
    {
      "tags": "detect,os"
    },
    {
      "tags": "detect,cpu"
    },
    {
      "tags": "get,sys-utils-cm"
    },
    {
      "names": [
        "python3"
      ],
      "tags": "get,python"
    },
    {
      "names": [
        "loadgen"
      ],
      "tags": "get,loadgen"
    },
    {
      "names": [
        "inference-src"
      ],
      "tags": "get,mlcommons,inference,src"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "onnxruntime",
          "tvm-onnx",
          "tvm-pip-install-onnx"
        ]
      },
      "names": [
        "ml-engine-onnxruntime"
      ],
      "tags": "get,generic-python-lib,_onnxruntime"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "tf",
          "tflite"
        ]
      },
      "names": [
        "ml-engine-tensorflow"
      ],
      "tags": "get,generic-python-lib,_tensorflow"
    },
    {
      "enable_if_env": {
        "CM_MODEL": [
          "resnet50"
        ]
      },
      "names": [
        "imagenet-preprocessed"
      ],
      "tags": "get,dataset,image-classification,imagenet,preprocessed"
    },
    {
      "enable_if_env": {
        "CM_MODEL": [
          "resnet50"
        ]
      },
      "tags": "get,dataset-aux,image-classification,imagenet-aux"
    },
    {
      "enable_if_env": {
        "CM_MODEL": [
          "retinanet"
        ]
      },
      "tags": "get,generic-python-lib,_pycocotools"
    },
    {
      "enable_if_env": {
        "CM_MODEL": [
          "retinanet"
        ]
      },
      "tags": "get,dataset,object-detection,open-images,original"
    },
    {
      "enable_if_env": {
        "CM_MODEL": [
          "bert-99.9"
        ]
      },
      "tags": "get,dataset,squad,original"
    },
    {
      "enable_if_env": {
        "CM_MODEL": [
          "bert-99.9"
        ]
      },
      "tags": "get,generic-python-lib,_transformers"
    },
    {
      "enable_if_env": {
        "CM_MODEL": [
          "bert-99.9"
        ]
      },
      "tags": "get,generic-python-lib,_tokenization"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "tf",
          "tflite"
        ],
        "CM_MODEL": [
          "resnet50"
        ]
      },
      "tags": "get,ml-model,image-classification,resnet50,_tensorflow"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "pytorch"
        ],
        "CM_MODEL": [
          "resnet50"
        ]
      },
      "tags": "get,ml-model,image-classification,resnet50,_pytorch"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "onnxruntime",
          "tvm-onnx"
        ],
        "CM_MODEL": [
          "resnet50"
        ]
      },
      "tags": "get,ml-model,image-classification,resnet50,_onnx"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "onnxruntime"
        ],
        "CM_MODEL": [
          "bert-99.9"
        ]
      },
      "tags": "get,ml-model,language-processing,bert,_onnx"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "pytorch"
        ],
        "CM_MODEL": [
          "retinanet"
        ]
      },
      "tags": "get,ml-model,object-detection,resnext50,fp32,_pytorch"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "onnxruntime"
        ],
        "CM_MODEL": [
          "retinanet"
        ]
      },
      "tags": "get,ml-model,object-detection,resnext50,fp32,_onnx"
    },
    {
      "enable_if_env": {
        "CM_DEVICE": [
          "gpu"
        ]
      },
      "tags": "get,cuda"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "tvm-onnx"
        ]
      },
      "names": [
        "ml-engine-tvm"
      ],
      "skip_if_env": {
        "CM_TVM_PIP_INSTALL": []
      },
      "tags": "get,tvm,_llvm"
    },
    {
      "enable_if_env": {
        "CM_BACKEND": [
          "pytorch"
        ]
      },
      "names": [
        "ml-engine-pytorch"
      ],
      "tags": "get,generic-python-lib,_torch"
    },
    {
      "tags": "get,sut,configs"
    }
  ],
  "env_key_mappings": {
    "CM_HOST_": "HOST_",
    "CM_ML_": "ML_"
  },
  "input_mapping": {
    "count": "CM_LOADGEN_QUERY_COUNT",
    "docker": "CM_RUN_DOCKER_CONTAINER",
    "hw_name": "CM_HW_NAME",
    "imagenet_path": "IMAGENET_PATH",
    "max_batchsize": "CM_LOADGEN_MAX_BATCHSIZE",
    "mode": "CM_LOADGEN_MODE",
    "num_threads": "CM_NUM_THREADS",
    "output_dir": "OUTPUT_BASE_DIR",
    "power": "CM_SYSTEM_POWER",
    "regenerate_files": "CM_REGENERATE_MEASURE_FILES",
    "rerun": "CM_RERUN",
    "scenario": "CM_LOADGEN_SCENARIO",
    "test_query_count": "CM_TEST_QUERY_COUNT"
  },
  "tags": [
    "app",
    "vision",
    "language",
    "mlcommons",
    "mlperf",
    "inference",
    "reference",
    "generic",
    "ref"
  ],
  "uid": "d775cac873ee4231",
  "variations": {
    "bert-99.9": {
      "env": {
        "CM_MODEL": "bert-99.9"
      },
      "post_deps": [
        {
          "enable_if_env": {
            "CM_LOADGEN_MODE": [
              "accuracy",
              "all"
            ],
            "CM_MLPERF_ACCURACY_RESULTS_DIR": [
              "on"
            ]
          },
          "names": [
            "squad-accuracy-script",
            "mlperf-accuracy-script"
          ],
          "tags": "run,accuracy,mlperf,_squad,_float32"
        }
      ]
    },
    "cpp": {
      "add_deps_recursive": {
        "imagenet-accuracy-script": {
          "tags": "_int64"
        }
      },
      "env": {
        "CM_MLPERF_CPP": "yes"
      },
      "posthook_deps": [
        {
          "tags": "app,mlperf,cpp,inference"
        }
      ]
    },
    "cpu": {
      "env": {
        "CM_DEVICE": "cpu"
      }
    },
    "fast": {
      "env": {
        "CM_FAST_FACTOR": "5",
        "CM_OUTPUT_FOLDER_NAME": "fast_results",
        "CM_MLPERF_RUN_STYLE": "fast"
      }
    },
    "gpu": {
      "env": {
        "CM_DEVICE": "gpu"
      }
    },
    "onnxruntime": {
      "add_deps_recursive": {
        "imagenet-preprocessed": {
          "tags": "_NCHW"
        }
      },
      "env": {
        "CM_BACKEND": "onnxruntime",
        "CM_BACKEND_VERSION": "<<<CM_ONNXRUNTIME_VERSION>>>"
      }
    },
    "python": {
      "add_deps_recursive": {
        "imagenet-accuracy-script": {
          "tags": "_float32"
        }
      },
      "env": {
        "CM_MLPERF_PYTHON": "yes"
      }
    },
    "pytorch": {
      "env": {
        "CM_BACKEND": "pytorch",
        "CM_BACKEND_VERSION": "<<<CM_PYTORCH_VERSION>>>"
      }
    },
    "r2.1_default": {
      "add_deps_recursive": {
        "compiler": {
          "tags": "llvm"
        },
        "inference-src": {
          "tags": "_octoml"
        },
        "loadgen": {
          "version": "r2.1"
        }
      },
      "env": {
        "CM_RERUN": "yes",
        "CM_SKIP_SYS_UTILS": "yes",
        "CM_TEST_QUERY_COUNT": "100"
      }
    },
    "resnet50": {
      "env": {
        "CM_MODEL": "resnet50"
      },
      "post_deps": [
        {
          "enable_if_env": {
            "CM_LOADGEN_MODE": [
              "accuracy",
              "all"
            ],
            "CM_MLPERF_ACCURACY_RESULTS_DIR": [
              "on"
            ]
          },
          "names": [
            "mlperf-accuracy-script",
            "imagenet-accuracy-script"
          ],
          "tags": "run,accuracy,mlperf,_imagenet"
        }
      ]
    },
    "retinanet": {
      "env": {
        "CM_MODEL": "retinanet"
      },
      "post_deps": [
        {
          "enable_if_env": {
            "CM_LOADGEN_MODE": [
              "accuracy",
              "all"
            ],
            "CM_MLPERF_ACCURACY_RESULTS_DIR": [
              "on"
            ]
          },
          "names": [
            "mlperf-accuracy-script",
            "openimages-accuracy-script"
          ],
          "tags": "run,accuracy,mlperf,_openimages"
        }
      ]
    },
    "test": {
      "env": {
        "CM_OUTPUT_FOLDER_NAME": "test_results",
        "CM_MLPERF_RUN_STYLE": "test"
      }
    },
    "tf": {
      "add_deps_recursive": {
        "imagenet-preprocessed": {
          "tags": "_NHWC"
        }
      },
      "env": {
        "CM_BACKEND": "tf",
        "CM_BACKEND_VERSION": "<<<CM_TENSORFLOW_VERSION>>>"
      }
    },
    "tflite": {
      "env": {
        "CM_BACKEND": "tflite"
      }
    },
    "tvm-onnx": {
      "env": {
        "CM_BACKEND": "tvm-onnx",
        "CM_BACKEND_VERSION": "<<<CM_ONNXRUNTIME_VERSION>>>"
      }
    },
    "tvm-pip-install-onnx": {
      "deps": [
        {
          "names": [
            "tvm",
            "ml-engine-tvm"
          ],
          "tags": "get,generic-python-lib,_apache-tvm"
        }
      ],
      "env": {
        "CM_BACKEND": "tvm",
        "CM_TVM_PIP_INSTALL": true
      }
    },
    "valid": {
      "env": {
        "CM_OUTPUT_FOLDER_NAME": "valid_results",
        "CM_MLPERF_RUN_STYLE": "valid"
      }
    }
  }
}
