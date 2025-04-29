# Author and developer: Grigori Fursin

from cmind import utils

import os

def run(i):

    ###################################################################
    # Prepare flow
    state = i['state']

    rt_cached = state['cmx'].get('use_system', {})
    if len(rt_cached)>0: return rt_cached

    host_os = state['system']['os']

    cmind = i['cmind']
    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    _input = i['input']

    # Check available names
    artifact = _input.get('name', '')
    tags = _input.get('system_tags', '')
    system = _input.get('desc', {})
    target_system_name = _input.get('target_system_name', '')

    if artifact == '':
        # Use hostname
        artifact = state['cmx']['detect_host_info_min']['host_os']['python_platform_node']
        if tags != '': tags += ','
        tags += artifact

    r = cmind.x({'automation': self_meta['use']['flex.common'],
                 'action': 'select_artifact',
                 'selected_text': 'Select Target System',
                 'selected_automation': self_meta['use']['flex.system'],
                 'selected_artifact': artifact,
                 'selected_tags': tags,
                 'quiet': quiet,
                 'create_if_not_found': True,
                 'control':{'out':out}})
    if r['return']>0: return cmind.embed_error(r)

    system_object = r['selected_artifact_object']

    system_meta = system_object.meta
    system_path = system_object.path

    use_compute_tags = utils.get_set(system_meta, 'use_compute_tags', state, ['flow', 'compute', 'compute_tags'])

    # Read meta
    file_meta = os.path.join(system_path, 'desc.json')

    system_desc = {}

    load_file_meta = file_meta
    if not os.path.isfile(load_file_meta):
        load_file_meta = os.path.join(self_path, 'desc.json')

    if os.path.isfile(load_file_meta):
        r = utils.load_json(load_file_meta)
        if r['return'] >0: return cmind.embed_error(r)

        system_desc = r['meta']

    if system_desc['system_name'] == '':
        system_desc['system_name'] = artifact

    if len(system) > 0:
        utils.merge_dicts({'dict1':system_desc, 'dict2':system, 'append_lists':True, 'append_unique':True})

    # Detect extra info
#    import json
#    print (json.dumps(state['cmx']['detect_host_info_min'], indent=2))

    if not os.path.isfile(file_meta):
        # Save file
        r = utils.save_json(file_meta, system_desc)
        if r['return'] >0: return cmind.embed_error(r)

    # Prepare output
    rrr = {'return':0}

    system_name = system_meta.get('system_name', '')

    if target_system_name != '': system_name = target_system_name
    elif system_name == '': system_name = system_meta['alias']

    rrr['target_system_name'] = system_name
    rrr['target_system_path'] = system_path
    rrr['meta'] = system_meta
    rrr['desc'] = system_desc

    state['cmx']['target_system_name'] = system_name
    state['cmx']['target_system_path'] = system_path

    state['cmx']['use_system'] = rrr

    return rrr
