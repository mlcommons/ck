# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']

    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    renew = _input2.get('renew', False)

    _input = i['input']
    benchmark = _input.get('benchmark', '')
    url = _input.get('url', '')
    branch = _input.get('branch', '')
    checkout = _input.get('checkout', '')
    version = _input.get('version', '')
    submission = _input.get('submission', False)
    git = _input.get('git', False)
    extra_cache_meta = _input.get('extra_cache_meta', {})
    extra_cache_tags = _input.get('extra_cache_tags', '')
    storage = _input.get('storage', '')
    path_to_results = _input.get('path_to_results', '')
    clean = _input.get('clean', False)
    ximport = _input.get('import', False)
    depth = _input.get('depth', '')

    if version == '' and url == '':
        return cmind.prepare_error(1, 'specify version and/or URL')

    self_meta = misc['meta']
    _vars = self_meta['vars']

    url2 = ''

    if version != '':
        if url == '':
            if submission:
                url2 = _vars['default_submission_url'] + version
            else:
                url2 = _vars['default_url'] + version
    else:
        version = url[-3:]

    if url2 != '':
        if git:
            url = 'git@github.com:'
        else:
            url = 'https://github.com/'

        url += url2

    # Substitute benchmark in URL
    url = url.replace('{{benchmark}}', benchmark)

    # Use Flex Task to clone repo
    if extra_cache_tags != '':
        extra_cache_tags += ','

    extra_cache_tags += '_benchmark.' + benchmark

    extra_cache_tags += ',_version.' + version

    if submission:
        extra_cache_tags += ',_submission'

    extra_cache_tags += ',mlperf-results'

    extra_cache_meta.update({'version': version,
                             'url': url,
                             'benchmark': benchmark,
                             'submission': submission,
                             'git': git})

    # Check where to store
    rr = {'return': 0}

    extra_cmx_output_file = ''

    if path_to_results == '':
        if storage == '':

            # Check flex.cfg:mlperf
            r = cmind.x({'automation':self_meta['use']['flex.cfg'],
                         'action':'load',
                         'artifact':'mlperf'})
            if r['return'] == 0:
                storage = r['meta'].get('storage_for_raw_results', '')

        if storage != '':
            url1 = url
            if url1.endswith('.git'):
                url1 = url1[:-4]

            path_to_results = os.path.join(storage, os.path.basename(url1))

    if path_to_results != '':
        basename = os.path.basename(path_to_results)
        extra_cmx_output_file = os.path.join(os.path.dirname(path_to_results), 
                f'cmx-output.{basename}.json')

        if console:
            print ('')
            print (f'Path to results: {path_to_results}')

        if os.path.isdir(path_to_results) and clean:
            print ('')
            x = input(f'Enter Y to clean directory with results "{path_to_results}": ')

            if x.lower().strip() == 'y':
                print ('')
                print ('Cleaning directory ...')

                import shutil
                shutil.rmtree(path_to_results)

    if ximport and not os.path.isdir(path_to_results):
        return cmind.prepare_error(1, f'Can\'t import from path that doesn\'t exist: {path_to_results}')

    # Prepare run flex task "git clone repo"
    ii = {'action':'run',
          'automation':misc['flex.task'],
          'control':{'out':out},
          'tags':'clone,git,repo',
          'url': url,
          'cache': True,
          'cache_tags': extra_cache_tags,
          'verbose': verbose,
          'renew': renew
         }

    if branch != '': 
        extra_cache_meta['branch'] = branch
        ii['branch'] = branch

    if checkout != '': 
        extra_cache_meta['checkout'] = checkout
        ii['checkout'] = checkout

    if path_to_results != '':
        ii['directory'] = path_to_results

    ii['cache_meta'] = extra_cache_meta

    if depth != '':
        ii['depth'] = depth

    r = cmind.x(ii)
    if r['return'] > 0: return cmind.embed_error(r)

    path_to_results = r['path_to_git_repo']

    rr['git_output'] = r

    rr['path_to_results'] = path_to_results

    # Save extra info
    if extra_cmx_output_file != '':
        r = utils.save_json(extra_cmx_output_file, meta = {'cache_meta':extra_cache_meta, 'output':rr})
        if r['return']>0: return cmind.embed_error(r)

    return rr
