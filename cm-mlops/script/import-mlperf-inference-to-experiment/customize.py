import cmind as cm
from cmind import utils

import os
import subprocess
import csv
import json
import copy


file_summary = 'summary.csv'
file_summary_json = 'mlperf-inference-summary-{}.json'
file_result = 'cm-result.json'

model2task = {
   "resnet":"image-classification",
   "retinanet":"object-detection",
   "ssd-small":"object-detection",
   "ssd-large": "object-detection",
   "rnnt":"speech-recognition",
   "bert-99":"language-processing",
   "bert-99.9":"language-processing",
   "gptj-99":"language-processing",
   "gptj-99.9":"language-processing",
   "llama2-70b-99":"language-processing",
   "llama2-70b-99.9":"language-processing",
   "dlrm-99":"recommendation",
   "dlrm-v2-99":"recommendation",
   "dlrm-99.9":"recommendation",
   "dlrm-v2-99.9":"recommendation",
   "3d-unet-99":"image-segmentation",
   "3d-unet-99.9":"image-segmentation",
   "stable-diffusion-xl":"text-to-image"
}

def preprocess(i):

    env = i['env']

    cur_dir = os.getcwd()

    # Query cache for results dirs
    r = cm.access({'action':'find',
                   'automation':'cache,541d6f712a6b464e',
                   'tags':'get,repo,mlperf-inference-results'})
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
                    version = 'v'+t[8:]
                    break

            skip_submission_checker = env.get('CM_SKIP_SUBMISSION_CHECKER','') in ['yes','True']

            print ('')
            print ('Processing results in path: {}'.format(path))
            print ('Version: {}'.format(version))
            print ('')

            if skip_submission_checker:
                if not os.path.isfile(file_summary):
                    return {'return':1, 'error':'{} not found'.format(file_summary)}
            else:
                if os.path.isfile(file_summary):
                    os.remove(file_summary)

                print ('* Running submission checker ...')

                xenv = {}

                submitter = env.get('CM_MLPERF_SUBMITTER', '')
                if submitter != '':
                    xenv['CM_MLPERF_SUBMITTER'] = submitter

                ii = {'action':'run',
                      'automation':'script',
                      'tags':'run,mlperf,inference,submission,checker',
                      'extra_args':' --skip-extra-files-in-root-check',
                      'submission_dir':path}

                if len(xenv)>0:
                    ii['env'] = xenv

                if version!='':
                    print ('  Version detected from cache tags: {}'.format(version))
                    ii['version']=version

                r = cm.access(ii)
                # Ignore if script fails for now (when some results are wrong)
                if r['return']>0 and r['return']!=2:
                    return r

                if r['return']>0:
                    print ('')
                    print ('WARNING: script returned non-zero value - possible issue - please check!')
                    print ('')
                    input ('Press Enter to continue')
                    print ('')

            r = convert_summary_csv_to_experiment(path, version, env)
            if r['return']>0: return r

    return {'return':0}


def convert_summary_csv_to_experiment(path, version, env):
    print ('* Processing MLPerf repo in cache path: {}'.format(path))

    cur_dir = os.getcwd()

    # Get Git URL
    os.chdir(path)

    burl = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
    url = burl.decode('UTF-8').strip()

    print ('  Git URL: {}'.format(url))

    os.chdir(cur_dir)

    if os.path.isfile(file_summary):
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

                accuracy = result.get('Accuracy', 0.0)
#
#                print (accuracy, type(accuracy))
                if accuracy!=None and accuracy!='None' and accuracy>0:
                    result['Accuracy_div_100'] = float('{:.5f}'.format(result['Accuracy']/100))

                # Add ratios


                # Append to summary
                summary.append(result)

        r=utils.save_json(file_summary_json.format(version), summary)
        if r['return']>0: return r

        # Create virtual experiment entries
        experiment = {}

        for result in summary:

            # Create name
            mlperfmodel = result['MlperfModel']
            task = model2task[mlperfmodel]

            system_type = result['SystemType']

            division = result['Division']
            has_power = result.get('has_power', False)

            if division == 'network':
                xdivision = 'closed-network'
            else:
                xdivision = division.lower()
                if has_power:
                    xdivision += '-power'

            # If datacenter,edge - remove ,edge to be consistent with https://mlcommons.org/en/inference-datacenter-21/
            j=system_type.find(',')
            if j>=0:
                system_type=system_type[:j]

            scenario = result['Scenario'].lower()

            name = 'mlperf-inference--{}--'+system_type+'--'+xdivision+'--'+task+'--'+scenario

            name_all = name.format('all')
            name_ver = name.format(version)

            for name in [name_all, name_ver]:
                if name not in experiment: experiment[name]=[]
                experiment[name].append(result)

        # Checking experiment
        env_target_repo=env.get('CM_IMPORT_MLPERF_INFERENCE_TARGET_REPO','').strip()
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

                # Get Result and Units together
                if 'Result' in result and 'Units' in result:
                    result['Result_Units']=result['Units']

                # Temporal hack for Power to separate power from the graph
                units = result.get('Units','')
                if units == 'Watts' or 'joules' in units:
                    if 'Result_Power' not in result:
                        result['Result_Power']=result['Result']
                        result['Result']=None

            # Write results
            r=utils.save_json(fresult, results)
            if r['return']>0: return r

    return {'return':0}
