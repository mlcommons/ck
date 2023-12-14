from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_DATASET_SQUAD_CALIBRATION_SET', '') == "one":
        env['DATASET_CALIBRATION_FILE'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], 'calibration', 'SQuAD-v1.1', 'bert_calibration_features.txt')
        env['DATASET_CALIBRATION_ID'] = 1
    elif env.get('CM_DATASET_SQUAD_CALIBRATION_SET', '') == "two":
        env['DATASET_CALIBRATION_FILE'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], 'calibration', 'SQuAD-v1.1', 'bert_calibration_qas_ids.txt')
        env['DATASET_CALIBRATION_ID'] = 2
    else:
        env['DATASET_CALIBRATION_FILE'] = "''"
        env['DATASET_CALIBRATION_ID'] = 0

    env['CK_ENV_MLPERF_INFERENCE'] = env['CM_MLPERF_INFERENCE_SOURCE']

    if env.get('CM_DATASET_SQUAD_PACKED', '') == "yes":
        i['run_script_input']['script_name'] = "run-packed"
        if env.get('+PYTHONPATH', '') == '':
            env['+PYTHONPATH'] = []

    env['+PYTHONPATH'].append(env['CM_MLPERF_INFERENCE_BERT_PATH'])

    return {'return':0}

def postprocess(i):

    env = i['env']
    cur = os.getcwd()

    if env.get('CM_DATASET_SQUAD_PACKED', '') != "yes":
        env['CM_DATASET_SQUAD_TOKENIZED_ROOT'] = cur
        if env.get('CM_DATASET_RAW', '') == "yes":
            env['CM_DATASET_SQUAD_TOKENIZED_INPUT_IDS'] = os.path.join(cur, 'bert_tokenized_squad_v1_1_input_ids.raw')
            env['CM_DATASET_SQUAD_TOKENIZED_SEGMENT_IDS'] = os.path.join(cur, 'bert_tokenized_squad_v1_1_segment_ids.raw')
            env['CM_DATASET_SQUAD_TOKENIZED_INPUT_MASK'] = os.path.join(cur, 'bert_tokenized_squad_v1_1_input_mask.raw')
        else:
            env['CM_DATASET_SQUAD_TOKENIZED_PICKLE_FILE'] = os.path.join(cur, 'bert_tokenized_squad_v1_1.pickle')

        env['CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH'] = env['CM_DATASET_MAX_SEQ_LENGTH']
        env['CM_DATASET_SQUAD_TOKENIZED_DOC_STRIDE'] = env['CM_DATASET_DOC_STRIDE']
        env['CM_DATASET_SQUAD_TOKENIZED_MAX_QUERY_LENGTH'] = env['CM_DATASET_MAX_QUERY_LENGTH']

    else:
        with open("packed_filenames.txt", "w") as f:
            for dirname in os.listdir(cur):
                if os.path.isdir(dirname) and not dirname.startswith("_"):
                    f.write(os.path.join(cur, dirname, "input_ids.raw") + "," + os.path.join(cur, dirname, "input_mask.raw") + "," + os.path.join(cur, dirname, "segment_ids.raw") + "," + os.path.join(cur, dirname, "input_position_ids.raw")+ "\n")
        env['CM_DATASET_SQUAD_TOKENIZED_PACKED_FILENAMES_FILE'] = os.path.join(cur, "packed_filenames.txt")

    return {'return':0}
