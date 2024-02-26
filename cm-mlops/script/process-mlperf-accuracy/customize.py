from cmind import utils
import cmind as cm
import os

def preprocess(i):

    os_info = i['os_info']

    xsep = ';' if os_info['platform'] == 'windows' else ':'
    
    env = i['env']
    results_dir = env.get("CM_MLPERF_ACCURACY_RESULTS_DIR", "")

    if results_dir == "":
        print("Please set CM_MLPERF_ACCURACY_RESULTS_DIR")
        return {'return':-1}

    # In fact, we expect only 1 command line here
    run_cmds = []

    if env.get('CM_MAX_EXAMPLES', '') != '' and env.get('CM_MLPERF_RUN_STYLE', '') != 'valid':
        max_examples_string = " --max_examples " + env['CM_MAX_EXAMPLES']
    else:
        max_examples_string = ""

    results_dir_split = results_dir.split(xsep)
    dataset = env['CM_DATASET']
    regenerate_accuracy_file = env.get('CM_MLPERF_REGENERATE_ACCURACY_FILE', False)

    for result_dir in results_dir_split:

        out_file = os.path.join(result_dir, 'accuracy.txt')

        if os.path.exists(out_file) and (os.stat(out_file).st_size != 0) and not regenerate_accuracy_file:
            continue

        if dataset == "openimages":
            if env.get('CM_DATASET_PATH_ROOT', '') != '':
                dataset_dir = env['CM_DATASET_PATH_ROOT']
                if 'DATASET_ANNOTATIONS_FILE_PATH' in env:
                    del(env['DATASET_ANNOTATIONS_FILE_PATH'])
            else:
                env['DATASET_ANNOTATIONS_FILE_PATH'] = env['CM_DATASET_ANNOTATIONS_FILE_PATH']
                dataset_dir = os.getcwd() # not used, just to keep the script happy
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " "+"'" + os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools", \
                "accuracy-openimages.py") + "'"+" --mlperf-accuracy-file "+"'" + os.path.join(result_dir, \
                    "mlperf_log_accuracy.json") + "'"+" --openimages-dir "+"'" + dataset_dir + "'"+" --verbose > "+"'" + \
                out_file + "'"

        elif dataset == "imagenet":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools",
                "accuracy-imagenet.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir,
                    "mlperf_log_accuracy.json") + "' --imagenet-val-file '" + os.path.join(env['CM_DATASET_AUX_PATH'],
                            "val.txt") + "' --dtype " + env.get('CM_ACCURACY_DTYPE', "float32") +  " > '" + out_file + "'"

        elif dataset == "squad":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_BERT_PATH'],
                "accuracy-squad.py") + "' --val_data '" + env['CM_DATASET_SQUAD_VAL_PATH'] + \
                "' --log_file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --vocab_file '" + env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH'] + \
                "' --out_file '" + os.path.join(result_dir, 'predictions.json') + \
                "' --features_cache_file '" + os.path.join(env['CM_MLPERF_INFERENCE_BERT_PATH'], 'eval_features.pickle') + \
                "' --output_dtype " + env['CM_ACCURACY_DTYPE'] + env.get('CM_OUTPUT_TRANSPOSED','') + max_examples_string + " > '" + out_file + "'"

        elif dataset == "cnndm":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "language", "gpt-j",
                "evaluation.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --dataset-file '" + env['CM_DATASET_EVAL_PATH'] + "'"+ " --dtype " + env.get('CM_ACCURACY_DTYPE', "float32")  +" > '" + out_file + "'"

        elif dataset == "openorca":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "language", "llama2-70b",
                "evaluate-accuracy.py") + "' --checkpoint-path '" + env['CM_ML_MODEL_LLAMA2_FILE_WITH_PATH'] + "' --mlperf-accuracy-file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --dataset-file '" + env['CM_DATASET_PREPROCESSED_PATH'] + "'"+ " --dtype " + env.get('CM_ACCURACY_DTYPE', "int32")  +" > '" + out_file + "'"


        elif dataset == "coco2014":
            env['+PYTHONPATH'] = [ os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "text_to_image", "tools") ]
            #env['DATASET_ANNOTATIONS_FILE_PATH'] = env['CM_DATASET_ANNOTATIONS_FILE_PATH']
            CMD =  env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "text_to_image", "tools",
                "accuracy_coco.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --caption-path '" + os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "text_to_image", "coco2014", "captions", "captions_source.tsv") + "' > '" + out_file + "'"

        elif dataset == "kits19":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_3DUNET_PATH'],
                "accuracy_kits.py") + \
                "' --preprocessed_data_dir '" + env['CM_DATASET_PREPROCESSED_PATH'] +\
                "' --postprocessed_data_dir '" + result_dir +\
                "' --log_file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --output_dtype " + env['CM_ACCURACY_DTYPE'] +" > '" + out_file + "'"

        elif dataset == "librispeech":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_RNNT_PATH'],
                "accuracy_eval.py") + \
                "' --dataset_dir '" + os.path.join(env['CM_DATASET_PREPROCESSED_PATH'], "..") +\
                "' --manifest '" + env['CM_DATASET_PREPROCESSED_JSON'] +\
                "' --log_dir '" + result_dir + \
                "' --output_dtype " + env['CM_ACCURACY_DTYPE'] +" > '" + out_file + "'"

        elif dataset == "terabyte":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_DLRM_PATH'], "tools",
                "accuracy-dlrm.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir,
                    "mlperf_log_accuracy.json") + \
                    "' --dtype " + env.get('CM_ACCURACY_DTYPE', "float32") +  " > '" + out_file + "'"

        else:
            return {'return': 1, 'error': 'Unsupported dataset'}

        outfile = os.path.join(result_dir, "accuracy.txt")
        if not os.path.exists(outfile) or (os.stat(outfile).st_size == 0) or env.get("CM_REGENERATE_MEASURE_FILES", False):
            run_cmds.append(CMD)


    if os_info['platform'] == 'windows':
        env['CM_RUN_CMDS'] = ('\n'.join(run_cmds)).replace("'", '"').replace('>','^>')
    else:
        env['CM_RUN_CMDS'] = "??".join(run_cmds)

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']

    xsep = ';' if os_info['platform'] == 'windows' else ':'

    results_dir = env.get("CM_MLPERF_ACCURACY_RESULTS_DIR", "")
    
    results_dir_split = results_dir.split(xsep)

    for result_dir in results_dir_split:
        accuracy_file = os.path.join(result_dir, "accuracy.txt")

        if os.path.exists(accuracy_file):
            print ('')
            print ('Accuracy file: {}'.format(accuracy_file))
            print ('')

            x = ''
            with open(accuracy_file, "r") as fp:
                x=fp.read()

            if x!='':
                print(x)

                # Trying to extract accuracy dict
                for y in x.split('\n'):
                    if y.startswith('{') and y.endswith('}'):

                        import json

                        try:
                           z=json.loads(y)
                           state['app_mlperf_inference_accuracy']=z

                           break
                        except ValueError as e:
                           pass

            print ('')
    return {'return':0}

