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

          (ic) (str): use CM "intelligent component" by name

          (ic_tags) (str): use CM "intelligent component" by tags

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

        ii['action']='update'
        r=self.cmind.access(ii)
        if r['return']>0: return r

        experiment = r['list'][0]

        experiment_path = experiment.path

        print ('Experiment artifact: {}'.format(experiment_path))

        # Get current date and time
        r = utils.get_current_date_time({})
        if r['return']>0: return r

        date_time = r['iso_datetime'].replace(':','_')

        # Check/create directory with date_time
        experiment_path2 = os.path.join(experiment_path, date_time)

        if not os.path.isdir(experiment_path2):
            os.makedirs(experiment_path2)

        # Change current path
        os.chdir(experiment_path2)


        # Prepare and clean output
        experiment_output_file = os.path.join(experiment_path2, 'cm-output.json')

        if os.path.isfile(experiment_output_file):
            os.delete(experiment_output_file)

        # Prepare input for IC artifact
        ii=utils.sub_input(i, self.cmind.cfg['artifact_keys'] + ['tags'], reverse=True)

        ii['action']='run'
        ii['automation']='ic,972c28dafb2543fa'

        if ii.get('ic','')!='':
           ii['artifact']=ii['ic']
           del(ii['ic'])

        if ii.get('ic_tags','')!='':
           ii['tags']=ii['ic_tags']
           del(ii['ic_tags'])

        # Record input
        experiment_input_file = os.path.join(experiment_path2, 'cm-input.json')

        r = utils.save_json(file_name=experiment_input_file, meta=ii)
        if r['return']>0: return r

        # Run IC
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

        # Run IC component
        print ('')
        rr=self.cmind.access(ii)

        return rr

