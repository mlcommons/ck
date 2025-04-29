# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy
import shutil

training_models = [
  'bert',
  'dlrm_dcnv2',
  'gpt3',
  'maskrcnn',
  'resnet',
  'ssd',
  'rnnt',
  'unet3d',
  'stable_diffusion',
  'llama2_70b_lora',
  'gnn'
]

submitter_training_subs = {
 "Clemson University Research Computing and Data": "Clemson",
 "RedHat-Supermicro": "Red_Hat",
 "Sustainable Metal Cloud": "smc",
 "NVIDIA+CoreWeave": "NVIDIA_CoreWeave"
}

submitter_training_subs2 = {
 "4.0": {
   "NVIDIA+CoreWeave": "NVIDIA",
   "Sustainable Metal Cloud": "smc",
   "RedHat-Supermicro": "Red_Hat"
 },
 "3.1": {
   "Clemson University Research Computing and Data": "Clemson",
   "NVIDIA+CoreWeave": "NVIDIA",
   "Sustainable Metal Cloud": "smc",
   "RedHat-Supermicro": "Red_Hat"
 }
}

def run(i):

    misc = i['misc']
    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']

    cmx = state['cmx']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    # Get aux input
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    new = _input2.get('new', False)
    renew = _input2.get('renew', False)

    env = _input2.get('env', {})

    # Get main input
    _input = i['input']

    csv_file = _input['csv_file']
    benchmark = _input['benchmark']
    mlperf_url = _input.get('mlperf_url', '')
    version = _input.get('version', '')
    system_desc = _input.get('system_desc', {})
    system_json_file_path = _input.get('system_json_file_path', '')
    result_extra = _input.get('result_extra', {})

    summary = []

    # Process
    import csv

    if console and verbose:
        print (f'Processing {csv_file} in {os.getcwd()} ...')

    try:
        with open (csv_file, encoding = 'utf-8') as fcsv:
            csv_reader = csv.DictReader(fcsv)

            for row in csv_reader:
                # In training, all models are in one row
                rows = []
                if benchmark == 'training':
                    for model_key in training_models:
                        v = row.get(model_key)
                        if v != None and v != '':
                            xrow = {}
                            for k in row.keys():
                                if k in training_models and k != model_key:
                                    continue
                                if k == model_key:
                                   xrow['mlperf_training_model'] = model_key
                                   xrow['result'] = row[k]
                                else:
                                   xrow[k] = row[k]

                            rows.append(copy.deepcopy(xrow))
                else:
                    rows = [row]

                for row in rows:

                    result = {}

                    keys = row.keys()

                    for k in keys:
                        v = row[k]

                        if type(v) == list and len(v) == 1:
                            v = v[0]

                        if v == 'False' or v == 'false':
                            v = False
                        elif v == 'True' or v == 'true':
                            v = True
                        else:
                            try:
                               v=float(v)

                               if v==int(v):
                                  v=int(v)
                            except ValueError:
                               pass

                        result[k] = v

                    # Add extra tags
                    location = ''
                    if mlperf_url != '':
                        result['url_repo'] = mlperf_url

                        location = result.get('Location', '')
                        if location == '':
                            location = result.get('location', '')
                        if location != '':
                            result['url_result'] = mlperf_url + '/' + location

                    result.update(result_extra)

                    # Attempt to load system JSON
                    system_desc_cur = system_desc
                    if len(system_desc) == 0:

                        system_json_file_path_cur = system_json_file_path
                        if system_json_file_path_cur == '':
                            url_system_file = result.get('details_url', '')

                            if url_system_file != '':
                                # MLPerf training
                                system_file_name = os.path.basename(url_system_file)[:-5]

                                x1 = os.path.dirname(url_system_file)
                                x2 = os.path.dirname(x1)
                                x3 = os.path.dirname(x2)

                                system_json_file_path_cur = url_system_file[len(x3)+1:]
                            else:
                                # INFERENCE
                                if location != '':
                                    x1 = os.path.dirname(location)
                                    x2 = os.path.dirname(x1)
                                    system_json_file = os.path.basename(x2) + '.json'
                                    x3 = os.path.dirname(x2)
                                    x4 = os.path.dirname(x3)
                                    system_json_file_path_cur = os.path.join(x4, 'systems', system_json_file)

                                    result['url_system_file'] = mlperf_url + '/' + system_json_file_path_cur.replace('\\', '/')

                            if benchmark == 'training':
                                subs = submitter_training_subs2[version] if version in submitter_training_subs2 else submitter_training_subs
                                for sub in subs:
                                     system_json_file_path_cur = system_json_file_path_cur.replace(sub, subs[sub])

                        if system_json_file_path_cur != '' and not os.path.isfile(system_json_file_path_cur):
                            return cmind.prepare_error(1, f'file "{system_json_file_path_cur}" not found')

                        result['system_file_name'] = os.path.basename(system_json_file_path_cur)

                        r = utils.load_json(system_json_file_path_cur)
                        if r['return'] >0: return cmind.embed_error(r)

                        system_desc_cur = r['meta']

                    # Add flattened system desc to results
                    fd = {}
                    utils.flatten_dict(system_desc_cur, fd, 'system.')

                    for k in fd:
                        if k not in result:
                            result[k] = fd[k]

                    # Generate UID to make it easier to debug result entries
                    r = utils.gen_uid()
                    result['debug_uid'] = r['uid']

                    # Append to summary
                    summary.append(result)

    except Exception as e:
        return cmind.prepare_error(1, f'problem prosessing file "{csv_file}": {e}')

    return {'return':0, 'summary': summary}
