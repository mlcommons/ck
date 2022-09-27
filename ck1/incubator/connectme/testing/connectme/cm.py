import os

from connectme import config, io, misc, repo

###########################################################################
class CM:
    def __init__(self, 
                 path="",
                 debug=False,
                 con=False,
                 line_before_json=False,
                 print_json=False):

        """
        ConnectMe main class
        
        Args:
             path (str): path to all repositories (optional)

        """

        # Configuration
        self.cfg = {}

        # Update with static config
        self.cfg.update(config.cfg)

        # Run-time parameters
        self.rt = {}

        # Set path to all repositories
        #   Check 1) explicit path from above
        #         2) environment variable CM_HOME
        #         3) USER HOME directory CM
        home_path = path if path != "" else self.set_home_path()

        self.rt['home_path'] = home_path

        # Check debug
        if os.environ.get(config.ENV_DEBUG, '')!='':
            debug = True
        self.rt['debug'] = debug

        # Check console
        self.rt['con']=con

        # Check output
        self.rt['print_json']=print_json

        # Check if line before json
        self.rt['line_before_json']=line_before_json

        # Check file with databases
        self.rt['file_repo_list'] = os.path.join(home_path, config.FILE_REPO_LIST)

        # Load repositories or initialize empty file with local repos
        self.repos = []

        
    ###########################################################################
    def init(self):
        """
        ConnectMe class
        
        Args:
             path (str): path to all repositories (optional)

        """

        # Check repositories
        fn = self.rt['file_repo_list']
        
        if os.path.isfile(fn):
           r = io.load_json(fn) 
           if r['return']>0: return r

           self.repos = r['data']
        else:
           # Initialize local repo
           path_local_repo = os.path.join(self.rt['home_path'], config.LOCAL_REPO_NAME)

           lrepo = repo.Repo(self)

           r = lrepo.init(path_local_repo,
                          config.LOCAL_REPO_NAME,
                          config.LOCAL_REPO_UID)
           if r['return']>0: return r

        return {'return':0}

    ###########################################################################
    def register_path(self, path):
        """
        Register path with repository.
        
        Args:
             path (str): path to a CM repository

        """

        found = False
        for x in self.repos:
            try:
                if os.path.samefile(x['path'], path):
                    found = True
                    break
            except:
                pass

        if not found:
            self.repos.append({'path':path})

        # Save file
        r = io.save_json_or_yaml(self.rt['file_repo_list'], self.repos, sort_keys=True)
        if r['return']>0: return r

        return {'return':0}
    
    ###########################################################################
    def set_home_path(self):
        """

        Set ConnectMe home path where to store repositories and other info.
        
        Check
        steps:
         1) environment variable CM_REPOS
         2) USER HOME directory CM

        Create dir if empty.

        Args: 
                None

        Returns:
                path (str): path
        
        """

        path = os.environ.get(config.ENV_HOME,'')
        if path == "":
           from os.path import expanduser
           path = os.path.join(expanduser("~"), config.DEFAULT_HOME_DIR)

        return path




    ###########################################################################
    def access(self, i, argv=None):
        """
        Access CM repositories

        Args:
            i (dict) - CM dictionary

            (argv) (list) - original input from the command line
                            to support wrapping around tools
        """

        # Process special commands
        module = i.get('module','')

        if module == 'ck':
            # Keep support for CK
            import ck.kernel as ck

            return ck.access(argv[1:])

        data = i.get('data','')
            
        # Import fnmatch if * or ?
        module_wildcards=True if '*' in module or '?' in module else False
        data_wildcards=True if '*' in data or '?' in data else False

        if module_wildcards or data_wildcards:
            import fnmatch
        
        # Iterate over CM repos
        for p in self.repos:
            path = p['path']

            if os.path.isdir(path):
                # Expand modules
                list_of_modules=[]
                if not module_wildcards:
                    list_of_modules.append(module)
                else:
                    list_of_potential_modules = os.listdir(path)

                    for m in list_of_potential_modules:
                        if fnmatch.fnmatch(m, module):
                            list_of_modules.append(m)

                # Iterate over modules
                for m in list_of_modules:
                    pm=os.path.join(path, m)
                
                    if os.path.isdir(pm):
                        # Expand data
                        list_of_data=[]
                        if not data_wildcards:
                            list_of_data.append(data)
                        else:
                            list_of_potential_data = os.listdir(pm)

                            for d in list_of_potential_data:
                                if fnmatch.fnmatch(d, data):
                                    list_of_data.append(d)

                        # Iterate over data
                        for d in list_of_data:
                            pd=os.path.join(pm, d)

                            if os.path.isdir(pd):
                                print (pd)



        return {'return':0}
    






    def search(self,
               repo="",
               module="",
               data=""):
        """
        """

        # Iterate over repos
        paths=[]
        
        for rr in self.rt['repo_list']:
            path=rr['path']

            check_this_repo = True

            if repo!='' and rr['name'] != repo:
                check_this_repo = False

            if check_this_repo:
                # List modules
                mdirs = os.listdir(path)

                for m in mdirs:
                    path_to_module = os.path.join(path, m)

                    if os.path.isdir(path_to_module):
                        check_this_module = True

                        if module != '' and m != module:
                            check_this_module = False

                        if check_this_module:
                             # List directories
                             ddirs = os.listdir(path_to_module)

                             for d in ddirs:
                                 path_to_data = os.path.join(path_to_module, d)

                                 if os.path.isdir(path_to_data):
                                     check_this_data = True

                                     if data != '' and d != data:
                                         check_this_data = False

                                     if check_this_data:
                                         paths.append(path_to_data)
        
        return {'return':0, 'paths':paths}















    ###########################################################################
    def finalize(self, r):
        """
        Prepare error code

        Args:
            output (dict): misc

        Returns:
            (dict): xyz

        """

        ret = r['return']

        if ret > 0 and self.rt['con']:
            print (r['error'])

        if self.rt['print_json']:
            if self.rt['line_before_json']:
                print (config.LINE_BEFORE_JSON)

            import json
            print (json.dumps(r, indent=2))
            
        if ret > 0 and self.rt['debug']:
            raise(Exception(r['error']))

        return r


    ###########################################################################
    def err(self, r):
        """
        Print error and exit. Useful for scripts.

        Args:
            r (dict): return dictionary


        """

        ret = r['return']

        self.finalize(r)

        exit(ret)





    def ok(self, output = {}):
        """Prepare return code

        """

        r={'return': 0}
        r.update(output)
        return r

    def exit(self, r):
        """
        Check output, print error if error and exit

        """

        import sys

        code=r['return']

        if code>0:
            print (r['error'])

        sys.exit(code)

    def find_module(self, module):
        """
        Initialize ConnectMe library.

           Check 1) environment variable CM_REPOS
                 2) USER HOME directory CM

        """

        # Python object for this module
        obj = None
        
        # Python module for API
        python_module = config.PLUGIN_PREFIX + module

        # Check inside connectme and then globally in Python
        import importlib
        for internal_module in [config.NAME + "." + python_module, python_module]:
            try:
                obj = importlib.import_module(internal_module)
            except Exception as e:
                pass

            # Test if compatible
            if obj:
                try:
                    # Test if has compatibility var
                    x = obj.connectme
                except Exception as e:
                    obj = None

            if obj:
                break

        return obj

    def run_helper(self, i):
        """
        """

        # Find module in input
        module = ''

        if type(i)==list:
            if len(i) > 0:
                module=i[0]
        else:
            module = i['module']
            del(i['module'])

        if module == '':
            return self.err(self.errors['module_not_defined'])

        # Find CM module
        obj = self.find_module(module)
        
        # TBD: init empty Module class with UID and with attr: dummy_module=True
        if not obj:
            return self.err(self.errors['module_not_found'])

        # Init class from the module
        api = obj.api(self)

        # Check if input is a list and module has special func "parse_cmd" 
        if type(i)==list and hasattr(api, 'parse_cmd'):
            return api.parse_cmd(i)
        
        # Find action
        action = ''
        if type(i)==list:
            if len(i) > 1:
                action=i[1]
        else:
            action=i['action']
            del(i['action'])

        if action == '':
            # Check if module has help
            if hasattr(api, 'print_help'):
                return api.print_help()
            
            return self.err(self.errors['action_not_defined'])

        # Test if has argv extensions (so this func will parse args itself)
        func = None
        try: 
            func = getattr(api, action + '_argv')
        except Exception as e:
            pass

        r = self.ok()

        if func and type(i)==list:
            r = func(['']+i)
        else:
            if type(i)==dict:
                ii=i
            else:
                # TBD: convert list to input 
                ii={}

            try:
                func = getattr(api, action)
            except Exception as e:
                return self.err(self.error['action_not_defined'])

            # Use internal parser
            r = func(**ii)

        return r


    
    def run(self, i):
        """
        Run CM module with a given action.

        Args:
           i (list | dict) - action input
        """

        r = self.run_helper(i)

        if self.rt['print_json']:
            print(r)

        return r

