# Developer: Grigori Fursin

import os

def main():
    # For now quick prototype hardwired to "summary.json" from MLPerf
    # Later need to clean it and make it universal

    print ('')
    print ('Reading summary.json ...')
    print ('')

    import json
    f = open('summary.json')

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
    if dashboard_project == '': dashboard_project = 'cm-mlperf-sc22-scc-retinanet-offline'

    for k in results:

        result=results[k]

        organization = result.get('Organization', '')
        if organization == '': organization = 'anonymous'

        label = organization

        system_name = result.get('SystemName','')
        if system_name != '': label += '(' + system_name + ')'

        qps = result.get('Result', 0.0)
        accuracy = result.get('Accuracy', 0.0) / 100

        result['performance']=qps
        result['accuracy']=accuracy

        wandb.init(entity = dashboard_user, 
                   project = dashboard_project, 
                   name = label)

        wandb.log(result)

        wandb.finish()

    print ('=========================================================')

if __name__ == '__main__':
    main()
