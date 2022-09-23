from cmind import utils
import os
import cmind as cm

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    script_tags =  "reproduce,tiny,app"
    microtvm_variants = { "cmsis_nn": [ "ad", "ic", "vww", "kws" ], "native": [ "ic"] }
    for microtvm_variant in microtvm_variants:
        for model in microtvm_variants[microtvm_variant]
        variation_tags_string="_"+microtvm_variant+"_"+model
        tags = script_tags + variation_tags_string
        r = cm.access({'action':'run', 'automation':'script', 'tags': tags, 'quiet': 'true', 'env': env, 
            'input': inp, 'state': state, 'add_deps': inp.get('add_deps', {}), 'add_deps_recursive':
                    inp.get('add_deps_recursive', {})})
        if r['return'] > 0:
            return r

    return {'return':0}

def postprocess(i):
    print("The binaries to flash can be found by \"find `cm find cache --tags=microtvm,source` --name zephyr.elf\"") 
    return {'return':0}
