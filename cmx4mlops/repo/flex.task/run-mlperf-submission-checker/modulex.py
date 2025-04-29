# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']
    cmx = state['cmx']

    misc = i['misc']
    out = misc.get('out', '')
    console = misc.get('console', False)
    self_meta = misc['meta']

    run_cmd = misc['helpers']['run_cmd']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    benchmark = _input.get('benchmark', '')
    if benchmark == '':
        return cmind.prepare_error(1, 'benchmark is not specified')

    env = _input2.get('env', {})
    timeout = _input.get('timeout', None)
    skip_submission_checker_errors = _input.get('skip_submission_checker_errors', False)
    skip_if_summary_exists = _input.get('skip_if_summary_exists', False)
    path = _input.get('path', '')

    if path == '': path = os.getcwd()
    path2 = utils.path2(path)

    cur_dir = os.getcwd()

    os.chdir(path)

    url = _input.get('url', '')

    short_run = _input.get('short_run', False)

    extra_flags = _input.get('extra_flags', '')
    if extra_flags != '':
        extra_flags = ' ' + extra_flags.strip()

    target_json = _input.get('target_json', '')

    # Get correct version of inference repo with submission checker
    version = _input.get('version', '')
    checkout = _input.get('checkout')

    version_alias = version

    truncate_accuracy_log = _input.get('truncate_accuracy_log', False)
    submitter = _input.get('submitter', '')
    if truncate_accuracy_log and submitter == '':
        return cmind.prepare_error(1, 'submitter is not specified to truncate accuracy')

    # Clean summary.csv
    csvs = []

    target = 'summary.csv'
    if target_json == '': target_json = 'summary.json'

    if not skip_if_summary_exists or not os.path.isfile(target):

        for f in [target, target_json]:
            if os.path.isfile(f):
                os.remove(f)

        ################################################################################
        # MLPerf inference
        if benchmark  == 'inference':
            if version == '5.0':
                version = '5.0'
                checkout = ''
    #            if '--skip-extra-accuracy-files-check' not in extra_flags:
    #                extra_flags += ' --skip-extra-accuracy-files-check'
            elif version == '5.0-test':
                version = '5.0'
                if '--skip-extra-files-in-root-check' not in extra_flags:
                    extra_flags += ' --skip-extra-files-in-root-check'
                short_run = True
            elif version == '5.0-unofficial':
                version = '5.0'
                if '--skip-extra-files-in-root-check' not in extra_flags:
                    extra_flags += ' --skip-extra-files-in-root-check'
                short_run = True
            elif version == 'scc24-live':
                version = '4.1'
                if '--skip-extra-files-in-root-check' not in extra_flags:
                    extra_flags += ' --skip-extra-files-in-root-check'
                short_run = True
            elif version == '4.1':
                checkout = ''
                if '--skip-extra-accuracy-files-check' not in extra_flags:
                    extra_flags += ' --skip-extra-accuracy-files-check'
            elif version in ['3.0', '3.1']:
                checkout = 'v3.1'

            xversion = f' --version v{version}' if version != '' else ''

            if checkout == None:
                if version != '':
                    checkout = 'v' + version
                else:
                    checkout = ''

            # Clone repo with inference src
            ii = {'action':'run',
                  'automation':misc['flex.task'],
                  'control':{'out':out},
                  'state':state,
                  'tags':'clone,git,repo',
                  'alias':'mlperf-inference-src',
                  'url': url,
        #          'depth': 1, # can't use it since need to do a specific checkout
                  'checkout': checkout,
                  'cache': True,
                  'add_to_state': 'cmx.mlperf_inference_src',
                  'cache_tags': f'mlperf-inference-src,_version.{version}',
                  'verbose': verbose
                 }

            r = cmind.x(ii)
            if r['return']>0: return cmind.embed_error(r)

            # Get path to MLPerf Inference Src
            path_to_mlperf_inference_src = r['path_to_git_repo']
            submission_checker = os.path.join(path_to_mlperf_inference_src, 'tools', 'submission', 'submission_checker.py')
            truncate_accuracy_log_py = os.path.join(path_to_mlperf_inference_src, 'tools', 'submission', 'truncate_accuracy_log.py')

            if short_run:
                submission_checker_short_run = os.path.join(os.path.dirname(submission_checker), "submission_checker_short_run.py")

                if not os.path.isfile(submission_checker_short_run):
                    with open(submission_checker, 'r') as file:
                        data = file.read()

                    data = data.replace("OFFLINE_MIN_SPQ = 24576", "OFFLINE_MIN_SPQ = 100")

                    data = data.replace("return is_valid, res, inferred", "return True, res, inferred")

                    with open(submission_checker_short_run, 'w') as file:
                        file.write(data)

                submission_checker = submission_checker_short_run

            submission_checker2 = utils.path2(submission_checker)


            # Prepare CMD for accuracy_pruning
            if truncate_accuracy_log:
                path_to_python = cmx['sys_tool_python']['sys_tool_python_with_path2']

                cmd = f'{path_to_python} {truncate_accuracy_log_py} --input {path} --backup {path}_backup --submitter {submitter}'

                print ('')
                r = run_cmd(cmind, console, cmd, env, timeout, state = state, verbose = verbose)
                if r['return']>0: 
                    if not skip_submission_checker_errors:
                        return cmind.embed_error(r)

                print ('')

            # Prepare CMD
            path_to_python = cmx['sys_tool_python']['sys_tool_python_with_path2']

            cmd = f"""{path_to_python} {submission_checker} --input {path}{xversion}{extra_flags}"""

            r = run_cmd(cmind, console, cmd, env, timeout, state = state, verbose = verbose)
            if r['return']>0: 
                if not skip_submission_checker_errors:
                    return cmind.embed_error(r)


        ################################################################################
        # MLPerf training

        elif benchmark  == 'training':

            # Use sys tool mlperf_loggging
            ii = {'action':'run',
                  'automation':misc['flex.task'],
                  'control':{'out':out},
                  'state':state,
                  'tags':'use,sys,tool',
                  'name':'pip_generic',
                  'package':'mlperf_logging',
                  'install_url':'git+https://github.com/mlperf/logging.git',
                  'alias':'pip-mlperf-logger',
                  'verbose': verbose
                 }

            r = cmind.x(ii)
            if r['return']>0: return r

            # Iterate over organizations with "results"
            for org in os.listdir():
                path1 = os.path.join(org, 'results')
                if os.path.isdir(path1):
                    print ('')
                    print (f'Processing organization: {org}')
                    print ('')

                    cmds = []

                    org_csv = f'summary.{org}.csv'
                    csvs.append(org_csv)

                    path_to_python = cmx['sys_tool_python']['sys_tool_python_with_path2']
    #                cmds.append(f"""{path_to_python} -m mlperf_logging.package_checker {org} {benchmark} {version}.0{extra_flags}""")
                    cmds.append(f"""{path_to_python} -m mlperf_logging.result_summarizer {org} {benchmark} {version}.0 --csv {org_csv}""")

                    for cmd in cmds:
                        r = run_cmd(cmind, console, cmd, env, timeout, state = state, verbose = verbose)
                        if r['return']>0: 
                            print ('WARNING: submission checker failed')

        ################################################################################

        else:
            return cmind.prepare_error(1, f'{benchmark} is not supported in Flex Task for MLPerf submission checker')

    # Get Git REPO URL and branch

    detected_url = ''

    cmd = 'git config --get remote.origin.url'

    r = run_cmd(cmind, console, cmd, env, None, capture_output = True, 
                state = state, verbose = verbose,
                cmd_prefix_from_state = [])
    if r['return'] == 0:
        detected_url = r['stdout'].strip()
        if detected_url.startswith('git@'):
            detected_url = 'https://' + detected_url[4:].replace(':','/')

    detected_branch = ''

    cmd = 'git rev-parse --abbrev-ref HEAD'

    r = run_cmd(cmind, console, cmd, env, None, capture_output = True, 
                state = state, verbose = verbose,
                cmd_prefix_from_state = [])
    if r['return'] == 0:
        detected_branch = r['stdout'].strip()

    mlperf_url = detected_url
    if detected_branch != '':
        mlperf_url += '/tree/' + detected_branch

    print ('')
    print (f'MLPerf URL: {mlperf_url}')

    # Get last commit to repo (time series)
    cmd = 'git log -1 --format="%at" | xargs -I{} date -d @{} +%Y/%m/%d_%H:%M:%S'

    datetime_last_commit = ''
    r = run_cmd(cmind, console, cmd, env, None, capture_output = True, 
                state = state, verbose = verbose,
                cmd_prefix_from_state = [])
    if r['return'] == 0:
        datetime_last_commit = r['stdout'].strip()

    # Process CSV
    summary = []
    import csv

    if len(csvs) == 0: csvs = [target]

    for target in csvs:
        if not os.path.isfile(target):
            print (f'WARNING: "{target}" file was not created')
            input('Press Enter to continue')
            continue

        ii = {'action':'run',
              'automation':misc['flex.task'],
              'control':{'out':out},
              'state':state,
              'tags':'process,mlperf,csv,results',
              'csv_file': target,
              'benchmark': benchmark,
              'version': version,
              'mlperf_url': mlperf_url,
              'result_extra': {
                    'benchmark_name': f'mlperf-{benchmark}',
                    'benchmark_version': version,
                    'benchmark_version_alias': version_alias,
                    'benchmark_branch': detected_branch,
                    'datetime_last_commit': datetime_last_commit
              },
              'verbose': verbose
             }

        r = cmind.x(ii)
        if r['return']>0: return r

        for s in r['summary']:
            summary.append(s)

    r = utils.save_json(target_json, summary)
    if r['return']>0: return r

    os.chdir(cur_dir)

    return {'return':0, 'summary_csv':target, 'summary_json':target_json}
