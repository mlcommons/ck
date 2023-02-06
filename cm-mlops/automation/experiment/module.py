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

          (script_tags) (str): find and run CM script by tags

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
            ii=utils.sub_input(i, self.cmind.cfg['artifact_keys'] + ['tags', 'cmd', 'action'], reverse=True)
            ii['action']='run'

            stags = ii.get('stags','').strip()
            if stags!='':
                ii['tags']=stags
                del(ii['stags'])

        ii['automation']='script,5b4e0237da074764'

        env = i.get('env', {})
        env['CM_EXPERIMENT_PATH'] = experiment_path
        env['CM_EXPERIMENT_PATH2'] = experiment_path2

        ii['env'] = env

        # Record input
        experiment_input_file = os.path.join(experiment_path2, 'cm-input.json')

        r = utils.save_json(file_name=experiment_input_file, meta={'cm_raw_input':i, 
                                                                   'cm_input':ii})
        if r['return']>0: return r
        
        # Prepare and clean output
        experiment_output_file = os.path.join(experiment_path2, 'cm-output.json')

        if os.path.isfile(experiment_output_file):
            os.delete(experiment_output_file)
        
        # Prepare and clean output
        experiment_output_file = os.path.join(experiment_path2, 'cm-output.json')

        if os.path.isfile(experiment_output_file):
            os.delete(experiment_output_file)


        # Run CM script
        print ('')
        rr=self.cmind.access(ii)
        if rr['return']>0: return rr


        # Record output
        r = utils.save_json(file_name=experiment_output_file, meta=rr)
        if r['return']>0: return r

        rr['experiment_path']=experiment_path
        rr['experiment_path2']=experiment_path2

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

