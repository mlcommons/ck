# Author and developer: Grigori Fursin

from cmind import utils

def run(i):
    ###################################################################
    # Prepare flow

    misc = i['misc']
    cmind = i['cmind']
    state = i['state']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    run_cmd = misc['helpers']['run_cmd']
    prepare_work_dir = misc['helpers']['prepare_work_dir']

    self_task_alias = misc['flex.task_alias']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)
    new = _input2.get('new', False)
    renew = _input2.get('renew', False)

    _input = i['input']

    env = _input2.get('env', {})
    name = _input.get('name', '')
    model_tags = _input.get('model_tags', '')
    path = _input.get('path', '')
    directory = _input.get('directory', '')
    connect = _input.get('connect', False)

    if path == '':
        # Check flex.cfg:mlperf
        r = cmind.x({'automation':self_meta['use']['flex.cfg'],
                     'action':'load',
                     'artifact':'mlperf'})
        if r['return'] == 0:
            path = r['meta'].get('storage_for_models', '')

    if verbose:
        x = model_tags if model_tags != '' else name
        print ('')
        print (f'INFO Use model "{x}"')

    r = cmind.x({'automation': self_meta['use']['flex.common'],
                 'action': 'select_artifact',
                 'selected_text': 'Select model',
                 'selected_automation': self_meta['use']['flex.model'],
                 'selected_artifact': name,
                 'selected_tags': model_tags,
                 'quiet': quiet,
                 'control':{'out':out}})

    if r['return']>0: return cmind.embed_error(r)

    model_object = r['selected_artifact_object']

    model_meta = model_object.meta
    model_path = model_object.path

    model_artifact_name = model_meta['alias']
    model_artifact_uid = model_meta['uid']

    ###############################################################
    # Check deps
    deps = model_meta.get('global_deps', [])

    tmp_deps = {}

    if len(deps)>0:
        process_deps = misc['helpers']['process_deps']

        r = process_deps(cmind, deps, state, misc['flex.task'],
                         verbose = verbose, console = console, quiet = quiet, 
                         tmp = {})
        if r['return'] >0: return r

        tmp_deps = r['tmp']


    # Check if has extra processing automation
    # for complex processing of paths and ENVs
    r = utils.load_module(cmind, model_path, 'modulex.py')
    if r['return'] >0: return cmind.embed_error(r)

    sub_module_obj = r['sub_module_obj']
    sub_module_path = r['sub_module_path']


    ###############################################################
    # Check if in cache
    cache_tags = misc['cache_tags']
    cache_meta = misc['cache_meta']

    model_tags = model_meta['tags']
    for tag in model_tags:
        if cache_tags != '': cache_tags += ','
        cache_tags += tag

    repo = _input.get('repo', '')
    if 'repo' in _input:
        if cache_tags != '': cache_tags += ','
        cache_tags += f'_repo.{repo}'


    r = prepare_work_dir(cmind, console, misc['cache_automation'], 
                         True, cache_tags, cache_meta, 
                         quiet = quiet,
                         verbose = verbose,
                         renew = renew,
                         new = new,
                         cache_name_prefix = self_task_alias)
    if r['return'] > 0: return cmind.embed_error(r)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # If cached, return cached output and workdir
    if len(r.get('output', {})) > 0:
        return r


    ##############################################################
    # Resume
    cache_uid = r['cache_uid']

    rr = {'return':0,
          '_update_cache_uid':cache_uid,
          '_update_cache_meta':cache_meta,
          '_update_cache_tags':cache_tags,
          '_cmx_model_alias': model_artifact_name,
          '_cmx_model_uid': model_artifact_uid,
          '_cmx_model_path': model_path,
          '_cmx_model_meta': model_meta
         }

    if sub_module_obj != None and hasattr(sub_module_obj, 'install'):
        cmind.log(f"use-model: call 'install' in {sub_module_path}", "info")

        r = sub_module_obj.install({'automation_flex_task_use_model':self_meta['use']['flex.model'],
                                    'cmind': cmind,
                                    'state': state,
                                    'misc': misc,
                                    'env': env,
                                    'tmp': tmp_deps,
                                    'model_meta': model_meta,
                                    'model_path': model_path,
                                    'path': path,
                                    'repo': repo,
                                    'directory': directory,
                                    'connect': connect,
                                    'out': out,
                                    'verbose': verbose,
                                    'console': console,
                                    'quiet': quiet,
                                    'new': new,
                                    'renew': renew,
                                    'self_meta': self_meta})
        if r['return'] > 0: return r

        rr.update(r)

    return rr
