from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']

    env = i['env']

    # Check if input files are empty and add files
    input_file_1 = env.get('CM_INPUT_1','')
    if input_file_1 == '': input_file_1 = 'ipol-paper-2024-439-sample-image-1.png'

    if not os.path.isfile(input_file_1):
        return {'return':1, 'error':'input file 1 "{}" not found'.format(input_file_1)}

    env['CM_INPUT_1']=os.path.abspath(input_file_1)

    input_file_2 = env.get('CM_INPUT_2','')
    if input_file_2 == '': input_file_2 = 'ipol-paper-2024-439-sample-image-2.png'

    if not os.path.isfile(input_file_2):
        return {'return':1, 'error':'input file 2 "{}" not found'.format(input_file_2)}

    env['CM_INPUT_2']=os.path.abspath(input_file_2)

    return {'return':0}

def postprocess(i):

    print ('')
    print ('Please check "diff.png"')
    print ('')

    return {'return':0}
