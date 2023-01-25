# Developer(s): Grigori Fursin

from cmind import utils

import os
import json
import shutil
import subprocess

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']
    script_path = i['run_script_input']['path']

    cm = i['automation'].cmind

    script_tags = env.get('CM_GUI_SCRIPT_TAGS','')

    if script_tags != '':
        # Check type of tags
        if ' ' in script_tags:
            script_tags = script_tags.replace(' ',',')

        print ('Searching CM scripts using tags "{}"'.format(script_tags))

        r = cm.access({'action':'find', 
                       'automation':'script', 
                       'tags':script_tags})
        if r['return']>0: return r

        lst = r['list']

        if len(lst)==1:
            script = lst[0]
            env['CM_GUI_SCRIPT_PATH'] = script.path
            env['CM_GUI_SCRIPT_ALIAS'] = script.meta['alias']

            print ('Script found in path {}'.format(script.path))

    env['CM_GUI_SCRIPT_TAGS'] = script_tags

    # Check other vars and assemble extra CMD
    extra_cmd = env.get('CM_GUI_EXTRA_CMD','')

    port = env.get('CM_GUI_PORT', '')
    address = env.get('CM_GUI_ADDRESS', '')
    no_browser = env.get('CM_GUI_NO_BROWSER', '')

    if no_browser!='':
        extra_cmd+=' --server.headless true'

    if address!='':
        extra_cmd+=' --server.address='+address

    if port!='':
        extra_cmd+=' --server.port='+port

    env['CM_GUI_EXTRA_CMD'] = extra_cmd

    print ('Prepared extra CMD for streamlit: {}'.format(extra_cmd))

    return {'return':0}
