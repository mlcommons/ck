# Developer: Grigori Fursin

import os

def main():
    # For now quick prototype hardwired to "summary.json" from MLPerf
    # Later need to clean it and make it universal

    print ('')
    print ('Reading summary.json ...')
    print ('')

    import json
    filename = os.environ.get('MLPERF_INFERENCE_SUBMISSION_SUMMARY','')
    if filename=='':
        filename = 'summary'
    filename+='.json'

    f = open(filename)

    results = json.load(f)

    f.close()

    print ('=========================================================')
    print ('Sending results to W&B dashboard ...')
    print ('')

    import wandb

    env = os.environ

    dashboard_user = env.get('CM_MLPERF_DASHBOARD_WANDB_USER', '')
    if dashboard_user == '': dashboard_user = 'cmind'

    dashboard_project = env.get('CM_MLPERF_DASHBOARD_WANDB_PROJECT', '')
    if dashboard_project == '': dashboard_project = 'cm-mlperf-dse-testing'

    for k in results:

        result=results[k]

        organization = str(result.get('Organization', ''))
        if organization == '': organization = 'anonymous'

        label = organization

        system_name = str(result.get('SystemName',''))
        if system_name != '': label += '(' + system_name + ')'

        qps = result.get('Result', 0.0)
        accuracy = result.get('Accuracy', 0.0) / 100

        result['performance'] = qps
        result['qps'] = qps
        result['accuracy'] = accuracy

        # Check extra env variables
        x = {
          "lang": "CM_MLPERF_LANG",
          "device": "CM_MLPERF_DEVICE",
          "submitter": "CM_MLPERF_SUBMITTER",
          "backend": "CM_MLPERF_BACKEND",
          "model": "CM_MLPERF_MODEL",
          "run_style": "CM_MLPERF_RUN_STYLE",
          "rerun": "CM_RERUN",
          "hw_name": "CM_HW_NAME",
          "max_batchsize": "CM_MLPERF_LOADGEN_MAX_BATCHSIZE",
          "num_threads": "CM_NUM_THREADS",
          "scenario": "CM_MLPERF_LOADGEN_SCENARIO",
          "test_query_count": "CM_TEST_QUERY_COUNT",
          "run_checker": "CM_RUN_SUBMISSION_CHECKER",
          "skip_truncation": "CM_SKIP_TRUNCATE_ACCURACY"
        }

        for k in x:
            env_key = x[k]
            if os.environ.get(env_key,'')!='':
               result['cm_misc_input_'+k]=os.environ[env_key]

        wandb.init(entity = dashboard_user, 
                   project = dashboard_project, 
                   name = label)

        wandb.log(result)

        wandb.finish()

    print ('=========================================================')

if __name__ == '__main__':
    main()
