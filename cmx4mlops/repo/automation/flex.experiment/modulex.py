# Author and developer: Grigori Fursin

import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    Automation actions
    """

    CMX_RESULT_FILE = 'cmx-result.json'
    CMX_RESULT_SUMMARY_FILE = 'cmx-result-summary.json'
    CMX_RESULT_SUMMARY_KEYS_FILE = 'cmx-result-summary-keys.json'
    CMX_INPUT_FILE = 'cmx-input.json'
    CMX_INPUT_STEP_FILE = 'cmx-input-step.json'
    CMX_OUTPUT_FILE = 'cmx-output.json'

    line1 = '='*60
    line2 = '*'*60

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
    def add(self, i):
        """
        Find or add experiment

        Args:
          i (dict): CMX dict

            (artifact) (str): artifact forces CM artifact name
            (name) (str): name goes into tags while creating CM artifact name as {datetime}.name.{UID}
            (skip_name) (bool): if True and console, don't ask for name
            (name_date) (bool): if True, use datetime as name
            (tags) (list): user-friendly tags separated by comma
            (dir) (str): sub-directory
            (step) (str): experiment step
            (rerun) (bool): if True, rerun experiment instead of creating a new one
            (quiet) (bool): if True, minimize questions
            (use_uid) (bool): if True and artifact == '' then artifact == UID instead of current date
            (fail_if_not_found) (bool): if True, fail if experiment is not found
            (input_copy) (dict): copy of input if called from `run` function
            (do_not_add_dummy_step) (bool): if True, do not add dummy result

        """

        import copy

        # Check input
        console = i['control'].get('out', '') == 'con'

        _input = i['control'].get('_input', {})

        tags = _input.pop('tags', '').strip()
        use_uid = _input.pop('use_uid', False)
        name = _input.pop('name', '')
        skip_name = _input.pop('skip_name', False)
        name_date = _input.pop('name_date', False)
        quiet = _input.pop('quiet', False)
        fail_if_not_found = _input.pop('fail_if_not_found', False)
        datetime = _input.pop('dir', '')
        step = _input.pop('step', '')
        rerun = _input.pop('rerun', False)
        input_copy = _input.pop('input_copy', {})
        do_not_add_dummy_step = _input.pop('do_not_add_dummy_step', False)

        dummy_meta  = _input.pop('meta', {})
        dummy_replace = _input.pop('replace', False)

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        # Separate artifact(s) into name and repo
        r = utils.process_input(i)
        if r['return']>0: return self.cmind.embed_error(r)

        automation = i['automation']
        artifact = i.get('artifact', '')

        artifact_decomposed = i['control'].get('_artifact', {})
        artifact_name = artifact_decomposed.get('name', '') # can be alias | uid | alias,uid
        artifact_repo = artifact_decomposed.get('repo', '') # can be alias | uid | alias,uid

        # If we are in the creation mode (and not reply or search)
        # and artifact=='' and name=='', ask for name
        if not fail_if_not_found and artifact_name == '' and name == '' and not skip_name and not name_date and console:
            print ('')
            name = input ('Enter experiment name or press Enter to use {datetime}: ')
            name = name.strip()

        if artifact_name == '' and name == '' and name_date:
            # Get default experiment artifact name (date)
            r = self.cmind.x({'action':'get_date_time',
                              'automation':self.meta['use']['flex.common']})
            if r['return']>0: return self.cmind.embed_error(r)

            artifact_name = r['date_str'].replace('-','')

        if tags == '':
            if artifact_name != '':
               tags = ','.join(artifact_name.split('-'))
            elif name != '':
               tags = ','.join(name.split('-'))

        if name != '':
            if tags != '':
                tags += ','
            tags += name

        # Attempt to search if exist
        ii = {'control':{'common':True},
              'action':'find',
              'automation':automation}
        if artifact != '': ii['artifact'] = artifact
        if tags != '': ii['tags'] = tags

        ii_copy = copy.deepcopy(ii)

        r = self.cmind.x(ii)
        if r['return'] >0: return self.cmind.embed_error(r)

        lst = r['list']

        # If not found, create
        if len(lst)>1:
            print ('')
            print ('More than 1 experiment artifact found:')

            lst = sorted(lst, key=lambda x: x.path)

            print ('')
            num = 0
            for e in lst:
                print (f'{num}) {e.path}')
                print ('     (all tags: {})'.format(','.join(e.meta.get('tags',[]))))
                num += 1

            if not console:
                return self.cmind.prepare_error(1, 'more than 1 experiment artifact found')

            print ('')
            x = input('Make your selection or press Enter for 0: ')

            x = x.strip()
            if x == '': x = '0'

            selection = int(x)

            if selection < 0 or selection >= num:
                selection = 0

            experiment_obj = lst[selection]

        elif len(lst)==1:
            experiment_obj = lst[0]

        else:
            if fail_if_not_found:
                return self.cmind.prepare_error(1, 'experiment was not found')

            # Create new entry
            ii = copy.deepcopy(ii_copy)
            ii['action'] = 'add'

            if artifact_name == '' and not use_uid:
               r = self.cmind.x({'action':'get_date_time',
                                 'automation':self.meta['use']['flex.common']})
               if r['return']>0: return self.cmind.embed_error(r)

               cm_artifact = r['date_str'].replace('-','')

               r = utils.gen_uid()
               if r['return']>0: return self.cmind.embed_error(r)
               experiment_uid = r['uid']

               if name != '':
                   cm_artifact += '.' + name

#               cm_artifact += '.' + experiment_uid + ',' + experiment_uid
               cm_artifact += ',' + experiment_uid

               if artifact_repo !='' : cm_artifact = artifact_repo + ':' + cm_artifact

               ii['artifact'] = cm_artifact

            r = self.cmind.x(ii)
            if r['return'] > 0: return self.cmind.embed_error(r)

            # Reload 
            experiment_uid = r['meta']['uid']

            r = self.cmind.x({'action':'find',
                              'automation':automation,
                              'artifact':experiment_uid})
            if r['return']>0: return self.cmind.embed_error(r)

            lst = r['list']
            if len(lst)==0 or len(lst)>1:
                return self.cmind.prepare_error(1, f'created experiment artifact with UID {experiment_uid} but can\'t find it - weird')

            experiment_obj = lst[0]

        # Print experiment folder
        experiment_path = experiment_obj.path

        if console:
            print ('')
            print ('Path to the CM experiment artifact: {}'.format(experiment_path))


        # Get directory with datetime
        if datetime == '' and rerun:
            # Check if already some dir exist
            directories = os.listdir(experiment_path)

            datetimes = sorted([f for f in directories if os.path.isfile(os.path.join(experiment_path, f, self.CMX_INPUT_FILE))], reverse=True)

            if len(datetimes)==1:
                datetime = datetimes[0]

            elif len(datetimes)>1:
                selection = 0

                if not quiet:
                    print ('')
                    print ('Select experiment:')

                    num = 0
                    print ('')
                    for d in datetimes:
                        print ('{}) {}'.format(num, d))
                        num += 1

                    if not console:
                        return self.cmind.prepare_error(1, 'more than 1 experiment found.\nPlease rerun with --dir={date and time}"')

                    print ('')
                    x = input('Make your selection or press Enter for 0: ')

                    x = x.strip()
                    if x == '': x = '0'

                    selection = int(x)

                    if selection < 0 or selection >= num:
                        selection = 0
                else:
                    print ('')
                    print (f'Selected experiment: {datetimes[0]}')

                datetime = datetimes[selection]

        if datetime != '':
            experiment_path2 = os.path.join(experiment_path, datetime)
        else:
            num = 0
            found = False

            while not found:
                r = self.cmind.x({'action':'get_date_time',
                                  'automation':self.meta['use']['flex.common']})
                if r['return']>0: return self.cmind.embed_error(r)

                datetime = r['date_time_str'].replace('-','')

                if num>0:
                    datetime += '.' + str(num)

                experiment_path2 = os.path.join(experiment_path, datetime)

                if not os.path.isdir(experiment_path2):
                    found = True
                    break

                num+=1

        # Check/create directory with date_time
        if not os.path.isdir(experiment_path2):
            os.makedirs(experiment_path2)

        # Change current path
        if console:
            print ('Path to experiment: {}'.format(experiment_path2))

        # Record CMX input
        experiment_input_file = os.path.join(experiment_path2, self.CMX_INPUT_FILE)

        experiment_output_summary_file = os.path.join(experiment_path2, self.CMX_RESULT_SUMMARY_FILE)
        experiment_output_summary_keys_file = os.path.join(experiment_path2, self.CMX_RESULT_SUMMARY_KEYS_FILE)

        if not os.path.isfile(experiment_input_file) or rerun:
            r = utils.gen_uid()
            if r['return']>0: return self.cmind.embed_error(r)
            main_uid_str = r['uid']

            r = utils.save_json(file_name = experiment_input_file, 
                                meta = {'input': input_copy, 'uid': main_uid_str})

        # Prepare experiment step and possibly result dummy
        if not do_not_add_dummy_step:
            stepx = 1 if step == '' else int(step)

            r = prepare_experiment_step(self.cmind, 
                                        stepx, 
                                        experiment_path2, 
                                        self.CMX_INPUT_STEP_FILE,
                                        self.CMX_RESULT_FILE,
                                        rerun = rerun)
            if r['return'] >0: return self.cmind.embed_error(r)


        return {'return': 0, 'experiment_obj': experiment_obj, 
                             'experiment_path': experiment_path, 
                             'experiment_path2': experiment_path2,
                             'experiment_input_file': experiment_input_file,
                             'experiment_output_summary_file': experiment_output_summary_file,
                             'experiment_output_summary_keys_file': experiment_output_summary_keys_file}


    ############################################################
    def rerun(self, i):
        """
        Rerun experiment instead of creating a new directory

        """

        i['action'] = 'run'
        i['rerun'] = True

        return self.cmind.x(i)

    ############################################################
    def run(self, i):
        """
        Run experiment

        Args:
          i (dict): CMX input

            (rerun) (bool): if True, rerun experiment instead of creating a new one
            (artifact) (str)
            (name) (str)
            (skip_name) (bool): if True and console, don't ask for name
            (name_date) (bool): if True, use datetime as name
            (quiet) (bool): if True, minimize questions
            (tags) (list)
            (dir) (str): sub-directory

            (cmd) (str): CMD to run
            (env) (dict): extra ENV vars to pass before CMD
            (cmx_input) (dict): run CMX automation instead of CMD

            (explore) (dict): exploration parameters

            (clean_summary) (bool): if True, remove cmx-result-summary.json and cmx-result-summary-keys.json

        """

        import copy
        import itertools
        import math
        import time
        import json

        # Check input
        r = utils.process_input(i)
        if r['return']>0: return self.cmind.embed_error(r)

        i_copy = copy.deepcopy(i)

        out = i['control'].get('out', '')
        console = (out == 'con')

        artifact = i.get('artifact', '')
        automation = i['automation']

        _input = i['control'].get('_input', {})

        name = _input.pop('name', '').strip()
        skip_name = _input.pop('skip_name', False)
        name_date = _input.pop('name_date', False)
        tags = _input.pop('tags', '').strip()
        rerun = _input.pop('rerun', False)
        datetime = _input.pop('dir', '')
        quiet = _input.pop('quiet', False)

        cmd = _input.pop('cmd', '')
        env = _input.pop('env', {})
        cmx_input = _input.pop('cmx_input', {})

        explore = _input.pop('explore', {})

        clean_summary = _input.pop('clean_summary', False)

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        # Save current directory
        cur_dir = os.getcwd()


        # Find or add experiment artifact
        ii = {'control': {'out':out},
              'action': 'add',
              'automation': automation,
              'do_not_add_dummy_step': True}
        if artifact != '': ii['artifact'] = artifact
        if name != '': ii['name'] = name
        if tags != '': ii['tags'] = tags
        if rerun: ii['rerun'] = True
        if skip_name: ii['skip_name'] = True
        if name_date: ii['name_date'] = True
        if quiet: ii['quiet'] = True

        r = self.cmind.x(ii)
        if r['return'] >0 : return self.cmind.embed_error(r)

        experiment_obj = r['experiment_obj']
        experiment_path = r['experiment_path']
        experiment_path2 = r['experiment_path2']
        experiment_input_file = r['experiment_input_file']
        experiment_output_summary_file = r['experiment_output_summary_file']
        experiment_output_summary_keys_file = r['experiment_output_summary_keys_file']

        if clean_summary:
            for filename in [experiment_output_summary_file, experiment_output_summary_keys_file]:
                if os.path.isfile(filename):
                    os.remove(filename)

        # Prepare exploration
        # Note that from Python 3.7, dictionaries are ordered so we can define order for exploration in json/yaml
        # ${{VARS}} ${{ABC(range(1,2,3))}}

        cmd_orig = cmd

        if len(cmx_input)>0:
            cmx_input_copy = copy.deepcopy(cmx_input)
        else:
            r = extract_exploration_expression(cmd, explore)
            if r['return'] >0: return self.cmind.embed_error(r)
            cmd = r['string']

        # Separate Design Space Exploration into var and range
        explore_keys = []
        explore_dimensions = []

        for k in explore:
            v = explore[k]

            explore_keys.append(k)

            if type(v)!=list:
                v=eval(v)

            explore_dimensions.append(v)

        # Next command will run all iterations so we need to redo above command once again
        step = 0

        steps = itertools.product(*explore_dimensions)

        num_steps = len(list(steps))

        steps = itertools.product(*explore_dimensions)

        ii_copy = copy.deepcopy(ii)

        for dimensions in steps:

            step += 1

            print (self.line1)
            print ('Experiment step: {} out of {}'.format(step, num_steps))

            print ('')

            env_step = copy.deepcopy(env)

            l_dimensions=len(dimensions)
            if l_dimensions>0:
                print ('  Updating variables during exploration:')

                print ('')
                for j in range(l_dimensions):
                    v = dimensions[j]
                    k = explore_keys[j]
                    print ('    - Dimension {}: "{}" = {}'.format(j, k, v))

                    env_step[k] = str(v)

                print ('')


            r = prepare_experiment_step(self.cmind,
                                        step,
                                        experiment_path2,
                                        self.CMX_INPUT_STEP_FILE,
                                        self.CMX_RESULT_FILE,
                                        skip_dummy_input = True,
                                        rerun = rerun)
            if r['return'] >0: return self.cmind.embed_error(r)

            experiment_path3 = r['experiment_path3']
            experiment_step_input_file = r['experiment_step_input_file']
            experiment_result_file = r['experiment_result_file']

            # Update {{}} in CMD
            if len(cmx_input)>0:
                cmx_input_step = copy.deepcopy(cmx_input_copy)

                for key in env_step:
                    value = env_step[k]

                    if '.' in key:
                       keys = key.split('.')
                       new_cmx_input_step = cmx_input_step

                       first = True

                       for key in keys[:-1]:
                           if first:
                               key = key.replace('-','_')
                               first = False

                           if key not in new_cmx_input_step:
                              new_cmx_input_step[key] = {}
                           new_cmx_input_step = new_cmx_input_step[key]

                       new_cmx_input_step[keys[-1]]=value
                    else:
                       key = key.replace('-','_')
                       cmx_input_step[key] = value


            else:
                env_step.update({'CD':cur_dir,
                                 'CMX_EXPERIMENT_STEP':str(step),
                                 'CMX_EXPERIMENT_PATH':experiment_path,
                                 'CMX_EXPERIMENT_PATH2':experiment_path2,
                                 'CMX_EXPERIMENT_PATH3':experiment_path3})

                r = process_cmd(cmd, env, env_step)
                if r['return']>0: return self.cmind.embed_error(r)

                cmd_step = r['cmd']

            # Prepare experiment step input
            r = utils.get_current_date_time({})
            if r['return']>0: return self.cmind.embed_error(r)

            current_datetime = r['iso_datetime']

            r = utils.gen_uid()
            if r['return']>0: return self.cmind.embed_error(r)
            uid_str = r['uid']

            import uuid
            meta = {'uid_step': uid_str, 'uuid_step': str(uuid.uuid4()), 'iso_datetime': current_datetime, 'exploration_step': step}

            if len(cmx_input)>0:
                meta['cmx_input_orig'] = cmx_input_copy
                meta['cmx_input'] = cmx_input_step
            else:
                meta['env'] = env_step
                meta['cmd_orig'] = cmd_orig
                meta['cmd'] = cmd

            if not os.path.isfile(experiment_step_input_file) or not rerun:
                r = utils.save_json(file_name = experiment_step_input_file, meta = meta)
                if r['return']>0: return self.cmind.embed_error(r)

            experiment_step_output_file = os.path.join(experiment_path3, self.CMX_OUTPUT_FILE)
            if os.path.isfile(experiment_step_output_file):
                os.remove(experiment_step_output_file)

            # Run CMD
            os.chdir(experiment_path3)

            if len(cmx_input)>0:
                print ('Generated CMX input:')
                print ('')
                print (json.dumps(cmx_input_step, indent=2))

            else:
                print ('Generated CMD:')
                print ('')
                print (cmd_step)

            print ('')
            print (self.line2)
            print ('Start experiment ...')
            print ('')

            # Prepare result
            result = {}
            if os.path.isfile(experiment_result_file):
                r = utils.load_json(experiment_result_file)
                if r['return']>0: return self.cmind.embed_error(r)
                result = r['meta']

            if len(cmx_input) == 0:
                cmx_input_step = {'action':'cmd',
                                  'automation':self.meta['use']['flex.common'],
                                  'env':env_step,
                                  'cmd':cmd_step,
                                  'timeout':None}

            experiment_step_input_raw_file = experiment_step_input_file[:-5] + '-raw.json'
            if not os.path.isfile(experiment_step_input_raw_file) or not rerun:
                r = utils.save_json(file_name = experiment_step_input_raw_file, meta = cmx_input_step)
                if r['return']>0: return self.cmind.embed_error(r)

            ############################################################################################
            # Run

            start_time = time.time()

            r = {}

            try:
                r = self.cmind.x(cmx_input_step)

                returncode = r['return']
                stdout = ''
                stderr = ''

                if returncode>0: stderr = r['error']

            except Exception as e:
                returncode = 99
                stdout = ''
                stderr = format(e)

            if returncode > 0:
                print (self.line1)
                print (f'CMX ERROR inside automation (possibly third-party):\n{stderr}')

            if len(cmx_input) > 0 and not r.get('use_raw_experiment_output_file', False):
                result.update(r)

            runtime = time.time() - start_time

            # Update current result with some output if exists
            if os.path.isfile(experiment_step_output_file):
                r = utils.load_json(file_name = experiment_step_output_file)
                if r['return']>0: return self.cmind.prepare_error(1, f'problem loading file {experiment_step_output_file}: ' + r['error'])

                utils.merge_dicts({'dict1':result, 'dict2':r['meta'], 'append_lists':True, 'append_unique':True})

            # Add extra info to the result
            result['cmx_return_code'] = returncode
            result['cmx_elapsed_time' ] = runtime

            if stderr != '' and stderr != None:
                result['stderr'] = stderr

            r = utils.gen_uid()
            if r['return']>0: return self.cmind.embed_error(r)
            result['uid_step'] = r['uid']

            r = utils.get_current_date_time({})
            if r['return']>0: return self.cmind.embed_error(r)

            result['iso_datetime'] = r['iso_datetime']
            result['uuid_step'] = str(uuid.uuid4())
            result['exploration_step'] = step

            # Merge results with externally created file
            r = utils.save_json(file_name = experiment_result_file, meta = result)
            if r['return']>0: return self.cmind.embed_error(r)

            # Check summary file
            summary = []

            if os.path.isfile(experiment_output_summary_file):
                r = utils.load_json(experiment_output_summary_file)
                if r['return']>0: return cmind.embed_error(r)

                summary = r['meta']

            flat_result = {}
            utils.flatten_dict(result, flat_result)

            summary.append(flat_result)

            r = utils.save_json(experiment_output_summary_file, summary)
            if r['return']>0: return cmind.embed_error(r)

            r = self.cmind.x({'action': 'summarize_keys',
                              'automation': self.meta['use']['flex.common'],
                              'summary':summary})
            if r['return']>0: return cmind.embed_error(r)

            keys = r['keys']

            r = utils.save_json(experiment_output_summary_keys_file, keys)
            if r['return']>0: return cmind.embed_error(r)

            print ('')
            print ('Stop experiment ...')
            print ('')

        rr = {'return':0,
              'experiment_path':experiment_path,
              'experiment_path2':experiment_path2}

        return rr


    ############################################################
    def replay(self, i):
        """
        Replay experiment

        (uid) (str): find experiment by UID

        (artifact) (str)
        (tags) (list)
        (dir) (str): sub-directory
        (step) (str): experiment step
        """

        import copy
        import json
        import time

        # Check input
        r = utils.process_input(i)
        if r['return']>0: return self.cmind.embed_error(r)

        i_copy = copy.deepcopy(i)

        out = i['control'].get('out', '')
        console = (out == 'con')

        artifact = i.get('artifact', '')
        automation = i['automation']

        _input = i['control'].get('_input', {})

        tags = _input.pop('tags', '').strip()
        datetime = _input.pop('dir', '')
        uid = _input.pop('uid', '')
        step = _input.pop('step', '')

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        # Find or add experiment artifact
        input_path = ''
        input_meta = {}

        # Find inputs from steps
        if uid != '':
            ii = {'action':'find',
                  'automation':automation}
            if artifact != '': ii['artifact'] = artifact
            if tags != '': ii['tags'] = tags

            r = self.cmind.x(ii)
            if r['return'] >0 : return self.cmind.embed_error(r)

            lst = r['list']

            for l in lst:
                experiment_path = l.path

                directories = os.listdir(experiment_path)

                datetimes = sorted([f for f in directories if os.path.isfile(os.path.join(experiment_path, f, self.CMX_INPUT_FILE))], reverse=True)

                for d in datetimes:
                    r = self._find_uid({'path':experiment_path, 'datetime':d, 'uid':uid})
                    if r['return']>0: return self.cmind.embed_error(r)

                    if r.get('input_found', False):
                        input_path = r['input_path']
                        input_meta = r['input_meta']
                        break


        else:
            ii = {'control':{'out':out},
                  'action':'add',
                  'automation':automation,
                  'rerun':True,
                  'do_not_add_dummy_step': True,
                  'fail_if_not_found': True}
            if artifact != '': ii['artifact'] = artifact
            if tags != '': ii['tags'] = tags

            r = self.cmind.x(ii)
            if r['return']>0: return self.cmind.embed_error(r)

            experiment_obj = r['experiment_obj']
            experiment_path = r['experiment_path']
            experiment_path2 = r['experiment_path2']

            datetime = os.path.basename(experiment_path2)

            # Check steps
            r = self._find_uid({'path':experiment_path, 'datetime':datetime, 'step': step})
            if r['return']>0: return self.cmind.embed_error(r)

            if r.get('input_found', False):
                input_path = r['input_path']
                input_meta = r['input_meta']

        if input_path == '' or not os.path.isfile(input_path):
            return self.cmind.prepare_error(1, 'couldn\'t find input path')


        # Final info
        if console:
            print ('')
            print ('Path to experiment: {}'.format(input_path))

        # Attempt to load cm-input.json
        experiment_input_file = input_path

        if console:
            print ('')
            print ('Experiment input:')
            print ('')
            print (json.dumps(input_meta, indent=2))
            print ('')

        experiment_path3 = os.path.dirname(experiment_input_file)

        os.chdir(experiment_path3)

        # Check if CMX or CMD
        cmx_input = input_meta.get('cmx_input', {})

        if len(cmx_input) == 0:
            # Run experiment again
            cmd_orig = input_meta.get('cmd_orig', '')
            env_step = input_meta.get('env', {})

            r = process_cmd(cmd_orig, {}, env_step)
            if r['return']>0: return self.cmind.embed_error(r)

            cmd_step = r['cmd']

            # Run CMD
            print ('CMD:')
            print ('')
            print (cmd_step)
            print ('')
            print (self.line2)

            cmx_input = {'action':'cmd',
                         'automation':self.meta['use']['flex.common'],
                         'env':env_step,
                         'cmd':cmd_step,
                         'timeout':None}

        if len(cmx_input) > 0:
            start_time = time.time()

            print ('')
            print ('Start experiment ...')

            r = self.cmind.x(cmx_input)
            if r['return']>0: return self.cmind.embed_error(r)

            runtime = time.time() - start_time

            print ('')
            print ('Stop experiment ...')
            print ('')

            print ('')
            print ('Experiment output:')
            print ('')

            import json
            print (json.dumps(r, indent=2))

            # TBA - validate experiment, perform stat. analysis, learn, etc ...

        return {'return':0}

    ############################################################
    def _find_uid(self, i):
        """
        Find experiment result with a given UID

        Args:
          (CM input dict): 

            path (str): path to experiment artifact
            datetime (str): sub-path to experiment
            (uid) (str): experiment UID
            (step) (str): experiment step
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          path_to_file (str): path to experiment result file
          meta (dict): complete list of all results
          result (dict): result dictionary with a given UID
        """

        path = i['path']
        datetime = i['datetime']
        uid = i.get('uid', '').strip()
        step = i.get('step', '')

        rr = {'return':0}

        # Now checking 'step-X' directories

        path_to_experiment2 = os.path.join(path, datetime)

        directories = os.listdir(path_to_experiment2)

        step_min = 0
        step_max = 0

        input_found = False

        for path in directories:

            if not path.startswith('step-'):
                continue

            path1 = os.path.join(path_to_experiment2, path)

            if os.path.isdir(path1):
                path_to_experiment_input_step_file = os.path.join(path1, self.CMX_INPUT_STEP_FILE)

                if os.path.isfile(path_to_experiment_input_step_file):
                    try:
                        stepx = int(path[5:])
                    except ValueError:
                        stepx = 0

                    if step_min == 0: step_min = stepx
                    if stepx < step_min: step_min = stepx

                    if step_max == 0: step_max = stepx
                    if stepx > step_max: step_max = stepx

                    if uid != '':
                        r = utils.load_json(file_name = path_to_experiment_input_step_file)
                        if r['return']>0: return self.cmind.embed_error(r)

                        meta = r['meta']

                        if meta.get('uid_step','') == uid :
                            input_found = True
                            rr['input_path'] = path_to_experiment_input_step_file
                            rr['input_meta'] = meta
                            break


        rr['step_min'] = step_min
        rr['step_max'] = step_max

        if not input_found and uid == '' and step_max > 0:
            steps = step_max - step_min + 1

            if step != '':
                step = int(step.strip())
            else:
                step = 0

                if steps == 1:
                    step = 1
                else:

                    print ('')
                    x = input (f'Found {steps} steps. Please select a step or press Enter to select step 1: ')
                    x = x.strip()

                    if x == '':
                        step = 1
                    else:
                        step = int(x)

                    if step < step_min or step > step_max:
                        return self.cmind.prepare_error(1, 'wrong step selected')


            path1 = os.path.join(path_to_experiment2, 'step-' + str(step))
            path_to_experiment_input_step_file = os.path.join(path1, self.CMX_INPUT_STEP_FILE)

            if os.path.isfile(path_to_experiment_input_step_file):
                r = utils.load_json(file_name = path_to_experiment_input_step_file)
                if r['return']>0: return self.cmind.embed_error(r)

                meta = r['meta']

                input_found = True
                rr['input_path'] = path_to_experiment_input_step_file
                rr['input_meta'] = meta

        if input_found:
            rr['input_found'] = True

        return rr


    ############################################################
    def get(self, i):
        """
        Get flex.experiment

        Args:
          i (dict): CMX dict

            (artifact) (str): artifact forces CM artifact name
            (name) (str): name goes into tags while creating CM artifact name as {datetime}.name.{UID}
            (name_date) (bool): if True, use datetime as name
            (tags) (list): user-friendly tags separated by comma
            (dir) (str): sub-directory
            (step) (str): experiment step
            (only_files) (bool): if True, return only files with results

        """

        # Check input
        console = i['control'].get('out', '') == 'con'

        _input = i['control'].get('_input', {})

        tags = _input.pop('tags', '').strip()
        name_date = _input.pop('name_date', False)
        datetime = _input.pop('dir', '')
        step = _input.pop('step', '')
        only_files = _input.pop('only_files', False)

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        # Separate artifact(s) into name and repo
        r = utils.process_input(i)
        if r['return']>0: return self.cmind.embed_error(r)

        automation = i['automation']
        artifact = i.get('artifact', '')

        # Search for flex.experiments
        ii = {'control':{'common':True},
              'action':'find',
              'automation':automation}
        if artifact != '': ii['artifact'] = artifact
        if tags != '': ii['tags'] = tags

        r = self.cmind.x(ii)
        if r['return'] >0: return self.cmind.embed_error(r)

        lst = r['list']

        summary = []
        files = []

        for l in lst:
            experiment_path = l.path

            directories = os.listdir(experiment_path)

            datetimes = sorted([f for f in directories if os.path.isfile(os.path.join(experiment_path, f, self.CMX_INPUT_FILE))], reverse=True)

            for d in datetimes:
                experiment_path2 = os.path.join(experiment_path, d)

                experiment_output_summary_file = os.path.join(experiment_path2, self.CMX_RESULT_SUMMARY_FILE)

                if os.path.isfile(experiment_output_summary_file):
                    files.append(experiment_output_summary_file)

                    if not only_files:
                        r = utils.load_json(file_name = experiment_output_summary_file)
                        if r['return']>0: return cmind.embed_error(r)

                        summary += r['meta']


        return {'return':0, 'summary':summary, 'files': files}


############################################################
def prepare_experiment_step(cm,
                            step,
                            experiment_path2,
                            cmx_input_step_file,
                            cmx_result_file,
                            skip_dummy_input = False,
                            rerun = False):

    import math

    # Generate UID and prepare extra directory:
    r = utils.gen_uid()
    if r['return']>0: return r
    uid_str = r['uid']

#    length_num_steps = int(math.log10(num_steps))
    step_str = str(step)
#    datetime3 = 'step-' + '0'*(1 + length_num_steps - len(step_str)) + step_str
    datetime3 = 'step-' + step_str

    experiment_path3 = os.path.join(experiment_path2, datetime3)
    if not os.path.isdir(experiment_path3):
        os.makedirs(experiment_path3)

    # Record experiment input with possible exploration
    experiment_result_file = os.path.join(experiment_path3, cmx_result_file)

    # Get date time of experiment
    r = utils.get_current_date_time({})
    if r['return']>0: return r

    current_datetime = r['iso_datetime']

    # Change current path to step
    print ('Path to experiment step: {}'.format(experiment_path3))
    print ('')

    experiment_step_input_file = os.path.join(experiment_path3, cmx_input_step_file)

    if not skip_dummy_input:

        # Prepare dummy input file
        meta = {'env':{}, 'cmd':'dir', 'uid_step': uid_str, 'iso_datetime': current_datetime}

        if not os.path.isfile(experiment_step_input_file) or not rerun:
           r = utils.save_json(file_name = experiment_step_input_file, meta = meta)
           if r['return']>0: return r

        # Prepare dummy result file
        result = {}
        result['uid_step'] = uid_str
        result['iso_datetime'] = current_datetime

        r = utils.save_json(file_name = experiment_result_file, meta = result)
        if r['return']>0: return r

    return {'return':0, 'experiment_path3': experiment_path3,
                        'experiment_step_input_file': experiment_step_input_file,
                        'experiment_result_file': experiment_result_file}

############################################################
def process_cmd(cmd, env, env_step):

    cmd_step = cmd

    j = 1
    k = 0
    while j>=0:
       j = cmd_step.find('{{', k)
       if j>=0:
           k = j
           l = cmd_step.find('}}',j+2)
           if l>=0:
               var = cmd_step[j+2:l]

               # Such vars must be in env
               if var not in env and var not in env_step:
                   return {'return':1, 'error':'key "{}" is not in ENV during exploration'.format(var)}

               if var in env:
                   value = env[var]
               else:
                   value = env_step[var]

               cmd_step = cmd_step[:j] + str(value) + cmd_step[l+2:]

    return {'return':0, 'cmd': cmd_step}

############################################################
def extract_exploration_expression(string, explore):

    # Extract exploration expressions from {{VAR{expression}}}
    j = 1
    k = 0
    while j>=0:
       j = string.find('}}}', k)
       if j>=0:
           k = j+1

           l = string.rfind('{{',0, j)

           if l>=0:
               l2 = string.find('{', l+2, j)
               if l2>=0:
                   k = l2+1

                   var = string[l+2:l2]
                   expr = string[l2+1:j]

                   explore[var] = expr

                   string = string[:l2]+ string[j+1:]

    return {'return':0, 'string':string}
