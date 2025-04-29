# Author and developer: Grigori Fursin

import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    Automation actions
    """

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
    def check(self, i):
        """
        Set configuration parameters

        Args:
          i (dict): 
             artifact (str): flex.cfg CMX artifact
             key (str): key to check
             ask (str): ask how to set the key
             reask (bool): force ask
             fail_if_empty (bool): fail if key is empty
             value: force value

        """


        ###################################################################
        # Process input

        # First level of inputs _input will be passed to associated module
        # Second level of inputs will control the task
        control = i['control']

        _input = control.get('_input', {})

        out = control.get('out', '')
        console = (out == 'con')

        artifact = i.get('artifact', '')
        if artifact == '':
            return self.cmind.prepare_error(1, 'flex.cfg artifact is not specified')

        key = _input.pop('key', '')
        if key == '':
            return self.cmind.prepare_error(1, 'key is not specified')

        ask = _input.pop('ask', '')
        reask = _input.pop('reask', False)
        fail_if_empty = _input.pop('fail_if_empty', False)
        value = _input.pop('value', None)
        return_dict = _input.pop('return_dict', '')

        ###################################################################
        # Separate artifact(s) into name and repo
        r = utils.process_input(i)
        if r['return']>0: return self.cmind.embed_error(r)

        r = self.cmind.x({'automation': control['_automation']['artifact'],
                          'action': 'find',
                          'artifact': artifact})
        if r['return']>0: return self.cmind.embed_error(r)

        lst = r['list']

        if len(lst) >1 :

            if console:
                print ('')
                print ('Available configurations:')
                print ('')
                for l in sorted(lst, key = lambda l: l.meta['alias']):
                    print ('* ' + l.meta['alias'])

            return self.cmind.prepare_error(1, 'more than 1 flex.cfg found')

        meta = {}

        if len(lst) == 1:
            meta = lst[0].meta

        if value == None:
            value = meta.get(key)

        if ask != '':
            if reask or value == None or (value == '' and fail_if_empty):
                print ('')
                value = input(ask + ' ').strip()

        if fail_if_empty and (value == None or value == ''):
            return self.cmind.prepare_error(1, 'value can\'t be empty')

        meta[key] = value

        # Update flx.cfg
        ii ={'automation': control['_automation']['artifact'],
             'action': 'update',
             'artifact': artifact,
             'meta': meta,
             'replace': True}

        r = self.cmind.x(ii)
        if r['return']>0: return self.cmind.embed_error(r)

        rr = {'return':0, key: value, 'value': value, 'meta': meta}

        if return_dict != '':
            rr[return_dict] = {key: value, 'value': value}

        return rr
