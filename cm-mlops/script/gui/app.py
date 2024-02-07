# Developer(s): Grigori Fursin

import streamlit as st
import os
import cmind

import misc

def main():
    
    query_params = misc.get_params(st)

    script_path = os.environ.get('CM_GUI_SCRIPT_PATH','')
    script_alias = os.environ.get('CM_GUI_SCRIPT_ALIAS','')
    title = os.environ.get('CM_GUI_TITLE', '')

    # Check if script tags are specified from CMD
    script_tags = os.environ.get('CM_GUI_SCRIPT_TAGS','').strip()

    script_tags_from_url = query_params.get('tags',[''])
    if len(script_tags_from_url)>0:
        x_script_tags_from_url = script_tags_from_url[0].strip()
        if x_script_tags_from_url != '':
            script_tags = x_script_tags_from_url

    meta = {}

    if script_tags !='':
        # Check type of tags
        if ' ' in script_tags:
            script_tags = script_tags.replace(' ',',')

        print ('Searching CM scripts using tags "{}"'.format(script_tags))

        r = cmind.access({'action':'find', 
                          'automation':'script,5b4e0237da074764', 
                          'tags':script_tags})
        if r['return']>0: return r

        lst = r['list']

        if len(lst)==1:
            script = lst[0]
            meta = script.meta
            script_path = script.path
            script_alias = meta['alias']



    # Read meta
    if len(meta)==0 and script_path!='' and os.path.isdir(script_path):
        fn = os.path.join(script_path, '_cm')
        r = cmind.utils.load_yaml_and_json(fn)
        if r['return'] == 0:
            meta = r['meta']
            script_path = script.path
            script_alias = meta['alias']

    import script

    ii = {'st': st,
          'params': query_params,
          'script_path': script_path, 
          'script_alias': script_alias, 
          'script_tags': script_tags, 
          'script_meta': meta,
          'skip_bottom': False}
    
    return script.page(ii)

if __name__ == "__main__":
    main()
