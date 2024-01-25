from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    print ('')
    print ('Running preprocess function in customize.py ...')

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']


#    print ('')
#    print ('Running postprocess function in customize.py ...')

    # Saving predictions to JSON file to current directory
    # Should work with "cm docker script" ?

    data = state.get('cm_app_image_classification_onnx_py',{})

    try:
        import json
        with open('cm-image-classification-onnx-py.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print ('CM warning: {}'.format(e))

    try:
        import yaml
        with open('cm-image-classification-onnx-py.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(data, f)
    except Exception as e:
        print ('CM warning: {}'.format(e))


    
    return {'return':0}
