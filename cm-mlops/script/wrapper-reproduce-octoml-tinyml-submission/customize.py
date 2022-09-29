from cmind import utils
import os
import cmind as cm

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']
    inp = i['input']
    if 'CM_FLASH_BOARD' in env:
        script_tags =  "flash,tiny"
    else:
        script_tags =  "reproduce,tiny,mlperf,octoml"
    boards = ["NUCLEO", "NRF" ]
    microtvm_variants = { "cmsis_nn": [ "ad", "ic", "vww", "kws" ], "native": [ "ic", "ad", "vww", "kws"] }
    for board in boards:
        for microtvm_variant in microtvm_variants:
            if board == "NRF" and microtvm_variant == "native":
                continue
            for model in microtvm_variants[microtvm_variant]:
                variation_tags_string="_"+board+",_"+microtvm_variant+",_"+model
                tags = script_tags + "," + variation_tags_string
                if 'CM_RECREATE_BINARY' in env:
                    r = cm.access({'action':'rm', 'automation':'cache', 'tags': tags, 'force': 'true'})
                    if r['return'] > 0:
                        return r
                r = cm.access({'action':'run', 'automation':'script', 'tags': tags, 'quiet': 'true', 'env': env,
                    'input': inp, 'state': state, 'add_deps': inp.get('add_deps', {}), 'add_deps_recursive':
                        inp.get('add_deps_recursive', {})})
                if r['return'] > 0:
                    return r

    return {'return':0}

def postprocess(i):
    return {'return':0}
