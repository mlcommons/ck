from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']
    automation = i['automation']

    extra = env.get('CM_GENERIC_PYTHON_PIP_EXTRA','')

    # Check extra index URL
    extra_index_url = env.get('CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL','').strip()
    if extra_index_url != '':
        # Check special cases
        if '${CM_TORCH_CUDA}' in extra_index_url:
            extra_index_url=extra_index_url.replace('${CM_TORCH_CUDA}', env.get('CM_TORCH_CUDA'))
        
        extra += ' --extra-index-url '+extra_index_url

    # Check update
    if env.get('CM_GENERIC_PYTHON_PIP_UPDATE','') in [True,'true','yes','on']:
        extra +=' -U'

    env['CM_GENERIC_PYTHON_PIP_EXTRA'] = extra
    
    package_name = env.get('CM_GENERIC_PYTHON_PACKAGE_NAME', '').strip()
    if package_name == '':
        return automation._available_variations({'meta':meta})

    return {'return':0}
