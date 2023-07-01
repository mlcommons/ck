import cmind as cm
from cmind import utils

import os
import subprocess
import csv
import json
import copy


file_summary = 'summary.csv'
file_summary_json = 'mlperf-training-summary-{}.json'
file_summary2 = 'summary.xlsx'
file_result = 'cm-result.json'

model2task = {
   "resnet":"image-classification",
   "maskrcnn":"object-detection-heavy-weight",
   "ssd":"object-detection-light-weight",
   "minigo": "reinforcement-learning",
   "rnnt":"speech-recognition",
   "bert":"language-processing",
   "dlrm":"recommendation",
   "3dunet":"image-segmentation"
}

model2dataset = {
   "resnet":"ImageNet",
   "maskrcnn":"COCO",
   "ssd":"OpenImages",
   "minigo": "Go",
   "rnnt":"LibriSpeech",
   "bert":"Wikipedia",
   "dlrm":"1TB Clickthrough",
   "3dunet":"KiTS19"
}


model2accuracy = {
   "resnet":75.9,
   "maskrcnn":0.377,
   "ssd":34.0,
   "minigo": 50,
   "rnnt":0.058,
   "bert":0.72,
   "dlrm":0.8025,
   "3dunet":0.908
}

model2accuracy_metric = {
   "resnet":"% classification",
   "maskrcnn":"Box min AP",
   "ssd":"% mAP",
   "minigo": "% win rate vs. checkpoint",
   "rnnt":"Word Error Rate",
   "bert":"Mask-LM accuracy",
   "dlrm":"AUC",
   "3dunet":"Mean DICE score"
}

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    cur_dir = os.getcwd()

    # Clean summary files
    for f in [file_summary, file_summary2]:
        if os.path.isfile(f):
            os.remove(f)

    # Query cache for results dirs
    r = cm.access({'action':'find',
                   'automation':'cache,541d6f712a6b464e',
                   'tags':'get,repo,mlperf-training-results'})
    if r['return']>0: return r

    lst = r['list']

    for c in lst:
        path = os.path.join(c.path, 'repo')

        if os.path.isdir(path):

            meta = c.meta

            tags = meta['tags']

            version = ''
            for t in tags:
                if t.startswith('version-'):
                    version = t[8:]
                    break

            # Run MLPerf logger
            run_script_input = i['run_script_input']
            automation = i['automation']

            env['CM_MLPERF_TRAINING_REPO_PATH'] = path
            env['CM_MLPERF_TRAINING_CURRENT_DIR'] = cur_dir
            env['CM_MLPERF_TRAINING_REPO_VERSION'] = version

            print ('')
            print ('Repo path:    {}'.format(path))
            print ('Repo version: {}'.format(version))

            r = automation.run_native_script({'run_script_input':run_script_input, 
                                              'env':env, 
                                              'script_name':'run_mlperf_logger'})
            if r['return']>0:
                return r

            r = convert_summary_csv_to_experiment(path, version, env)
            if r['return']>0: return r

    return {'return':0}


def convert_summary_csv_to_experiment(path, version, env):
    print ('* Processing MLPerf training results repo in cache path: {}'.format(path))

    cur_dir = os.getcwd()

    # Get Git URL
    os.chdir(path)

    burl = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
    url = burl.decode('UTF-8').strip()

    print ('  Git URL: {}'.format(url))

    os.chdir(cur_dir)

    if not os.path.isfile(file_summary):
        return {'return':1, 'error':'{} was not created'.format(file_summary)}
    else:
        summary = []

        with open (file_summary, encoding = 'utf-8') as fcsv:
            csv_reader = csv.DictReader(fcsv)

            for rows in csv_reader:
                result = {}

                keys = rows.keys()

                for k in keys:
                    v = rows[k]

                    if v == 'False':
                        v=False
                    elif v == 'True':
                        v=True
                    else:
                        try:
                           v=float(v)

                           if v==int(v):
                              v=int(v)
                        except ValueError:
                           pass

                    result[k] = v

                # Add extra tags
                if url!='':
                    result['git_url']=url

                    location = result.get('Location','')
                    if location != '':
                        result['url']=url+'/tree/master/'+location

                if result.get('Accuracy',0)>0:
                    result['Accuracy_div_100'] = float('{:.5f}'.format(result['Accuracy']/100))

                # Add ratios


                # Append to summary
                summary.append(result)

        r=utils.save_json(file_summary_json.format(version), summary)
        if r['return']>0: return r

        # Create virtual experiment entries
        experiment = {}

        for result in summary:

            for model in model2task:
                if result.get(model, '')!='':
                    result1 = {}

                    result1['Result'] = result[model]
                    result1['Result_Units'] = 'min.'
                    result1['Accuracy'] = model2accuracy[model]
                    result1['Accuracy_Metric'] = model2accuracy_metric[model]
                    result1['Task'] = model2task[model]
                    result1['Benchmark'] = model2task[model]
                    result1['Dataset'] = model2dataset[model]
                    result1['Model_ID'] = model

                    result1['_Result'] = result[model]
                    result1['_Result_Units'] = 'min.'
                    result1['_Accuracy'] = model2accuracy[model]
                    result1['_Accuracy_Metric'] = model2accuracy_metric[model]
                    result1['_Task'] = model2task[model]
                    result1['_Dataset'] = model2dataset[model]
                    result1['_Model_ID'] = model

                    result1['version']=version
                    result1['_version']=version
                    result1['Organization']=result['submitter']
                    result1['_Organization']=result['submitter']
                    result1['_System']=result['system']

                    for k in result:
                        if k==model or k not in model2task:
                            result1[k]=result[k]

                    xdivision = result['division']

                    name = 'mlperf-training--{}--'+xdivision+'--'+model2task[model]

                    name_all = name.format('all')
                    name_ver = name.format(version)

                    for name in [name_all, name_ver]:
                        if name not in experiment: experiment[name]=[]
                        experiment[name].append(result1)

        # Checking experiment
        env_target_repo=env.get('CM_IMPORT_MLPERF_TRAINING_TARGET_REPO','').strip()
        target_repo='' if env_target_repo=='' else env_target_repo+':'

        print ('')
        for name in experiment:
            print ('    Preparing experiment artifact "{}"'.format(name))

            tags = name.split('--')
            if 'mlperf' not in tags: tags.insert(0, 'mlperf')

            # Checking if experiment already exists
            r = cm.access({'action':'find',
                           'automation':'experiment,a0a2d123ef064bcb',
                           'artifact':target_repo+name})
            if r['return']>0: return r

            lst = r['list']

            if len(lst)==0:
                r = cm.access({'action':'add',
                               'automation':'experiment,a0a2d123ef064bcb',
                               'artifact':target_repo+name,
                               'tags':tags})
                if r['return']>0: return r

                path = r['path']
            else:
                path = lst[0].path

            results = experiment[name]

            # Check if already date directory
            dirs = os.listdir(path)

            path2 = ''
            for d in dirs:
                dd = os.path.join(path, d)
                if os.path.isdir(dd):
                    path2 = dd
                    break

            if path2=='':

                r = utils.get_current_date_time({})
                if r['return']>0: return r

                date_time = r['iso_datetime'].replace(':','-').replace('T','.')

                path2 = os.path.join(path, date_time)

                os.makedirs(path2)

            # Check if cm-result.json
            fresult = os.path.join(path2, file_result)

            if os.path.isfile(fresult):
                r=utils.load_json(fresult)
                if r['return']>0: return r

                existing_results = r['meta']

                # Need to check which ones to add
                for result in existing_results:
                    found = False

                    # New results
                    for result2 in results:
                        matched = True

                        # Need to iterate over keys in the new results since old results can have more keys (derivates, etc)
                        for k in result2:
                            if k!='uid':
                                if k not in result or result2[k]!=result[k]:
                                    matched = False
                                    break

                        if matched:
                            found = True
                            break

                    if not found:
                        results.append(result)

            # Check extra keys
            final_results=[]
            for result in results:
                # Generate UID
                if 'uid' not in result:
                    r=utils.gen_uid()
                    if r['return']>0: return r

                    result['uid'] = r['uid']

            # Write results
            r=utils.save_json(fresult, results)
            if r['return']>0: return r

    return {'return':0}
