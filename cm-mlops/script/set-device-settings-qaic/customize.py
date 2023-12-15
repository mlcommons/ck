from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_QAIC_ECC', '') == 'yes':
        import json
        for device in env['CM_QAIC_DEVICES'].split(","):
            ecc_template = {}
            ecc_template['qid'] = device
            ecc_template['dev_config'] = {}
            ecc_template['dev_config']['update_ras_ecc_config_request'] = {}
            ecc_template['dev_config']['update_ras_ecc_config_request']['ras_ecc'] = []
            ecc_template['dev_config']['update_ras_ecc_config_request']['ras_ecc'].append("RAS_DDR_ECC")
            with open("request_"+device+".json", "w") as f:
                f.write(json.dumps(ecc_template)


    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
