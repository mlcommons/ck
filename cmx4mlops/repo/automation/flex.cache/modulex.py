# Author and developer: Grigori Fursin

import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    Automation actions
    """

    CMX_OUTPUT_FILE = 'cmx-output.json'

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
          i (dict): CM input dict

             action (str): CM action
             automation (str): CM automation
             artifact (str): CM artifact
             artifacts (list): list of extra CM artifacts

             control: (dict): various CM control
              (out) (str): if 'con', output to console
              ...

             (flags)
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        # Access CM
        print (self.cmind)

        # Print self path
        print (self.path)

        # Print self meta
        print (self.meta)

        # Print self automation module path
        print (self.automation_file_path)

        # Print self automation module path
        print (self.full_path)

        # Print self artifact
        print (self.artifact)

        # Print input

        import json
        print (json.dumps(i, indent=2))

        return {'return':0}

    ############################################################
    def prepare(self, i):
        """
        Prepare cache entry

        Input:
          i (dict): unified CM input
            * (artifact) (str): cache name
            * (artifact_prefix) (str): add prefix to cache entry for readability
            * (tags) (str): cache tags
            * (cache_meta) (dict): extra cache meta
            * (renew) (bool): renew in existing cache entry
            * (new) (bool): create new cache entry
            * (quiet) (bool): if True, select 0
            * (version) (str): prune by version
            * (version_min) (str): prune by version_min
            * (version_max) (str): prune by version_max

        Output:
          r (dict): unified CM output
            * return (int): 0 if success
            * (error) (str): error string if return > 0

            * path (str): path to prepared cache entry
            * meta (dict): meta of the prepared cache entry
            * (output) (dict): output if finalized cache
        """

        import copy

        ###################################################################
        # Process input

        out = i['control'].get('out', '')
        console = out == 'con'
        _input = i['control'].get('_input', {})

        tags = _input.pop('tags', '')
        extra_cache_meta = _input.pop('cache_meta', {})
        renew = _input.pop('renew', False)
        new = _input.pop('new', False)
        quiet = _input.pop('quiet', False)
        artifact_prefix = _input.pop('artifact_prefix', None)

        version_min = _input.pop('version_min', '')
        if version_min != '':
            version_min2 = [utils.digits(v) for v in version_min.split('.')]

        version_max = _input.pop('version_max', '')
        if version_max != '':
            version_max2 = [utils.digits(v) for v in version_max.split('.')]

        force_version = _input.pop('version', '')

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        automation = i['automation']
        artifact = i.get('artifact', '')

        # Attempt to search if exists
        ii = {'action':'find',
              'automation':automation}
        if artifact != '': ii['artifact'] = artifact
        if tags != '': ii['tags'] = tags + ',-tmp'

        ii_copy = copy.deepcopy(ii)

        if not new:
            r = self.cmind.x(ii)
            if r['return'] >0: return self.cmind.embed_error(r)

            lst = r['list']
        else:
            lst = []

        rr = {'return':0}

        # Prune by version if needed
        if len(lst) > 0 and (version_min != '' or version_max != '' or force_version != ''):
            pruned_lst = [] 
            for l in lst:
                version = l.meta.get('version', '')

                passed_version_check = True
                if version_min != '' or version_max != '':
                    version2 = [utils.digits(v) for v in version.split('.')]

                    if version_min != '' and version2 < version_min2:
                        passed_version_check = False
                    if version_max != '' and version2 > version_max2:
                        passed_version_check = False
                    if force_version != '' and force_version != version:
                        passed_version_check = False

                if passed_version_check:
                    pruned_lst.append(l)

            lst = pruned_lst

        # Select
        if len(lst) > 1:
            text = f"More than 1 entry found in cache for tags \"{ii['tags']}\". Please select"

            select_lst = []
            for l in lst:
                xtags = l.meta.get('tags', [])

                uid = l.meta.get('uid', '')

                version = l.meta.get('version', '')

                x = ','.join(xtags)
                if version != '': x += f' (Version {version})'
                x += f' [{uid}]'

                version2 = [utils.digits(v) for v in version.split('.')]

                select_lst.append({'cmx_obj':l,
                                   'text': x,
                                   'version': version,
                                   'version2': version2})

            select_lst = sorted(select_lst, key = lambda x: x['version2'], reverse = True)

            select_lst2 = []
            for l in select_lst:
                select_lst2.append(l['text'])

            r = self.cmind.x({'automation': self.meta['use']['flex.common'],
                              'action': 'select_from_list',
                              'text': text,
                              'list': select_lst2,
                              'quiet': quiet,
                              'control':{'out':out}})
            if r['return']>0: return self.cmind.embed_error(r)

            index = r['index']

            lst = [select_lst[index]['cmx_obj']]

        # Continue
        if len(lst) == 0:
            # Didn't find completed artifacts, search for unfinished ones 
            # (that failed and we need to rerun them)
            ii = copy.deepcopy(ii_copy)
            ii['tags'] = tags + ',tmp'

            r = self.cmind.x(ii)
            if r['return'] >0: return self.cmind.embed_error(r)

            lst = r['list']

            if len(lst) > 1:
                paths = ''
                for l in lst:
                    paths += l.path + '\n'

                return self.cmind.prepare_error(1, 'More than 1 temporal entry found in cache for tags "{}" - delete some:\n{}'.format(i['tags'], paths))

            elif len(lst) == 1:
                cache_obj = lst[0]

                cache_path = cache_obj.path
                cache_meta = cache_obj.meta
            else:
                # No temporal cache entries found, create temporal one
                ii = copy.deepcopy(ii_copy)
                ii['action'] = 'add'
                ii['tags'] = tags + ',tmp'
                ii['meta'] = extra_cache_meta

                if ii.get('artifact', '') == '':
                    ii['artifact'] = '' if (artifact_prefix == '' or artifact_prefix == None) else artifact_prefix + '-'

                    rx = utils.gen_uid()
                    ii['artifact'] += rx['uid'] + ',' + rx['uid']

                r = self.cmind.x(ii)
                if r['return'] >0: return self.cmind.embed_error(r)

                cache_path = r['path']
                cache_meta = r['meta']

        else:
            # Found cached entry
            cache_obj = lst[0]

            cache_path = cache_obj.path
            cache_meta = cache_obj.meta

            if not renew:
                output = {'return':0}
                output_path = os.path.join(cache_path, self.CMX_OUTPUT_FILE)

                if os.path.isfile(output_path):
                    r = utils.load_json(file_name = output_path)
                    if r['return'] >0: return self.cmind.embed_error(r)

                    output = r['meta']

                rr['output'] = output

        # Check log
        self.cmind.log(f"flex.cache: prepared path {cache_path}", "info")

        # Finish output
        rr['path'] = cache_path
        rr['meta'] = cache_meta

        return rr

    ############################################################
    def finish(self, i):
        """
        Finish cache entry

        Input:
          i (dict): unified CM input
            * (artifact) (str)
            * (output) (dict): record to cmx-output.json
            * (cache_meta) (dict): extra cache meta
            * (cache_tags) (list): extra cache tags
            * (extra_cmx_output_file) (str): if !='' record output to this file too
                                             useful for external storage for results, datasets, models
                                            that are referenced by flex.cache

        Output:
          r (dict): unified CM output
            * return (int): 0 if success
            * (error) (str): error string if return > 0
        """

        ###################################################################
        # Process input

        console = i['control'].get('out', '') == 'con'
        _input = i['control'].get('_input', {})

        output = _input.pop('output', {})
        cache_meta = _input.pop('cache_meta', {})
        cache_tags = _input.pop('cache_tags', '')
        extra_cmx_output_file = _input.pop('extra_cmx_output_file', '')

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        automation = i['automation']
        artifact = i.get('artifact', '')

        ii = {'action':'load',
              'automation':automation,
              'artifact':artifact
              }

        r = self.cmind.x(ii)
        if r['return'] >0: return self.cmind.embed_error(r)

        path = r['path']
        meta = r['meta']

        if len(cache_meta)>0:
            meta.update(cache_meta)

        tags = meta.get('tags', [])

        if 'tmp' in tags: tags.remove('tmp')

        if cache_tags != '': 
            for tag in cache_tags.split(','):
                if tag not in tags:
                    tags.append(tag)

        # Check version
        if 'version' in meta:
            version = meta.get('version', '')
            tags = [tag for tag in tags if not tag.startswith('_version.')]
            tags.append(f'_version.{version}')

        meta['tags'] = tags

        ii = {'action':'update',
              'automation':automation,
              'artifact':artifact,
              'meta':meta,
              'replace':True
             }

        rr = self.cmind.x(ii)
        if rr['return'] >0: return cmind.embed_error(rr)

        output_path = os.path.join(path, self.CMX_OUTPUT_FILE)

        r = utils.save_json(file_name = output_path, meta = output)
        if r['return'] >0: return cmind.embed_error(r)

        if extra_cmx_output_file != '' and extra_cmx_output_file != None:
            r = utils.save_json(file_name = extra_cmx_output_file, meta = output)
            if r['return'] >0: return cmind.embed_error(r)

        return rr


    ############################################################
    def show(self, i):
        """
        Show cache entries

        Input:
          i (dict): unified CM input
            * (artifact) (str)
            * (tags) (str)

        Output:
          r (dict): unified CM output
            * return (int): 0 if success
            * (error) (str): error string if return > 0
            * (list) (list): list of CMX cache objects
        """

        import copy

        ###################################################################
        # Process input

        console = i['control'].get('out', '') == 'con'

        _input = i['control'].get('_input', {})

        tags = _input.pop('tags', '')

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        automation = i['automation']
        artifact = i.get('artifact', '')

        # Attempt to search if exists
        ii = {'action':'find',
              'automation':automation}
        if artifact != '': ii['artifact'] = artifact
        if tags != '': ii['tags'] = tags

        ii_copy = copy.deepcopy(ii)

        r = self.cmind.x(ii)
        if r['return'] >0: return self.cmind.embed_error(r)

        lst = r['list']

        if console:
            for l in lst:
                path = l.path
                uid = l.meta['uid']
                xtags = l.meta.get('tags', [])
                version = l.meta.get('version', '')

                print ('')

                x = ','.join(xtags)
                if version != '': x += f' (Version {version})'
                x += f' [{uid}]'
                print (x)
                print (f'  {path}')

        return r

    ############################################################
    def clean(self, i):
        """
        Clean tmp flex.cache entries

        Input:
          i (dict): unified CM input
            * (artifact) (str)
            * (tags) (str)
            * (f) (bool): force remove

        Output:
          r (dict): unified CM output
            * return (int): 0 if success
            * (error) (str): error string if return > 0
            * (list) (list): list of CMX cache objects
        """

        import copy

        ###################################################################
        # Process input

        console = i['control'].get('out', '') == 'con'

        _input = i['control'].get('_input', {})

        tags = _input.pop('tags', '')
        if tags != '': tags += ','
        tags += 'tmp'

        force = _input.pop('f', False)

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        automation = i['automation']
        artifact = i.get('artifact', '')

        # Attempt to search if exists
        ii = {'action':'rm',
              'automation':automation,
              'control':{}}
        if artifact != '': ii['artifact'] = artifact
        if tags != '': ii['tags'] = tags
        if console: ii['control']['out'] = 'con'
        if force: ii['force'] = True
        ii_copy = copy.deepcopy(ii)

        return self.cmind.x(ii)

