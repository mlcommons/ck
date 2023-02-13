import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    CM "experiment" automation actions
    """

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

          automation (str): automation as CM string object

          (artifact) (str): experiment artifact

          (tags) (str): experiment tags separated by comma

          (script) (str): find and run CM script by name
          (s)

          (script_tags) (str): find and run CM script by tags
          (stags)

          (explore) (dict): exploration dictionary

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action
        """

        from cmind import utils
        import itertools
        import copy

        # Update/create experiment entry
        ii=utils.sub_input(i, self.cmind.cfg['artifact_keys'] + ['tags'])

        artifact = ii.get('artifact','')
        artifact_without_repo = artifact
        j = artifact.find(':')
        if j>=0:
           artifact_without_repo = artifact[j+1:]

        tags = ii.get('tags','').strip()

        # Check if need to add a new UID experiment or find if exists
        action = 'add' if artifact_without_repo=='' and tags=='' else 'find'

        ii['action']=action
        r=self.cmind.access(ii)
        if r['return']>0: return r

        if action == 'add':
            experiment_path = r['path']
        else:
           lst = r['list']

           if len(lst)==0:
               ii['action']='add'
               r=self.cmind.access(ii)
               if r['return']>0: return r
               experiment_path = r['path']
           elif len(lst)==1:
               experiment = r['list'][0]
               experiment_path = experiment.path
           else:
               # Select 1 and proceed
               print ('More than 1 experiment artifact found:')

               print ('')

               lst = sorted(lst, key=lambda x: x.path)
               
               num = 0
               for e in lst:
                   print ('{}) {}'.format(num, e.path))
                   num += 1

               print ('')
               x=input('Make your selection or press Enter for 0: ')

               x=x.strip()
               if x=='': x='0'

               selection = int(x)

               if selection < 0 or selection >= num:
                   selection = 0

               experiment = lst[selection]
               experiment_path = experiment.path

               print ('')


        
        
        
        
        # Get directory with datetime
        num = 0
        found = False

        while not found:
            r = utils.get_current_date_time({})
            if r['return']>0: return r

            date_time = r['iso_datetime'].replace(':','-').replace('T','.')

            if num>0:
                date_time+='.'+str(num)

            experiment_path2 = os.path.join(experiment_path, date_time)

            if not os.path.isdir(experiment_path2):
                found = True
                break

            num+=1

        # Check/create directory with date_time
        os.makedirs(experiment_path2)

        # Change current path
        print ('Path to experiment: {}'.format(experiment_path2))

        os.chdir(experiment_path2)


        
        # Check if exploration is in the input
        explore = i.get('explore', {})
        if len(explore)>0:
            del(i['explore'])


        # Prepare run command
        cmd = ''
        ii = {}
        
        unparsed = i.get('unparsed_cmd', [])
        if len(unparsed)>0:
            for u in unparsed:
                if ' ' in u: u='"'+u+'"'
                cmd+=' '+u

            cmd=cmd.strip()

            ii = {'action':'native-run',
                  'cmd':cmd}
        
        else:
            ii=utils.sub_input(i, self.cmind.cfg['artifact_keys'] + ['tags', 'cmd', 'action', 'explore'], reverse=True)
            ii['action']='run'

            for x in [('tags', ['script_tags', 'stags']), ('artifact', ['s', 'script'])]:
                for k in x[1]:
                    v = ii.get(k,'').strip()
                    if v!='':
                        ii[x[0]]=v
                        del(ii[k])


        ii['automation']='script,5b4e0237da074764'

        env = i.get('env', {})
        
        # Extract exploration expressions from {{VAR{expression}}}

        for key in ii:
            v = ii[key]

            if type(v)==str:
                
                j = 1
                k = 0
                while j>=0:
                   j = v.find('}}}', k)
                   if j>=0:
                       k = j+1

                       l = v.rfind('{{',0, j)

                       if l>=0:
                           l2 = v.find('{', l+2, j)
                           if l2>=0:
                               k = l2+1

                               var = v[l+2:l2]
                               expr = v[l2+1:j]

                               explore[var] = expr

                               v = v[:l2]+ v[j+1:]

                ii[key] = v

        # Prepare exploration
        # Note that from Python 3.7, dictionaries are ordered so we can define order for exploration in json/yaml
        # ${{XYZ}} ${{ABC(range(1,2,3))}}
        
        # separate dse into var and range
        explore_keys=[]
        explore_dimensions=[]

        for k in explore:
            v=explore[k]

            explore_keys.append(k)

            if type(v)!=list:
                v=eval(v)

            explore_dimensions.append(v)


        step = 0

        steps = itertools.product(*explore_dimensions)

        # Next command will run all iterations so we need to redo above command once again
        num_steps = len(list(steps))

        steps = itertools.product(*explore_dimensions)


        ii_copy = copy.deepcopy(ii)

        for dimensions in steps:
            
            step += 1
            
            print ('================================================================')
            print ('Experiment step: {} out of {}'.format(step, num_steps))

            print ('')

            ii = copy.deepcopy(ii_copy)

            l_dimensions=len(dimensions)
            if l_dimensions>0:
                print ('  Updating variables during exploration:')

                print ('')
                for j in range(l_dimensions):
                    v = dimensions[j]
                    k = explore_keys[j]
                    print ('    - Dimension {}: "{}" = {}'.format(j, k, v))

                    env[k] = str(v)

                print ('')

            # Prepare extra directory if num_steps > 1
            if num_steps==1:
                experiment_path3 = experiment_path2
            else:
                x = len(str(num_steps))

                y = len(str(step))

                extra_path = 'result-' + '0'*(x-y) + str(step)

                experiment_path3 = os.path.join(experiment_path2, extra_path)

                if not os.path.isdir(experiment_path3):
                    os.makedirs(experiment_path3)

                    # Change current path
                    print ('Path to experiment step: {}'.format(experiment_path3))
                    print ('')

            # Prepare and run experiment in a given placeholder directory
            os.chdir(experiment_path3)
                    
            env['CM_EXPERIMENT_PATH'] = experiment_path
            env['CM_EXPERIMENT_PATH2'] = experiment_path2
            env['CM_EXPERIMENT_PATH3'] = experiment_path3

            ii['env'] = env
            
            # Update {{}} in all inputs
            for key in ii:
                v = ii[key]

                if type(v)==str:
                    
                    j = 1
                    k = 0
                    while j>=0:
                       j = v.find('{{', k)
                       if j>=0:
                           k = j
                           l = v.find('}}',j+2)
                           if l>=0:
                               
                               var = v[j+2:l]

                               # Such vars must be in env
                               if var not in env:
                                   return {'return':1, 'error':'key "{}" is not in env during exploration'.format(var)}

                               v = v[:j] + env[var] + v[l+2:]

                    ii[key] = v


            # Record input
            experiment_input_file = os.path.join(experiment_path3, 'cm-input.json')

            r = utils.save_json(file_name=experiment_input_file, meta={'cm_raw_input':i, 
                                                                       'cm_input':ii})
            if r['return']>0: return r
            
            # Prepare and clean output
            experiment_output_file = os.path.join(experiment_path3, 'cm-output.json')

            if os.path.isfile(experiment_output_file):
                os.delete(experiment_output_file)
            
            # Prepare and clean output
            experiment_output_file = os.path.join(experiment_path3, 'cm-output.json')

            if os.path.isfile(experiment_output_file):
                os.delete(experiment_output_file)


            # Run script (CM or native)
            rr=self.cmind.access(ii)
            if rr['return']>0: return rr


            # Record output
            r = utils.save_json(file_name=experiment_output_file, meta=rr)
            if r['return']>0: return r




        rr = {'return':0,
              'experiment_path':experiment_path,
              'experiment_path2':experiment_path2}
        
        return rr

    ############################################################
    def replay(self, i):
        """
        Reply experiment

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          automation (str): automation as CM string object

          (artifact) (str): experiment artifact

          (tags) (str): experiment tags separated by comma

          (datetime) (str): ISO time

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action
        """

        from cmind import utils

        # Update/create experiment entry
        ii=utils.sub_input(i, self.cmind.cfg['artifact_keys'] + ['tags'])

        ii['action']='find'
        r=self.cmind.access(ii)
        if r['return']>0: return r

        lst = r['list']

        if len(lst)==0:
            return {'return':16, 'error':'experiment not found'}

        if len(lst)>1:
            print ('Experiment artifacts:')
            print ('')

            for l in lst:
                print (l.path)

            return {'return':1, 'error':'more than 1 artifact found'}

            print ('')

        experiment = r['list'][0]

        experiment_path = experiment.path

        print ('Experiment artifact: {}'.format(experiment_path))

        # Check date and time
        datetime = i.get('datetime','').replace(':','_')

        if datetime=='':
            files = os.listdir(experiment_path)

            directories = sorted([ f for f in files if os.path.isdir(os.path.join(experiment_path,f))], reverse=True)

            if len(directories)==0:
                return {'return':16, 'error':'no experiments found in the artifact'}

            if len(directories)>1:
                print ('')
                print ('Available experiments:')
                print ('')

                for d in directories:
                    print (d)

            datetime = directories[0]

        experiment_path2 = os.path.join(experiment_path, datetime)

        if not os.path.isdir(experiment_path2):
            return {'return':1, 'error':'experiment path not found {}'.format(experiment_path2)}

        # Read input
        experiment_input_file = os.path.join(experiment_path2, 'cm-input.json')

        r = utils.load_json(file_name=experiment_input_file)
        if r['return']>0: return r

        ii=r['meta']

        # Run CM script
        print ('')
        rr=self.cmind.access(ii)

        return rr

