import os
import itertools
import copy
import json

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    CM "experiment" automation actions
    """

    CM_RESULT_FILE = 'cm-result.json'
    CM_INPUT_FILE = 'cm-input.json'
    CM_OUTPUT_FILE = 'cm-output.json'
    
    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          automation (str): automation as CM string object

          parsed_automation (list): prepared in CM CLI or CM access function
                                    [ (automation alias, automation UID) ] or
                                    [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

          (artifact) (str): artifact as CM string object

          (parsed_artifact) (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action
        """

        import json
        print (json.dumps(i, indent=2))

        return {'return':0}


    
    
    
    ############################################################
    def run(self, i):
        """
        Run experiment

        Args:
          (CM input dict): 

            (out) (str): if 'con', output to console

            (artifact) (str): experiment artifact name (can include repository separated by :)
            (tags) (str): experiment tags separated by comma

            (dir) (str): force recording into a specific directory
            
            
            (script) (str): find and run CM script by name
            (s)

            (script_tags) (str): find and run CM script by tags
            (stags)

            (rerun) (bool): if True, rerun experiment in a given entry/directory instead of creating a new one...

            (explore) (dict): exploration dictionary

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action
        """

        # Copy of original input
        ii_copy = copy.deepcopy(i)
        cur_dir = os.getcwd()

        # Find or add artifact based on repo/alias/tags
        r = self._find_or_add_artifact(i)
        if r['return']>0: return r
        
        experiment = r['experiment']
        
        console = i.get('out','')=='con'
        
        # Print experiment folder
        experiment_path = experiment.path

        if console:
            print ('')
            print ('Path to CM experiment artifact: {}'.format(experiment_path))


        # Get directory with datetime
        datetime = i.get('dir','')

        if datetime == '' and i.get('rerun', False):
            # Check if already some dir exist

            directories = os.listdir(experiment_path)

            datetimes = sorted([f for f in directories if os.path.isfile(os.path.join(experiment_path, f, self.CM_RESULT_FILE))], reverse=True)

            if len(datetimes)==1:
                datetime = datetimes[0]
            elif len(datetimes)>1:
                print ('')
                print ('Select experiment:')

                datetimes = sorted(datetimes)
                
                num = 0
                print ('')
                for d in datetimes:
                    print ('{}) {}'.format(num, d.replace('.',' ')))
                    num += 1

                if not console:
                    return {'return':1, 'error':'more than 1 experiment found.\nPlease use "cm rerun experiment --dir={date and time}"'}

                print ('')
                x=input('Make your selection or press Enter for 0: ')

                x=x.strip()
                if x=='': x='0'

                selection = int(x)

                if selection < 0 or selection >= num:
                    selection = 0

                datetime = datetimes[selection]

        
        if datetime!='':
            experiment_path2 = os.path.join(experiment_path, datetime)
        else:
            num = 0
            found = False

            while not found:
                r = utils.get_current_date_time({})
                if r['return']>0: return r

                datetime = r['iso_datetime'].replace(':','-').replace('T','.')

                if num>0:
                    datetime+='.'+str(num)

                experiment_path2 = os.path.join(experiment_path, datetime)

                if not os.path.isdir(experiment_path2):
                    found = True
                    break

                num+=1

        # Check/create directory with date_time
        if not os.path.isdir(experiment_path2):
            os.makedirs(experiment_path2)

        # Change current path
        print ('Path to experiment: {}'.format(experiment_path2))

        os.chdir(experiment_path2)

        # Record experiment input with possible exploration
        experiment_input_file = os.path.join(experiment_path2, self.CM_INPUT_FILE)
        experiment_result_file = os.path.join(experiment_path2, self.CM_RESULT_FILE)

        # Clean original input
        for k in ['parsed_artifact', 'parsed_automation', 'cmd']:
            if k in ii_copy:
                del(ii_copy[k])

        r = utils.save_json(file_name=experiment_input_file, meta=ii_copy)
        if r['return']>0: return r
        
        # Prepare run command
        cmd = ''
        
        unparsed = i.get('unparsed_cmd', [])
        if len(unparsed)>0:
            for u in unparsed:
                if ' ' in u: u='"'+u+'"'
                cmd+=' '+u

            cmd=cmd.strip()

        # Prepare script run
        env = i.get('env', {})

        ii = {'action':'native-run',
              'automation':'script,5b4e0237da074764',
              'env':env}

        # Prepare exploration
        # Note that from Python 3.7, dictionaries are ordered so we can define order for exploration in json/yaml
        # ${{XYZ}} ${{ABC(range(1,2,3))}}
        
        # Extract exploration expressions from {{VAR{expression}}}
        explore = i.get('explore', {})

        j = 1
        k = 0
        while j>=0:
           j = cmd.find('}}}', k)
           if j>=0:
               k = j+1

               l = cmd.rfind('{{',0, j)

               if l>=0:
                   l2 = cmd.find('{', l+2, j)
                   if l2>=0:
                       k = l2+1

                       var = cmd[l+2:l2]
                       expr = cmd[l2+1:j]

                       explore[var] = expr

                       cmd = cmd[:l2]+ cmd[j+1:]

        
        # Separate Design Space Exploration into var and range
        explore_keys=[]
        explore_dimensions=[]

        for k in explore:
            v=explore[k]

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
            
            print ('================================================================')
            print ('Experiment step: {} out of {}'.format(step, num_steps))

            print ('')

            ii = copy.deepcopy(ii_copy)

            env = ii.get('env', {})

            l_dimensions=len(dimensions)
            if l_dimensions>0:
                print ('  Updating ENV variables during exploration:')

                print ('')
                for j in range(l_dimensions):
                    v = dimensions[j]
                    k = explore_keys[j]
                    print ('    - Dimension {}: "{}" = {}'.format(j, k, v))

                    env[k] = str(v)

                print ('')

            # Generate UID and prepare extra directory:
            r = utils.gen_uid()
            if r['return']>0: return r

            uid = r['uid']

            experiment_path3 = os.path.join(experiment_path2, uid)
            if not os.path.isdir(experiment_path3):
                os.makedirs(experiment_path3)

            # Get date time of experiment
            r = utils.get_current_date_time({})
            if r['return']>0: return r

            current_datetime = r['iso_datetime']

            # Change current path
            print ('Path to experiment step: {}'.format(experiment_path3))
            print ('')
            os.chdir(experiment_path3)

            # Prepare and run experiment in a given placeholder directory
            os.chdir(experiment_path3)
                    
            ii['env'] = env
            
            # Change only in CMD
            env_local={'CD':cur_dir,
                       'CM_EXPERIMENT_STEP':str(step),
                       'CM_EXPERIMENT_PATH':experiment_path,
                       'CM_EXPERIMENT_PATH2':experiment_path2,
                       'CM_EXPERIMENT_PATH3':experiment_path3}

            
            # Update {{}} in CMD
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
                       if var not in env and var not in env_local:
                           return {'return':1, 'error':'key "{}" is not in env during exploration'.format(var)}

                       if var in env:
                           value = env[var]
                       else:
                           value = env_local[var]

                       cmd_step = cmd_step[:j] + str(value) + cmd_step[l+2:]

            ii['command'] = cmd_step
                       
            print ('Generated CMD:')
            print ('')
            print (cmd_step)
            print ('')
            
            # Prepare experiment step input
            experiment_step_input_file = os.path.join(experiment_path3, self.CM_INPUT_FILE)

            r = utils.save_json(file_name=experiment_step_input_file, meta=ii)
            if r['return']>0: return r

            experiment_step_output_file = os.path.join(experiment_path3, self.CM_OUTPUT_FILE)
            if os.path.isfile(experiment_step_output_file):
                os.delete(experiment_step_output_file)

            # Run CMD
            rr=self.cmind.access(ii)
            if rr['return']>0: return rr

            # Record output
            result = {}

            if os.path.isfile(experiment_step_output_file):
                r = utils.load_json(file_name=experiment_step_output_file)
                if r['return']>0: return r

                result = r['meta']

                #Try to flatten
                try:
                    flatten_result = flatten_dict(result)
                    result = flatten_result
                except:
                    pass
            
            # Add extra info
            result['uid'] = uid
            result['iso_datetime'] = current_datetime

            # Attempt to append to the main file ...
            all_results = []

            if os.path.isfile(experiment_result_file):
                r = utils.load_json(file_name=experiment_result_file)
                if r['return']>0: return r

                all_results = r['meta']

            all_results.append(result)

            r = utils.save_json(file_name=experiment_result_file, meta = all_results)
            if r['return']>0: return r

        
        rr = {'return':0,
              'experiment_path':experiment_path,
              'experiment_path2':experiment_path2}
        
        return rr


    
    
    ############################################################
    def rerun(self, i):
        """
        Rerun experiment
    
        cm run experiment --rerun=True ...
        """

        i['rerun']=True

        return self.run(i)
    
    
    
    
    
    
    
    
    
    
    
    
    ############################################################
    def replay(self, i):
        """
        Replay experiment

        Args:
          (CM input dict): 

             (out) (str): if 'con', output to console

             (artifact) (str): experiment artifact

             (tags) (str): experiment tags separated by comma

             (dir) (str): experiment directory (often date time)
             (uid) (str): unique ID of an experiment

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action
        """

        # Find or add artifact based on repo/alias/tags
        i['fail_if_not_found']=True
        r = self._find_or_add_artifact(i)
        if r['return']>0: return r
        
        experiment = r['experiment']
        
        console = i.get('out','')=='con'
        
        # Print experiment folder
        experiment_path = experiment.path

        if console:
            print ('')
            print ('Path to CM experiment artifact: {}'.format(experiment_path))

        # Check date and time folder
        uid = i.get('uid', '')
        datetime = i.get('dir', '')

        if datetime!='':
            datetimes = [datetime]
        else:
            directories = os.listdir(experiment_path)

            datetimes = sorted([f for f in directories if os.path.isfile(os.path.join(experiment_path, f, self.CM_RESULT_FILE))], reverse=True)

        if len(datetimes)==0:
            return {'return':1, 'error':'experiment(s) not found in {}'.format(experiment_path)}
        
        # Check datetime directory
        found_result = {}

        if uid!='':
            for d in datetimes:
                r = self._find_uid({'path':experiment_path, 'datetime':d, 'uid':uid})
                if r['return']>0: return r

                if len(r.get('result',{}))>0:
                    found_result = r['result']
                    datetime = d
                    experiment_path2 = os.path.join(experiment_path, datetime)
                    break
                
            if len(found_result)==0:
                return {'return':1, 'error':'couldn\'t find result with UID {} in {}'.format(uid, experiment_path)}

        else:
            if len(datetimes)==1:
                datetime = datetimes[0]
            else:
                print ('')
                print ('Available experiments:')

                datetimes = sorted(datetimes)
                
                num = 0
                print ('')
                for d in datetimes:
                    print ('{}) {}'.format(num, d.replace('.',' ')))
                    num += 1

                if not console:
                    return {'return':1, 'error':'more than 1 experiment found.\nPlease use "cm run experiment --dir={date and time}"'}
                
                print ('')
                x=input('Make your selection or press Enter for 0: ')

                x=x.strip()
                if x=='': x='0'

                selection = int(x)

                if selection < 0 or selection >= num:
                    selection = 0

                datetime = datetimes[selection]
        
            # Final path to experiment
            experiment_path2 = os.path.join(experiment_path, datetime)

            if not os.path.isdir(experiment_path2):
                return {'return':1, 'error':'experiment path not found {}'.format(experiment_path2)}

            r = self._find_uid({'path':experiment_path, 'datetime':datetime})
            if r['return']>0: return r

            results = r['meta']

            if len(results)==0:
                return {'return':1, 'error':'results not found in {}'.format(experiment_path2)}

            elif len(results)==1:
                selection = 0

            else:
                print ('')
                print ('Available Unique IDs of results:')

                results = sorted(results, key=lambda x: x.get('uid',''))
                
                num = 0
                print ('')
                for r in results:
                    print ('{}) {}'.format(num, r.get('uid','')))
                    num += 1

                if not console:
                    return {'return':1, 'error':'more than 1 result found.\nPlease use "cm run experiment --uid={result UID}"'}

                print ('')
                x=input('Make your selection or press Enter for 0: ')

                x=x.strip()
                if x=='': x='0'

                selection = int(x)

                if selection < 0 or selection >= num:
                    selection = 0

            found_result = results[selection]
            uid = found_result['uid']
            
        # Final info
        if console:
            print ('')
            print ('Path to experiment: {}'.format(experiment_path2))

            print ('')
            print ('Result UID: {}'.format(uid))

        # Attempt to load cm-input.json
        experiment_input_file = os.path.join(experiment_path2, self.CM_INPUT_FILE)

        if not os.path.isfile(experiment_input_file):
            return {'return':1, 'error':'{} not found - can\'t replay'.format(self.CM_INPUT_FILE)}

        r = utils.load_json(experiment_input_file)
        if r['return']>0: return r

        cm_input = r['meta']

        tags = cm_input.get('tags','').strip()
        if 'replay' not in tags:
            if tags!='': tags+=','
            tags+='replay'
        cm_input['tags'] = tags
        
        if console:
            print ('')
            print ('Experiment input:')
            print ('')
            print (json.dumps(cm_input, indent=2))
            print ('')
        
        # Run experiment again
        r = self.cmind.access(cm_input)
        if r['return']>0: return r

        # TBA - validate experiment, etc ...
        
        
        return {'return':0}


    ############################################################
    def _find_or_add_artifact(self, i):
        """
        Find or add experiment artifact (reused in run and reply)

        Args:
          (CM input dict): 

            (fail_if_not_found) (bool) - if True, fail if experiment is not found

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          experiment (CM artifact class): Experiment artifact
        
        """

        console = i.get('out','')=='con'

        # Try to find experiment artifact by alias and/or tags
        ii = utils.sub_input(i, self.cmind.cfg['artifact_keys'] + ['tags'])
        ii['action']='find'

        ii_copy = copy.deepcopy(ii)

        # If artifact is specified, remove tags
        artifact = ii.get('artifact','').strip()
        if artifact!='' and not artifact.endswith(':') \
                        and '*' not in artifact and '?' not in artifact:
            if 'tags' in ii: del(ii['tags'])

        r = self.cmind.access(ii)
        if r['return']>0: return r

        lst = r['list']

        if len(lst)>1:
            print ('More than 1 experiment artifact found:')

            lst = sorted(lst, key=lambda x: x.path)
            
            num = 0
            print ('')
            for e in lst:
                print ('{}) {}'.format(num, e.path))
                print ('        Tags: {}'.format(','.join(e.meta.get('tags',[]))))
                num += 1

            if not console:
                return {'return':1, 'error':'more than 1 experiment artifact found.\nPlease use "cm run experiment {name}" or "cm run experiment --tags={tags separated by comma}"'}
            
            print ('')
            x=input('Make your selection or press Enter for 0: ')

            x=x.strip()
            if x=='': x='0'

            selection = int(x)

            if selection < 0 or selection >= num:
                selection = 0

            experiment = lst[selection]

        elif len(lst)==1:
            experiment = lst[0]
        else:
           # Create new entry
            if i.get('fail_if_not_found',False):
                return {'return':1, 'error':'experiment not found'}
            
            ii = copy.deepcopy(ii_copy)
            ii['action']='add'
            r = self.cmind.access(ii)
            if r['return']>0: return r

            experiment_uid = r['meta']['uid']

            r = self.cmind.access({'action':'find',
                                   'automation':'experiment,a0a2d123ef064bcb',
                                   'artifact':experiment_uid})
            if r['return']>0: return r

            lst = r['list']
            if len(lst)==0 or len(lst)>1:
                return {'return':1, 'error':'created experiment artifact with UID {} but can\'t find it - weird'.format(experiment_uid)}

            experiment = lst[0]
        
        return {'return':0, 'experiment':experiment}

    ############################################################
    def _find_uid(self, i):
        """
        Find experiment result with a given UID

        Args:
          (CM input dict): 

            path (str): path to experiment artifact
            datetime (str): sub-path to experiment
            (uid) (str): experiment UID

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

        path_to_experiment_result_file = os.path.join(path, datetime, self.CM_RESULT_FILE)

        rr={'return':0, 'path_to_file':path_to_experiment_result_file}

        if os.path.isfile(path_to_experiment_result_file):
            r = utils.load_json(file_name=path_to_experiment_result_file)
            if r['return']>0: return r

            meta = r['meta']

            rr['meta'] = meta

            # Searching for UID
            if uid!='':
                for result in meta:
                    ruid = result.get('uid', '').strip()
                    if ruid!='' and ruid==uid:
                        rr['result']=result
                        break

        return rr

############################################################################
def flatten_dict(d, flat_dict = {}, prefix = ''):

    for k in d:
        v = d[k]

        if type(v) is dict:
           flatten_dict(v, flat_dict, prefix+k+'.')
        else:
           flat_dict[prefix+k] = v    

    return flat_dict
