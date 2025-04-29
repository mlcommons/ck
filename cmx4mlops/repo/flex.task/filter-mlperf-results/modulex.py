# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']
    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    path = _input.get('path', '')
    benchmark = _input.get('benchmark', '')
    version = _input.get('version', '')
    tags = _input.get('tags', '')
    experiment_repo = _input.get('experiment_repo', '')

    if experiment_repo == '':

        # Check flex.cfg:mlperf
        r = cmind.x({'automation':self_meta['use']['flex.cfg'],
                     'action':'load',
                     'artifact':'mlperf'})
        if r['return'] == 0:
            experiment_repo = r['meta'].get('experiment_repo', '')

    if experiment_repo == '':
        experiment_repo = 'local'

    # Check path
    if path != '':
        if not os.path.isdir(path):
            return cmind.prepare_error(1, f'path with raw MLPerf results not found: {path}')

        objects.append({'path':path, 
                        'meta':{'benchmark':benchmark,
                                'version':version}})
    else:
        # Query flex.cache 
        find_tags = 'clone,git,repo,mlperf-results'

        if benchmark != '': find_tags += ',_benchmark.' + benchmark

        if version != '': find_tags += ',_version.' + version

        if tags != '': find_tags +=',' + tags

        r = cmind.x({'action':'find',
                     'automation':self_meta['use']['flex.cache'],
                     'tags':find_tags})

        if r['return'] >0: return r

        lst = r['list']

        objects = []

        for l in lst:
            path = l.path
            meta = l.meta

            objects.append({'path':path, 'meta':meta})

    # Go through paths
    summary = {}
    total_results = 0
    for obj in objects:
        path_proxy = obj['path']
        meta = obj['meta']

        # Load CMX output to get extra meta
        path = path_proxy

        cmx_output = os.path.join(path, 'cmx-output.json')

        r = utils.load_json(cmx_output, check_if_exists=True)
        if r['return'] ==0: 
            meta2 = r['meta']
            path = meta2['path_to_git_repo']

            if 'cache_meta' in meta2:
                meta.update(meta2['cache_meta'])

        print ('='*80)
        print (f'MLPerf results path: {path}')

        tags = ','.join(meta.get('tags', []))

        url = meta.get('url', '')
        benchmark = meta.get('benchmark', '')
        version = meta.get('version', '')

        if benchmark == '':
            if 'inference' in path: benchmark = 'inference'
            elif 'training' in path: benchmark = 'training'

        if version == '':
            j = path.lower().find('_v')
            if j>0:
               j1 = path.find('_', j+1)
               if j1<0:
                   version = path[j+2:]
               else:
                   version = path[j+2:j1]

        print (f'MLPerf benchmark: {benchmark}')
        print (f'MLPerf URL: {url}')
        print (f'MLPerf version: {version}')
        print (f'CMX tags: {tags}')

        # Call MLPerf submission checker and summary generators
        cur_dir = os.getcwd()

        os.chdir(path)

        # Check if CSV or JSON already exists
        results_dir = os.path.basename(path)
        target_json = os.path.abspath(os.path.join(path, '..', f'cmx-output.{results_dir}.summary.json'))
        target_keys_json = os.path.abspath(os.path.join(path, '..', f'cmx-output.{results_dir}.summary_keys.json'))

        if not os.path.isfile(target_json):

            ii = {'action': 'run',
                  'automation': misc['flex.task'],
                  'tags': f'run,mlperf,submission,checker',
                  'control': {'out':out},
                  'state': state,
                  'verbose': verbose,
                  'benchmark': benchmark,
                  'version': version,
                  'extra_flags': '--skip-extra-files-in-root-check', #' --skip-empty-files-check --skip-power-check --skip_compliance',
                  'target_json': target_json
                 }

            r = cmind.x(ii)
            if r['return']>0: return r

        if verbose:
            print ('')
            print (f'INFO MLPerf summary JSON file: {target_json}')

        # Get unique keys
        r = utils.load_json(target_json)
        if r['return'] >0: return r

        summary = r['meta']

        keys = {}

        for result in summary:
            total_results += 1
            for k in result:
                v = result[k]

#                if type (k) == list or type(k) == dict:
#                    # TBD - need to flatten
#                    print (v)

                if k not in keys:
                    keys[k] = []

                if v not in keys[k]:
                    keys[k].append(v)

        # Sort lists
        for k in keys:
            v = keys[k]

            numeric = True
            for vv in v:
                if type(vv) not in [int, float]:
                    numeric = False
                    break

            if numeric:
                keys[k] = sorted(v)
            else:
                keys[k] = sorted(v, key = lambda x: str(x))

        r = utils.save_json(target_keys_json, keys)
        if r['return']>0: return r

        # Check flex.experiment
        flex_experiment_artifact = f'{experiment_repo}:mlperf-{benchmark}-{version}-imported'
        flex_experiment_tags = tags + ',imported,cmx'

        r = cmind.x({'action': 'find',
                     'automation': self_meta['use']['flex.experiment'],
                     'artifact': flex_experiment_artifact})
        if r['return'] >0: return cmind.embed_error(r)

        flex_experiment_path = ''
        experiments = r['list']

        if len(experiments) > 1:
            paths = [x.path for x in experiments]
            paths_str = '\n'.join(paths) + '\n'

            r['error'] += ' - delete some to avoid ambiguity\n' + paths_str

        if len(experiments) == 1:
            flex_experiment_path = experiments[0].path
        else:
            r = cmind.x({'action': 'add',
                         'automation': self_meta['use']['flex.experiment'],
                         'artifact': flex_experiment_artifact,
                         'tags': flex_experiment_tags,
                         'meta': {'import_meta':meta},
                         'replace': True})
            if r['return'] >0: return cmind.embedd_error(r)

            flex_experiment_path = r['experiment_path']

        # Check last datetime to store results
        directories = os.listdir(flex_experiment_path)

        datetimes = sorted([f for f in directories if os.path.isfile(os.path.join(flex_experiment_path, f, 'cmx-input.json'))], reverse=True)

        target_experiment_path = os.path.join(flex_experiment_path, datetimes[0])

        print ('')
        print (f'CMX Flex Experiment: {target_experiment_path}')

        target_summary_input = os.path.join(target_experiment_path, 'cmx-input.json')
        target_summary_file = os.path.join(target_experiment_path, 'cmx-result-summary.json')
        target_summary_keys_file = os.path.join(target_experiment_path, 'cmx-result-summary-keys.json')

        r = utils.save_json(target_summary_file, summary)
        if r['return']>0: return r

        r = utils.save_json(target_summary_keys_file, keys)
        if r['return']>0: return r

        input_meta = {}
        if os.path.isfile(target_summary_input):
            r = utils.load_json(target_summary_input)
            if r['return']>0: return r
            input_meta = r['meta']

        input_meta['input'] = meta

        r = utils.save_json(target_summary_input, input_meta)
        if r['return'] >0: return r

#        # Call MLPerf checkers
#        r = utils.call_internal_module(None, __file__, f'modulex_{benchmark}', 'process', {'path':path})
#        if r['return'] > 0: return r

        os.chdir(cur_dir)

        summary.append({'benchmark': benchmark, 'url': url, 'version': version, 'cmx_tags': tags,
                        'results_dir': results_dir, 'target_json': target_json, 'target_keys_json': target_keys_json})

    print ('')
    print (f'Total MLPerf results: {total_results}')

    return {'return':0, 'objects': objects, 'summary': summary, 'total_results': total_results}
