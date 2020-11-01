#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

import os
cfg = {}  # Will be updated by CK (meta description of this module)
work = {}  # Will be updated by CK (temporal data)
ck = None  # Will be updated by CK (initialized CK kernel)

# Local settings


##############################################################################
# Initialize module


def init(i):
    """
    Input:  {}

    Output: {
              return   - return code =  0, if successful
                                     >  0, if error
              (error)  - error text if return > 0
            }

    """
    return {'return': 0}

##############################################################################
# Create repository in a given directory and record info in CK


def add(i):
    """
    Note, that we can't create repos in parallel (recording to repo cache may fail).
    However, for now, we do not expect such cases (i.e. repos are created rarely)

    Input:  {
              (repo_uoa)                 - repo UOA (where to create entry)
              data_uoa                   - data UOA
              (data_uid)                 - data UID (if uoa is an alias)
              (data_name)                - user friendly data name

              (cids[0])                  - as uoa or full CID

              (path)                     - if !='' - create in this path or import from this path
              (here)                     - if =='yes', create in current path
              (use_default_path)         - if 'yes' create repository in the default path (CK_REPOS)
                                           instead of the current path (default is 'yes')

              (use_current_path)         - if 'yes' create repository in the current path
                                           (default is 'no')

              (default)                  - if 'yes', no path is used, 
                                           but the repository is taken either 
                                           from the CK directory or from CK_LOCAL_REPO

              (import)                   - if 'yes', register repo in the current directory in CK
                                           (when received from someone else)

              (remote)                   - if 'yes', remote repository
              (remote_repo_uoa)          - if !='' and type=='remote' repository UOA on the remote CK server

              (shared)                   - if not remote and =='git', repo is shared/synced through GIT
              (share)                    - (for user-friendly CMD) if 'yes', set shared=git

              (allow_writing)            - if 'yes', allow writing 
                                           (useful when kernel is set to allow writing only to such repositories)

              (url)                      - if type=='remote' or 'git', URL of remote repository or git repository
              (hostname)                 - if !='', automatically form url above (add http:// + /ck?)
              (port)                     - if !='', automatically add to url above
              (hostext)                  - if !='', add to the end of above URL instead of '/ck?' -
                                           useful when CK server is accessed via Apache2, IIS, Nginx or other web servers

              (githubuser)               - if shared repo, use this GitHub user space instead of default "ctuning"
              (sync)                     - if 'yes' and type=='git', sync repo after each write operation

              (gitzip)                   - if 'yes', download as zip from GitHub
              (zip)                      - path to zipfile (local or remote http/ftp)
              (overwrite)                - if 'yes', overwrite files when unarchiving

              (repo_deps)                - dict with dependencies on other shared repositories with following keys:
                                             "repo_uoa"
                                             ("repo_uid") - specific UID (version) of a repo
                                             ("repo_url") - URL of the shared repository (if not from github.com/ctuning)

              (quiet)                    - if 'yes', do not ask questions unless really needed

              (skip_reusing_remote_info) - if 'yes', do not reuse remote .cmr.json description of a repository

              (current_repos)            - if resolving dependencies on other repos, list of repos being updated (to avoid infinite recursion)

              (describe)                 - describe repository for Artifact Evaluation (see http://cTuning.org/ae)

              (stable)        - take stable version (highly experimental)
              (version)       - checkout version (default - stable)
              (branch)        - git branch
              (checkout)      - git checkout

              (private)                  - if 'yes', mark as private (do not automatically list entries, etc)

              (split_all_dirs)           - if !='0' force split of all dirs in this repo (be careful)
                                           must be empty before doing this!

              (recache)                  - if 'yes' force recache
            }

    Output: {
              return       - return code =  0, if successful
                                           16, repository with a given path is already registered in CK
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    # Check if global writing is allowed
    r = ck.check_writing({})
    if r['return'] > 0:
        return r

    o = i.get('out', '')

    a = i.get('repo_uoa', '')
    d = i.get('data_uoa', '')
    di = i.get('data_uid', '')
    dn = i.get('data_name', '')

    if ck.cfg.get('allowed_entry_names', '') != '':
        import re

        anames = ck.cfg.get('allowed_entry_names', '')

        if not re.match(anames, a) or \
           not re.match(anames, d) or \
           not re.match(anames, di):
            return {'return': 1, 'error': 'found disallowed characters in names (allowed: "'+anames+'")'}

    if ck.cfg.get('force_lower', '') == 'yes':
        a = a.lower()
        d = d.lower()
        di = di.lower()

    stable = i.get('stable', '')
    version = i.get('version', '')
    if stable == 'yes':
        version = 'stable'
    branch = i.get('branch', '')
    checkout = i.get('checkout', '')

    cr = i.get('current_repos', [])

    rdeps = i.get('repo_deps', [])

    quiet = i.get('quiet', '')

    overwrite = i.get('overwrite', '')

    remote = i.get('remote', '')
    rruoa = i.get('remote_repo_uoa', '')
    shared = i.get('shared', '')
    if shared == 'yes':
        shared = 'git'

    share = i.get('share', '')
    if share == 'yes' and shared == '':
        shared = 'git'

    private = i.get('private', '')
    split_all_dirs = i.get('split_all_dirs', '')
    xrecache = i.get('recache', '')

    ptr = ''
    zp = i.get('zip', '')
    gz = i.get('gitzip', '')

    if zp != '':
        if zp.startswith('~'):
            from os.path import expanduser
            home = expanduser("~")

            zp = os.path.abspath(home+os.sep+zp[1:])

        quiet = 'yes'

        if d == '':
            # Try to get data UOA
            if not os.path.isfile(zp):
                return {'return': 1, 'error': 'zip file not found'}

            # Try to get .ckr.json
            import zipfile

            try:
                with zipfile.ZipFile(zp) as z:
                    zip_has_git = False
                    if '.git/HEAD' in z.namelist():
                        zip_has_git = True

                    if ck.cfg['repo_file'] in z.namelist():
                        x = z.open(ck.cfg['repo_file'])
                        y = x.read()

                        r = ck.convert_json_str_to_dict(
                            {'str': y, 'skip_quote_replacement': 'yes'})
                        if r['return'] > 0:
                            return r
                        yd = r['dict']

                        d = yd.get('data_uoa', '')
                        di = yd.get('data_uid', '')
                        dn = yd.get('data_name', '')

                        zip_shared = yd.get('dict', {}).get('shared', '')
                        if zip_shared != '':
                            if zip_shared != 'git' or zip_has_git:
                                shared = yd['dict']['shared']
                                share = 'yes'

                        x.close()
                z.close()
            except Exception as e:
                return {'return': 1, 'error': 'problem reading zip file ('+format(e)+')'}

            if d == '':
                x1 = os.path.basename(zp)
                d = os.path.splitext(x1)[0]
                if d.startswith('ckr-'):
                    d = d[4:]

                if o == 'con':
                    ck.out('Auto-detected repo name from zip filename: '+d)

    if gz == 'yes':
        zp = ck.cfg['default_shared_repo_url']+'/'+d+'/archive/master.zip'
        ptr = d+'-master/'
        quiet = 'yes'

    rx = form_url(i)
    if rx['return'] > 0:
        return rx
    url = rx['url']

    sync = i.get('sync', '')
    df = i.get('default', '')

    eaw = i.get('allow_writing', '')

    udp = i.get('use_default_path', 'yes')
    ucp = i.get('use_current_path', '')
    if ucp == 'yes':
        udp = ''

    # Get repo path (unless 'here' later)
    px = i.get('path', '')

    # Check if import
    imp = i.get('import', '')
    if imp == 'yes':
        if px == '':
            i['here'] = 'yes'

    # Get 'here' path
    if i.get('here', '') == 'yes':
        px = os.getcwd()
    p = px

    if imp == 'yes':
        py = os.path.join(p, ck.cfg['repo_file'])
        if os.path.isfile(py):
            r = ck.load_json_file({'json_file': py})
            if r['return'] > 0:
                return r
            dc = r['dict']

            d = dc.get('data_uoa', '')
            di = dc.get('data_uid', '')
            dn = dc.get('data_name', '')

    if p == '' and udp == 'yes':
        p = os.path.join(ck.work['dir_repos'], d)

    # Normalize path
    p = os.path.normpath(p)

    # If console mode, first, check if shared (GIT, etc)
    if o == 'con':
        # Asking for alias
        if df != 'yes' and (d == '' or ck.is_uid(d)):
            r = ck.inp(
                {'text': 'Enter an alias for this repository (or Enter to skip it): '})
            d = r['string']
            if d == '':
                d = di
            if d == '':
                r = ck.gen_uid({})
                if r['return'] > 0:
                    return r
                di = r['data_uid']
                d = di

        # Asking for a user-friendly name
        if df != 'yes' and dn == '':
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Enter a user-friendly name of this repository (or Enter to reuse alias): '})
                dn = r['string']
            if dn == '':
                dn = d

        # Asking if remote
        if df != 'yes' and remote == '':
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Is this repository a remote CK web service (y/N)? '})
                remote = r['string'].lower()
            if remote == 'yes' or remote == 'y':
                remote = 'yes'
            else:
                remote = ''

        # Asking for a user-friendly name
        if px == '' and df != 'yes' and remote != 'yes' and udp == '':
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Would you like to create repo in the directory from CK_REPOS variable (Y/n): '})
                x = r['string'].lower()
                if x == '' or x == 'yes' or x == 'y':
                    p = os.path.join(ck.work['dir_repos'], d)

        # Asking for remote url
        if df != 'yes' and remote == 'yes' and url == '':
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Enter URL of remote CK repo (example: http://localhost:3344/ck?): '})
                url = r['string'].lower()
            if url == '':
                return {'return': 1, 'error': 'URL is empty'}

        # Asking for remote repo UOA
        if df != 'yes' and remote == 'yes' and rruoa == '':
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Enter remote repo UOA or Enter to skip: '})
                rruoa = r['string'].lower()

        # Asking for shared
        if remote == '' and shared == '' and share == '':
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Is this repository shared via GIT (y/N)? '})
                x = r['string'].lower()
                if x == 'yes' or x == 'y':
                    share = 'yes'

        if share == 'yes' and shared == '':
            shared = 'git'

        # Check additional parameters if git
        ghu = i.get('githubuser', '')
        if shared == 'git' and url == '':

            if ghu != '':
                durl = ck.cfg.get('github_repo_url', '')
                if not durl.endswith('/'):
                    durl += '/'
                durl += ghu
            else:
                durl = ck.cfg.get('default_shared_repo_url', '')

            if not durl.endswith('/'):
                durl += '/'
            durl += d
#          if durl.startswith('http://') or durl.startswith('https://'):
#             durl+='.git'

            if quiet != 'yes':
                s = 'Enter URL of GIT repo '
                if d == '':
                    s += '(for example, https://github.com/ctuning/ck-analytics.git)'
                else:
                    s += '(or Enter for '+durl+')'
                r = ck.inp({'text': s+': '})
                url = r['string'].lower()
            if url == '':
                url = durl

        # Check additional parameters if git
        if shared == 'git' and sync == '':
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Would you like to sync repo each time after writing to it (y/N)?: '})
                x = r['string'].lower()
                if x == 'yes' or x == 'y':
                    sync = 'yes'

        # Asking for a user-friendly name
        if df != 'yes' and remote != 'yes' and eaw == '':
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Would you like to explicitly allow writing to this repository in case kernel disables all writing (y/N): '})
                x = r['string'].lower()
                if x == 'yes' or x == 'y':
                    eaw = 'yes'

        # Check if add more deps
        if quiet != 'yes':
            r = add_more_deps({})
            if r['return'] > 0:
                return r

            rdeps1 = r['repo_deps']
            for q in rdeps1:
                rdeps.append(q)

    # Check if already registered (if not remote)
    if remote != 'yes':
        r = ck.find_repo_by_path({'path': p})
        if r['return'] > 0 and r['return'] != 16:
            return r

    # Check if repository is already registered with this path
    r = ck.find_repo_by_path({'path': p})
    if r['return'] == 0:
        return {'return': 16, 'error': 'repository with a given path is already registered in CK'}
    elif r['return'] != 16:
        return r

    # Prepare local description file
    py = os.path.join(p, ck.cfg['repo_file'])

    # Create dummy if doesn't exist
    if remote != 'yes' and not os.path.isdir(p):
        os.makedirs(p)

    # If zip, get (download) and unzip file ...
    if zp != '':
        rz = get_and_unzip_archive(
            {'zip': zp, 'path': p, 'path_to_remove': ptr, 'overwrite': overwrite, 'out': o})
        if rz['return'] > 0:
            return rz

        py = os.path.join(p, ck.cfg['repo_file'])
        if os.path.isfile(py):
            r = ck.load_json_file({'json_file': py})
            if r['return'] > 0:
                return r
            dc = r['dict']

            d = dc.get('data_uoa', '')
            di = dc.get('data_uid', '')
            dn = dc.get('data_name', '')

    # If git, clone repo
    repo_had_local = True
    dd = {}
    if remote != 'yes' and shared == 'git' and zp == '':
        r = pull({'path': p, 'type': shared, 'url': url,
                  'clone': 'yes', 'git': i.get('git', ''), 'out': o})
        if r['return'] > 0:
            return r

        # Check if there is a local repo description
        if os.path.isfile(py):
            r = ck.load_json_file({'json_file': py})
            if r['return'] > 0:
                return r
            dc = r['dict']
            ddc = dc.get('dict', {})
            dd.update(ddc)

            xd = dc.get('data_uoa', '')
            xdi = dc.get('data_uid', '')
            xdn = dc.get('data_name', '')

            if o == 'con':
                ck.out('Cloned repository has the following info:')
                ck.out(' UID                = '+xdi)
                ck.out(' UOA                = '+xd)
                ck.out(' User friendly name = '+xdn)
                ck.out('')
            if i.get('skip_reusing_remote_info', '') != 'yes':
                d = xd
                di = xdi
                dn = xdn
        else:
            repo_had_local = False

    # Prepare meta description
    if df == 'yes':
        dd['default'] = 'yes'
    if remote == 'yes':
        dd['remote'] = 'yes'
        if rruoa != '':
            dd['remote_repo_uoa'] = rruoa
    if shared != '':
        dd['shared'] = shared
        if sync != '':
            dd['sync'] = sync
    if url != '':
        dd['url'] = url
    if remote != 'yes':
        dd['path'] = p
    if eaw == 'yes':
        dd['allow_writing'] = 'yes'
    if len(rdeps) > 0:
        dd['repo_deps'] = rdeps
    if private != '':
        dd['private'] = private
    if split_all_dirs != '':
        dd['split_all_dirs'] = split_all_dirs
    if xrecache != '':
        dd['recache'] = xrecache

    # Check if need to describe for Artifact Evaluation
    if i.get('describe', '') == 'yes':
        r = describe({'dict': dd})
        if r['return'] > 0:
            return r

    # If not default, go to common core function to create entry
    if df != 'yes':
        ii = {'module_uoa': work['self_module_uoa'],
              'action': 'add',
              'data_uoa': d,
              'dict': dd,
              'common_func': 'yes'}
        if a != '':
            ii['repo_uoa'] = a
        if di != '':
            ii['data_uid'] = di
        if dn != '':
            ii['data_name'] = dn
        rx = ck.access(ii)
        if rx['return'] > 0:
            return rx
    else:
        # Load default repo and prepare return
        ii = {'module_uoa': work['self_module_uoa'],
              'action': 'load',
              'data_uoa': 'default',
              'common_func': 'yes'}
        rx = ck.access(ii)
    px = rx['path']
    dx = rx['data_uid']
    alias = rx['data_alias']

    # Update repo cache if not default local
    dz = {'data_uoa': d, 'data_uid': dx, 'data_alias': alias,
          'path_to_repo_desc': px, 'data_name': dn, 'dict': dd}

    if df != 'yes':
        r = ck.reload_repo_cache({})  # Ignore errors
        ck.cache_repo_uoa[d] = dx
        ck.cache_repo_info[dx] = dz
        r = ck.save_repo_cache({})
        if r['return'] > 0:
            return r

    # Record local info of the repo (just in case)
    if remote != 'yes':
        if 'path_to_repo_desc' in dz:
            # Avoid recording some local info
            del (dz['path_to_repo_desc'])
        if dz.get('dict', {}).get('path', '') != '':
            del (dz['dict']['path'])  # Avoid recording some local info

        if not os.path.isfile(py):
            ry = ck.save_json_to_file({'json_file': py, 'dict': dz})
            if ry['return'] > 0:
                return ry

        # If sync (or pulled repo did not have local description), add it ...
        if sync == 'yes' or (shared == 'git' and not repo_had_local):
            ppp = os.getcwd()

            os.chdir(p)
            ss = ck.cfg['repo_types'][shared]['add'].replace(
                '$#path#$', px).replace('$#files#$', ck.cfg['repo_file'])
            os.system(ss)

            os.chdir(ppp)

    # If console mode, print various info
    if o == 'con':
        ck.out('')
        ck.out('CK repository successfully registered!')
        ck.out('')

        if df != 'yes':
            ck.out('CK repo description path = '+px)
            ck.out('CK repo UID              = '+dx)

    # Recache repos otherwise may be problems with deps
    if o == 'con':
        ck.out('')
        ck.out('Recaching repos to speed up access ...')
        ck.out('')
    r = recache({'out': o})
    if r['return'] > 0:
        return r

    # Check deps
    if o == 'con':
        ck.out('  ========================================')
        ck.out('  Checking dependencies on other repos ...')
        ck.out('')

    how = 'pull'
    if gz == 'yes':
        how = 'add'
    r = deps({'path': p,
              'current_path': cr,
              'how': how,
              'version': version,
              'branch': branch,
              'checkout': checkout,
              'out': o})
    if r['return'] > 0:
        return r

    # Print if default
    if df == 'yes' and o == 'con':
        ck.out('')
        ck.out('Please, do not forget to add path to this repository to CK_LOCAL_REPO environment variable:')
        ck.out('')
        ck.out('  Linux: export CK_LOCAL_REPO='+p)
        ck.out('  Windows: set CK_LOCAL_REPO='+p)

    return rx

##############################################################################
# Update repository in a given directory and record info in CK


def update(i):
    """
    Update repository info

    Input:  {
              data_uoa                   - data UOA of the repo

              (shared)                   - if not remote and =='git', shared through GIT

              (url)                      - if type=='git', URL of remote repository or git repository
              (hostname)                 - if !='', automatically form url above (add http:// + /ck?)
              (port)                     - if !='', automatically add to url above
              (hostext)                  - if !='', add to the end of above URL instead of '/ck?' -
                                           useful when CK server is accessed via Apache2, IIS, Nginx or other web servers

              (sync)                     - if 'yes' and type=='git', sync repo after each write operation
              (allow_writing)            - if 'yes', allow writing 
                                           (useful when kernel is set to allow writing only to such repositories)

              (repo_deps)                - dict with dependencies on other shared repositories with following keys:
                                             "repo_uoa"
                                             ("repo_uid") - specific UID (version) of a repo
                                             ("repo_url") - URL of the shared repository (if not from github.com/ctuning)

              (update)                   - if 'yes', force updating

              (describe)                 - describe repository for Artifact Evaluation (see http://cTuning.org/ae)

              (private)                  - if 'yes', mark as private (do not automatically list entries, etc)

              (split_all_dirs)           - if !='0' force split of all dirs in this repo (be careful)
                                           must be empty before doing this!

              (recache)                  - if 'yes' force recache

              (quiet)                    - if 'yes', do not answer extra questions

              (dict)                     - update dict directly
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import copy

    # Check if global writing is allowed
    r = ck.check_writing({})
    if r['return'] > 0:
        return r

    o = i.get('out', '')

    duoa = i.get('data_uoa', '')

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa = duoa.lower()

    remote = i.get('remote', '')
    rruoa = i.get('remote_repo_uoa', '')
    shared = i.get('shared', '')
    sync = i.get('sync', '')

    rx = form_url(i)
    if rx['return'] > 0:
        return rx
    url = rx['url']

    rdeps = i.get('repo_deps', [])

    eaw = i.get('allow_writing', '')

    quiet = i.get('quiet', '')

    # Get configuration (not from Cache - can be outdated info!)
#    r=ck.load_repo_info_from_cache({'repo_uoa':duoa})
    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uoa'],
                   'data_uoa': duoa})
    if r['return'] > 0:
        return r

    p = r.get('dict', {}).get('path', '')

    dn = r.get('data_name', '')
    d = r['dict']

    dd = i.get('dict', {})
    if len(dd) > 0:
        d.update(dd)

    remote = d.get('remote', '')

    changed = False

    # Check user-friendly name
    if dn != '':
        ck.out('Current user-friendly name of this repository: '+dn)
        ck.out('')

        if quiet != 'yes':
            r = ck.inp(
                {'text': 'Enter a user-friendly name of this repository (or Enter to keep old value): '})
            x = r['string']
            if x != '':
                dn = x
                changed = True

    # If remote or shared, update URL
    if shared == 'yes' or shared == 'git':
        d['shared'] = 'git'

    shared = d.get('shared', '')
    if remote == 'yes':
        url = d.get('url', '')
        ck.out('Repository is remote ...')
        ck.out('')
        ck.out('Current URL: '+url)
        ck.out('')
        if quiet != 'yes':
            rx = ck.inp(
                {'text': 'Enter new URL (or Enter to leave old one): '})
            x = rx['string']
            if x != '':
                d['url'] = x
                changed = True
    elif shared != '':
        if url != '':
            d['url'] = url

        url = d.get('url', '')
        ck.out('Repository is shared ...')
        ck.out('')
        ck.out('Current URL: '+url)

        if shared == 'git':
            sync = d.get('sync', '')
            ck.out('')
            if sync != '':
                ck.out('Current sync setting: '+sync)
            if quiet != 'yes':
                r = ck.inp(
                    {'text': 'Would you like to sync repo each time after writing to it (y/N)?: '})
                x = r['string'].lower()
                if x == 'yes' or x == 'y':
                    d['sync'] = 'yes'
                    changed = True

    # Asking about forbidding explicit writing to this repository
    if remote != 'yes' and eaw == '':
        if eaw == '':
            eaw = d.get('allow_writing', '')
        ck.out('')
        if eaw != '':
            ck.out('Current "allow writing" setting: '+eaw)

        if quiet != 'yes':
            r = ck.inp(
                {'text': 'Would you like to allow explicit writing to this repository when kernel disables all writing (y/N): '})
            x = r['string'].lower()
            if x == 'yes' or x == 'y':
                d['allow_writing'] = 'yes'
                changed = True

    # Check if explicit deps
    if len(rdeps) > 0:
        if 'repo_deps' not in d:
            d['repo_deps'] = rdeps
        else:
            for q in rdeps:
                d['repo_deps'].append(q)
        changed = True

    # Print deps
    rdeps = d.get('repo_deps', [])
    if len(rdeps) > 0:
        ck.out('')
        ck.out('Current dependencies on other repositories:')
        r = print_deps({'repo_deps': rdeps, 'out': o, 'out_prefix': '  '})
        if r['return'] > 0:
            return r
        ck.out('')

    # Check if add more deps
    if quiet != 'yes':
        r = add_more_deps({})
        if r['return'] > 0:
            return r

        rdeps1 = r['repo_deps']
        if len(rdeps1) > 0:
            if 'repo_deps' not in d:
                d['repo_deps'] = rdeps1
            else:
                for q in rdeps1:
                    d['repo_deps'].append(q)
            changed = True

    # Check if need to describe for Artifact Evaluation
    if i.get('describe', '') == 'yes':
        r = describe({'dict': d})
        if r['return'] > 0:
            return r
        changed = True

    # Check if private
    private = i.get('private', '')
    if private != '':
        d['private'] = private
        changed = True

    # Check if split_all_dirs
    split_all_dirs = i.get('split_all_dirs', '')
    if split_all_dirs != '':
        d['split_all_dirs'] = split_all_dirs
        changed = True

    # Check if recache
    xrecache = i.get('recache', '')
    if xrecache != '':
        d['recache'] = xrecache
        changed = True

    # Refreshing local repository description
    if remote != 'yes':
        pcfg = os.path.join(p, ck.cfg['repo_file'])
        if os.path.isfile(pcfg):
            if o == 'con':
                ck.out('')
                ck.out('Refreshing repo info in '+pcfg+' ...')

            r = ck.load_json_file({'json_file': pcfg})
            if r['return'] > 0:
                return r

            dcfg = r['dict']

            if 'dict' not in dcfg:
                dcfg['dict'] = {}

            dcfg['dict'].update(d)

            # Clean not needed keys (local)
            for k in ['data_uid', 'data_uoa', 'data_alias', 'data_name', 'path']:
                if k in dcfg['dict']:
                    del(dcfg['dict'][k])

            r = ck.save_json_to_file(
                {'json_file': pcfg, 'dict': dcfg, 'sort_keys': 'yes'})
            if r['return'] > 0:
                return ry

            # Update back repo meta in CK
            copy_dcfg = copy.deepcopy(dcfg)
            d.update(copy_dcfg['dict'])

    # Write if changed
#    if changed or i.get('update','')=='yes':
    if o == 'con':
        ck.out('')
        ck.out('Refreshing repo info in the CK local:repo:'+duoa+' ...')

    rx = ck.access({'action': 'update',
                    'module_uoa': ck.cfg['repo_name'],
                    'data_uoa': duoa,
                    'data_name': dn,
                    'dict': d,
                    'common_func': 'yes',
                    'substitute': 'yes',
                    'skip_update': 'yes',
                    'sort_keys': 'yes'})
    if rx['return'] > 0:
        return rx

    # Recaching
    if o == 'con':
        ck.out('')
        ck.out('Recaching repos to speed up access ...')
        ck.out('')
    r = recache({'out': o})
    if r['return'] > 0:
        return r

    return {'return': 0}

##############################################################################
# Pull from shared repo if URL


def pull(i):
    """
    Input:  {
              (path)  - repo UOA (where to create entry)
              (type)  - type
              (url)   - URL

                or

              (data_uoa)      - repo UOA

              (clone)         - if 'yes', clone repo instead of update

              (current_repos) - if resolving dependencies on other repos, list of repos being updated (to avoid infinite recursion)

              (git)           - if 'yes', use git protocol instead of https

              (ignore_pull)   - useful just for switching to another branch

              (stable)        - take stable version (highly experimental)
              (version)       - checkout version (default - stable)
              (branch)        - git branch
              (checkout)      - git checkout
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    xrecache = False

    pp = []
    px = i.get('path', '')
    t = i.get('type', '')
    url = i.get('url', '')

    stable = i.get('stable', '')
    version = i.get('version', '')
    if stable == 'yes':
        version = 'stable'
    branch = i.get('branch', '')
    checkout = i.get('checkout', '')

    ip = i.get('ignore_pull', '')

    cr = i.get('current_repos', [])

    tt = 'pull'
    if i.get('clone', '') == 'yes':
        tt = 'clone'

    if px != '':
        pp.append({'path': px, 'type': t, 'url': url})

    uoa = i.get('data_uoa', '')

    cids = i.get('cids', [])
    if len(cids) > 0 and uoa == '':
        uoa = cids[0]

    if ck.cfg.get('force_lower', '') == 'yes':
        uoa = uoa.lower()

    # If url is not empty and uoa is empty, get name from URL:
    if url != '' and uoa == '' and px == '':
        ix = url.rfind('/')
        if ix > 0:
            uoa = url[ix+1:]
            if uoa.endswith('.git'):
                uoa = uoa[:-4]

            i['data_uoa'] = uoa

    if uoa == '' and len(pp) == 0 and url == '':
        uoa = '*'

    if uoa != '':
        if uoa.find('*') >= 0 or uoa.find('?') >= 0:
            r = ck.list_data(
                {'module_uoa': work['self_module_uoa'], 'data_uoa': uoa})
            if r['return'] > 0:
                return r

            lst = r['lst']
            for q in lst:
                # Loading repo
                r = ck.access({'action': 'load',
                               'module_uoa': work['self_module_uoa'],
                               'data_uoa': q['data_uoa'],
                               'common': 'yes'})
                if r['return'] > 0:
                    return r
                d = r['dict']
                t = d.get('shared', '')
                duoa = r['data_uoa']

                if d.get('recache', '') == 'yes':
                    xrecache = True

                if t != '':
                    p = d.get('path', '')
                    url = d.get('url', '')
                    checkouts = d.get('checkouts', {})
                    pp.append({'path': p, 'type': t, 'url': url,
                               'data_uoa': duoa, 'checkouts': checkouts})
        else:
            # Loading repo
            r = ck.access({'action': 'load',
                           'module_uoa': work['self_module_uoa'],
                           'data_uoa': uoa,
                           'common': 'yes'})
            if r['return'] > 0:
                if r['return'] == 16:
                    # If not found, try to add from GIT

                    i['action'] = 'add'
                    i['shared'] = 'yes'
                    x = i.get('quiet', '')
                    if x == '':
                        x = 'yes'
                    i['quiet'] = x
                    i['current_repos'] = cr

                    return add(i)
                else:
                    return r

            d = r['dict']
            duoa = r['data_uoa']

            if d.get('recache', '') == 'yes':
                xrecache = True

            p = d['path']
            t = d.get('shared', '')
            url = d.get('url', '')
            checkouts = d.get('checkouts', {})

            pp.append({'path': p, 'type': t, 'url': url,
                       'data_uoa': duoa, 'checkouts': checkouts})

    # Updating ...
    for q in pp:
        p = q.get('path', '')
        duoa = q.get('data_uoa', '')
        t = q.get('type', '')
        url = q.get('url', '')

        # Substitute all https:// with git@ to be able to save password or use ssh key
        if i.get('git', '') == 'yes' or ck.cfg.get('use_git_instead_of_https', '') == 'yes':
            url = url.replace('https://', 'git@')

            j = url.find('/')
            if j > 0:
                url = url[:j]+':'+url[j+1:]

            url += '.git'

        # Check if repository is broken
        try:
            from ck import api
            r = api.request(
                {'get': {'action': 'get-repo-status', 'data_uoa': duoa, 'url': url}})
            if r['return'] == 0:
                s = r.get('dict', {}).get('warning', '')
                if s != '':
                    ck.out(
                        '******************************************************************')
                    ck.out('Warning: '+s)
        except Exception as e:
            pass

        if o == 'con' and tt != 'clone':
            ck.out('******************************************************************')
            ck.out('Updating repo "'+duoa+'" ...')
            ck.out('')
            ck.out('  Local path: '+p)
            ck.out('  URL:        '+url)

        if t == 'git':
            # Check if git is installed
            rq = ck.gen_tmp_file({})
            if rq['return'] > 0:
                return rq
            xfn = rq['file_name']

            os.system('git --version > '+xfn)

            rq = ck.load_text_file({'text_file': xfn,
                                    'delete_after_read': 'yes'})
            xs = ''
            if rq['return'] == 0:
                xs = rq['string'].strip()

            if xs.find(' version ') < 0:
                return{'return': 1, 'error': 'git command line client is not found - please, install it or download repo as zip'}

            # Continue
            try:
                px = os.getcwd()
            except OSError:
                from os.path import expanduser
                px = expanduser("~")

            if not os.path.isdir(p):
                os.makedirs(p)

            if o == 'con':
                ck.out('')
                ck.out('  cd '+p)
            os.chdir(p)

            r = 0
            if ip != 'yes':
                s = ck.cfg['repo_types'][t][tt].replace(
                    '$#url#$', url).replace('$#path#$', p)

                if o == 'con':
                    ck.out('  '+s)
                    ck.out('')

                r = os.system(s)

                if o == 'con':
                    ck.out('')

            os.chdir(px)  # Restore path

            if r > 0:
                if o == 'con':
                    ck.out('')
                    ck.out(
                        ' WARNING: repository update likely failed OR IN A DIFFERENT BRANCH/CHECKOUT (git exit code: '+str(r)+')')
                    ck.out('')
                    rx = ck.inp(
                        {'text': 'Would you like to continue (Y/n)?: '})
                    x = rx['string'].lower()
                    if x == 'n' or x == 'no':
                        return {'return': 1, 'error': 'repository update likely failed - exit code '+str(r)}
                else:
                    return {'return': 1, 'error': 'repository update likely failed - exit code '+str(r)}
        else:
            if o == 'con':
                ck.out('CK warning: this repository is not shared!')

        # Check deps
        if tt != 'clone':  # clone is done in add ...
            if o == 'con':
                ck.out('  ========================================')
                ck.out('  Checking dependencies on other repos ...')
                ck.out('')

            r = deps({'path': p,
                      'current_path': cr,
                      'how': 'pull',
                      'version': version,
                      'branch': branch,
                      'checkout': checkout,
                      'out': o})
            if r['return'] > 0:
                return r

    # Re-caching ...
    if xrecache:
        if o == 'con':
            ck.out('  ==============================================')
            ck.out('  At least one repository requires recaching ...')
            ck.out('')

        r = recache({'out': o})
        if r['return'] > 0:
            return r

    return {'return': 0}

##############################################################################
# Push and commit to shared repo if URL


def push(i):
    """
    Input:  {
              (path)  - repo UOA (where to create entry)
              (type)  - type
              (url)   - URL

                or

              (data_uoa)  - repo UOA

              (clone) - if 'yes', clone repo instead of update
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    pp = []
    px = i.get('path', '')
    t = i.get('type', '')
    url = i.get('url', '')

    if px != '':
        pp.append({'path': px, 'type': t, 'url': url})

    uoa = i.get('data_uoa', '')
    cids = i.get('cids', [])
    if len(cids) > 0:
        uoa = cids[0]

    if uoa == '' and len(pp) == 0:
        uoa = '*'

    if ck.cfg.get('force_lower', '') == 'yes':
        uoa = uoa.lower()

    if uoa != '':
        if uoa.find('*') >= 0 or uoa.find('?') >= 0:
            r = ck.list_data(
                {'module_uoa': work['self_module_uoa'], 'data_uoa': uoa})
            if r['return'] > 0:
                return r

            lst = r['lst']
            for q in lst:
                # Loading repo
                r = ck.access({'action': 'load',
                               'module_uoa': work['self_module_uoa'],
                               'data_uoa': q['data_uoa'],
                               'common': 'yes'})
                if r['return'] > 0:
                    return r
                d = r['dict']
                t = d.get('shared', '')
                if t != '':
                    p = d.get('path', '')
                    url = d.get('url', '')
                    pp.append({'path': p, 'type': t, 'url': url})
        else:
            # Loading repo
            r = ck.access({'action': 'load',
                           'module_uoa': work['self_module_uoa'],
                           'data_uoa': uoa,
                           'common': 'yes'})
            if r['return'] > 0:
                return r
            d = r['dict']

            p = d['path']
            t = d.get('shared', '')
            url = d.get('url', '')

            pp.append({'path': p, 'type': t, 'url': url})

    # Pushing ...
    for q in pp:
        p = q.get('path', '')
        t = q.get('type', '')
        url = q.get('url', '')

        if o == 'con':
            ck.out('')
            ck.out('Trying to commit and push '+p+' ...')

        if t == 'git':
            px = os.getcwd()

            if not os.path.isdir(p):
                return {'return': 1, 'error': 'local path to repository is not found'}

            if o == 'con':
                ck.out('')
                ck.out('cd '+p+' ...')

            os.chdir(p)

            s = ck.cfg['repo_types'][t]['commit'].replace(
                '$#url#$', url).replace('$#path#$', p)
            if o == 'con':
                ck.out('')
                ck.out('Executing command: '+s)
                ck.out('')
            r = os.system(s)

            if o == 'con':
                ck.out('')

            s = ck.cfg['repo_types'][t]['push'].replace(
                '$#url#$', url).replace('$#path#$', p)
            if o == 'con':
                ck.out('')
                ck.out('Executing command: '+s)
                ck.out('')
            r = os.system(s)

            if o == 'con':
                ck.out('')

            os.chdir(px)  # Restore path

            if r > 0:
                if o == 'con':
                    ck.out('')
                    ck.out(
                        ' WARNING: repository update likely failed - exit code '+str(r))
                    ck.out('')
                    rx = ck.inp(
                        {'text': 'Would you like to continue (Y/n)?: '})
                    x = rx['string'].lower()
                    if x == 'n' or x == 'no':
                        return {'return': 1, 'error': 'repository update likely failed - exit code '+str(r)}
                else:
                    return {'return': 1, 'error': 'repository update likely failed - exit code '+str(r)}
        else:
            if o == 'con':
                ck.out('CK warning: this repository is not shared!')

    return {'return': 0}

##############################################################################
# Create repository in a given directory and record info in CK


def create(i):
    """
    See function 'add'

    """

    return add(i)

##############################################################################
# Recache all repositories in cache


def recache(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    o = i.get('out', '')

    # Listing all repos
    r = ck.access({'action': 'list',
                   'module_uoa': ck.cfg['repo_name']})
    if r['return'] > 0:
        return r
    l = r['lst']

    cru = {}
    cri = {}

    # Processing repos
    # We need 2 passes (if some repos such as remote ones are referenced inside new repos)

    for ps in [0, 1]:
        for q in l:
            if ps == 0 or (ps == 1 and q.get('processed', '') != 'yes'):
                ruoa = q['repo_uoa']
                muoa = q['module_uoa']
                duoa = q['data_uoa']
                duid = q['data_uid']

                # First try to load from cache to check that not remote ...
                remote = False
                rx = ck.load_repo_info_from_cache({'repo_uoa': duoa})
                if rx['return'] == 0:
                    rd = rx.get('dict', {})
                    if rd.get('remote', '') == 'yes':
                        remote = True

                if not remote:
                    if duid == ck.cfg['repo_uid_default'] or duid == ck.cfg['repo_uid_local']:
                        if o == 'con':
                            ck.out('Skipping repo '+duoa+' ...')
                    else:
                        if o == 'con':
                            ck.out('Processing repo '+duoa+' ...')

                        # Repo dictionary (may be changing in .ckr.json)
                        dt = {}

                        # Find real repo and get .ckr.json
                        rx = ck.access({'action': 'where',
                                        'module_uoa': muoa,
                                        'data_uoa': duoa})
                        if rx['return'] == 0:
                            pckr = os.path.join(
                                rx['path'], ck.cfg['repo_file'])
                            if os.path.isfile(pckr):
                                rx = ck.load_json_file({'json_file': pckr})
                                if rx['return'] > 0:
                                    return rx

                                dt = rx['dict']['dict']

                        # Load extra info repo (do not use repo, since may not exist in cache)
                        rx = ck.access({'action': 'load',
                                        'module_uoa': muoa,
                                        'data_uoa': duoa})
                        if rx['return'] > 0:
                            if ps == 0:
                                continue
                            else:
                                return rx

                        if len(dt) == 0:
                            dt = rx['dict']
                        else:
                            if rx['dict'].get('path', '') != '':
                                dt['path'] = rx['dict']['path']

                        dname = rx['data_name']
                        dalias = rx['data_alias']
                        dp = rx['path']

                        if duoa != duid:
                            cru[duoa] = duid

                        dd = {'dict': dt}

                        dd['data_uid'] = duid
                        dd['data_uoa'] = duoa
                        dd['data_alias'] = dalias
                        dd['data_name'] = dname
                        dd['path_to_repo_desc'] = dp

                        cri[duid] = dd

                    q['processed'] = 'yes'

        # Recording
        ck.cache_repo_uoa = cru
        ck.cache_repo_info = cri

        rx = ck.save_repo_cache({})
        if rx['return'] > 0:
            return rx

        rx = ck.reload_repo_cache({'force': 'yes'})
        if rx['return'] > 0:
            return rx

    if o == 'con':
        ck.out('')
        ck.out('Repositories were successfully recached!')

    return {'return': 0}

##############################################################################
# Remove information about repository


def rm(i):
    """
    Input:  {
              (repo_uoa)            - repo UOA (where to delete entry about repository)
              uoa                   - data UOA
              (force)               - if 'yes', force removal
              (with_files) or (all) - if 'yes', remove files as well
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    # Check if global writing is allowed
    r = ck.check_writing({})
    if r['return'] > 0:
        return r

    global cache_repo_uoa, cache_repo_info

    ruoa = i.get('repo_uoa', '')
    uoa = i.get('data_uoa', '')

    if ck.cfg.get('force_lower', '') == 'yes':
        ruoa = ruoa.lower()
        uoa = uoa.lower()

    o = i.get('out', '')

    if uoa == '':
        return {'return': 1, 'error': 'UOA of the repository is not defined'}

    wf = i.get('with_files', '')
    if wf == '':
        wf = i.get('all', '')

    force = i.get('force', '')

    r = ck.access({'action': 'load',
                   'repo_uoa': ruoa,
                   'module_uoa': work['self_module_uoa'],
                   'data_uoa': uoa,
                   'common_func': 'yes'})
    if r['return'] > 0:
        return r
    duid = r['data_uid']
    duoa = r['data_uoa']

    d = r['dict']
    p = d.get('path', '')

    to_delete = True
    if o == 'con' and force != 'yes':
        r = ck.inp(
            {'text': 'Are you sure to delete information about repository '+duoa+' (y/N): '})
        c = r['string'].lower()
        if c != 'yes' and c != 'y':
            to_delete = False

    if to_delete and o == 'con' and force != 'yes' and wf == 'yes':
        r = ck.inp(
            {'text': 'You indicated that you want to DELETE ALL ENTRIES IN THE REPOSITORY! Are you sure (y/N): '})
        x = r['string'].lower()
        if x != 'yes' and x != 'y':
            wf = ''

    if to_delete:
        if o == 'con':
            ck.out('')
            ck.out('Reloading repo cache ...')
        r = ck.reload_repo_cache({})  # Ignore errors
        if r['return'] > 0:
            return r

        if o == 'con':
            ck.out('Removing from cache ...')
        if duoa in ck.cache_repo_uoa:
            del (ck.cache_repo_uoa[duoa])
        if duid in ck.cache_repo_info:
            del (ck.cache_repo_info[duid])

        if o == 'con':
            ck.out('Rewriting repo cache ...')
        r = ck.save_repo_cache({})
        if r['return'] > 0:
            return r

        if o == 'con':
            ck.out('Removing entry ...')
        r = ck.access({'action': 'remove',
                       'repo_uoa': ruoa,
                       'module_uoa': work['self_module_uoa'],
                       'data_uoa': uoa,
                       'common_func': 'yes'})
        if r['return'] > 0:
            return r

        if wf == 'yes' and p != '':
            if o == 'con':
                ck.out('Removing entries from the repository ...')
            import shutil
            if os.path.isdir(p):
                shutil.rmtree(p, onerror=ck.rm_read_only)

        if o == 'con':
            ck.out('')
            ck.out('Information about repository was removed successfully!')
            if wf != 'yes':
                ck.out('Note: repository itself was not removed!')

    return {'return': 0}

##############################################################################
# Remove information about repository


def remove(i):
    """
    Input:  { See 'rm' function }
    Output: { See 'rm' function }
    """

    return rm(i)

##############################################################################
# Remove information about repository


def delete(i):
    """
    Input:  { See 'rm' function }
    Output: { See 'rm' function }
    """

    return rm(i)

##############################################################################
# find path to a local repository


def where(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    duoa = i.get('data_uoa', '')

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa = duoa.lower()

    r = ck.find_path_to_repo({'repo_uoa': duoa})
    if r['return'] > 0:
        return r

    d = r.get('dict', {})
    url = d.get('url', '')

    p = r['path']
    if p == '':
        p = url

    if o == 'con':
        ck.out(p)

    return r

##############################################################################
# archive repository


def zip(i):
    """
    Input:  {
              data_uoa       - repo UOA

              (archive_path) - if '' create inside repo path

              (archive_name) - if !='' use it for zip name
              (auto_name)    - if 'yes', generate name name from data_uoa: ckr-<repo_uoa>.zip
              (bittorent)    - if 'yes', generate zip name for BitTorrent: ckr-<repo_uid>-YYYYMMDD.zip

              (overwrite)    - if 'yes', overwrite zip file
              (store)        - if 'yes', store files instead of packing


              (data)         - CID allowing to add only these entries with pattern (can be from another archive)

              (all)          - archive all files
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    duoa1 = i.get('data_uoa', '')

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa1 = duoa1.lower()

    duid = ''
    path = ''

    if duoa1 != '':
        # Find path to repo
        r = ck.find_path_to_repo({'repo_uoa': duoa1})
        if r['return'] > 0:
            return r

        duoa = r['repo_uoa']
        duid = r['repo_uid']
        path = r['path']

    an = i.get('archive_name', '')
#    if an=='': an='ckr.zip'

    if i.get('auto_name', '') == 'yes':
        an = 'ckr'
        if duoa != '':
            an += '-'+duoa
        an += '.zip'
    elif i.get('bittorrent', '') == 'yes':
        import time
        an = 'ckr-'
        if duid != '':
            an += duid
        an += '-'+time.strftime('%Y%m%d')+'.zip'
    elif an == '':
        if duoa1 == '':
            an = 'ckr.zip'
        else:
            an = 'ckr-'+duoa1+'.zip'

    ap = i.get('archive_path', '')
#    if ap=='': ap=path

    pfn = os.path.join(ap, an)

    if pfn.startswith('~'):
        from os.path import expanduser
        home = expanduser("~")

        pfn = os.path.abspath(home+os.sep+pfn[1:])

    if os.path.isfile(pfn):
        if i.get('overwrite', '') == 'yes':
            os.remove(pfn)
        else:
            return {'return': 1, 'error': 'archive '+pfn+' already exists'}

    if o == 'con':
        ck.out('Creating archive '+pfn +
               ' - please wait, it may take some time ...')

    # Check all files
    ignore = []
    if i.get('all', '') != 'yes':
        ignore = ck.cfg.get('ignore_directories_when_archive_repo', [])

    # Prepare archive
    import zipfile

    zip_method = zipfile.ZIP_DEFLATED
    if i.get('store', '') == 'yes':
        zip_method = zipfile.ZIP_STORED

    # Prepare list of files
    fl = {}

    data = i.get('data', '')
    if data != '':
        xpm = {}

        rx = ck.access({'action': 'search',
                        'cid': data})
        if rx['return'] > 0:
            return rx
        lst = rx['lst']
        for q in lst:
            pp = q['path']

            pm1, pd = os.path.split(pp)
            pr, pm = os.path.split(pm1)

            if pr not in fl:
                fl[pr] = []

            ry = ck.find_path_to_entry({'path': pr, 'data_uoa': pm})
            if ry['return'] > 0:
                return ry
            pm_uid = ry['data_uid']
            pm_alias = ry['data_alias']

            if pm_alias != '':
                if pm_alias not in xpm:
                    xpm[pm_alias] = pm_uid
                    fl[pr].append(os.path.join(
                        ck.cfg['subdir_ck_ext'], ck.cfg['file_alias_a'] + pm_alias))
                    fl[pr].append(os.path.join(
                        ck.cfg['subdir_ck_ext'], ck.cfg['file_alias_u'] + pm_uid))

            ry = ck.find_path_to_entry({'path': pm1, 'data_uoa': pd})
            if ry['return'] > 0:
                return ry
            pd_uid = ry['data_uid']
            pd_alias = ry['data_alias']

            if pd_alias != '':
                fl[pr].append(os.path.join(
                    pm, ck.cfg['subdir_ck_ext'], ck.cfg['file_alias_a'] + pd_alias))
                fl[pr].append(os.path.join(
                    pm, ck.cfg['subdir_ck_ext'], ck.cfg['file_alias_u'] + pd_uid))

            r = ck.list_all_files(
                {'path': pp, 'all': 'yes', 'ignore_names': ignore})
            if r['return'] > 0:
                return r
            for q in r['list']:
                fx = os.path.join(pm, pd, q)
                fl[pr].append(fx)

    else:
        r = ck.list_all_files(
            {'path': path, 'all': 'yes', 'ignore_names': ignore})
        if r['return'] > 0:
            return r
        fl[path] = r['list']

    # Write archive
    try:
        f = open(pfn, 'wb')
        z = zipfile.ZipFile(f, 'w', zip_method)
        for path in fl:
            fl1 = fl[path]
            for fn in fl1:
                p1 = os.path.join(path, fn)
                z.write(p1, fn, zip_method)
        z.close()
        f.close()

    except Exception as e:
        return {'return': 1, 'error': 'failed to prepare archive ('+format(e)+')'}

    return {'return': 0}

##############################################################################
# unzip entries to a given repo


def unzip(i):
    """
    Input:  {
              (data_uoa)    - repo UOA where to unzip (default, if not specified)
              zip           - path to zipfile (local or remote http/ftp)
              (overwrite)   - if 'yes', overwrite files when unarchiving
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    duoa = i.get('data_uoa', '')
    if duoa == '':
        duoa = 'local'

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa = duoa.lower()

    overwrite = i.get('overwrite', '')

    zip_ = i.get('zip', '')
    if zip_ == '':
        zip_ = 'ckr.zip'

    # Check if exists
    if not os.path.isfile(zip_):
       return {'return':1, 'error':'file "'+zip_+'" not found'}

    # Find path to repo
    r = ck.find_path_to_repo({'repo_uoa': duoa})
    if r['return'] > 0:
        return r

    path = r['path']

    # Unzipping archive
    rz = get_and_unzip_archive(
        {'zip': zip_, 'path': path, 'overwrite': overwrite, 'out': o})
    if rz['return'] > 0:
        return rz

    return {'return': 0}

##############################################################################
# received from web (if needed) and unzip archive


def get_and_unzip_archive(i):
    """
    Input:  {
              zip              - zip filename or URL
              path             - path to extract
              (overwrite)      - if 'yes', overwrite files when unarchiving
              (path_to_remove) - if !='', remove this part of the path from extracted archive
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    zp = i['zip']
    p = i['path']
    pr = i.get('path_to_remove', '')

    overwrite = i.get('overwrite', '')

    # If zip, get (download) and unzip file ...
    rm_zip = False
    if zp.find('://') >= 0:
        if o == 'con':
            ck.out('Downloading CK archive ('+zp+') - it may take some time ...')

        rm_zip = True

        # Generate tmp file
        import tempfile
        # suffix is important - CK will delete such file!
        fd, fn = tempfile.mkstemp(suffix='.tmp', prefix='ck-')
        os.close(fd)
        os.remove(fn)

        # Import modules compatible with Python 2.x and 3.x
        import urllib

        try:
            import urllib.request as urllib2
        except:
            import urllib2

        # Prepare request
        request = urllib2.Request(zp)

        # Connect
        try:
            f = urllib2.urlopen(request)
        except Exception as e:
            return {'return': 1, 'error': 'Failed downloading CK archive ('+format(e)+')'}

        import time
        t = time.time()
        t0 = t

        chunk = 32767
        size = 0

        try:
            fo = open(fn, 'wb')
        except Exception as e:
            return {'return': 1, 'error': 'problem opening file='+fn+' ('+format(e)+')'}

        # Read from Internet
        try:
            while True:
                s = f.read(chunk)
                if not s:
                    break
                fo.write(s)

                size += len(s)

                if o == 'con' and (time.time()-t) > 3:
                    speed = '%.1d' % (size/(1000*(time.time()-t0)))
                    ck.out('  Downloaded '+str(int(size/1000)) +
                           ' KB ('+speed+' KB/sec.) ...')
                    t = time.time()

            f.close()
        except Exception as e:
            return {'return': 1, 'error': 'Failed downlading CK archive ('+format(e)+')'}

        fo.close()

        zp = fn

    # Unzip if zip
    if zp != '':
        if o == 'con':
            ck.out('  Extracting to '+p+' ...')

        import zipfile
        f = open(zp, 'rb')
        z = zipfile.ZipFile(f)

        # First, try to find .ckr.json
        xprefix = ''
        for dx in z.namelist():
            if pr != '' and dx.startswith(pr):
                dx = dx[len(pr):]
            if dx.endswith(ck.cfg['repo_file']):
                xprefix = dx[:-len(ck.cfg['repo_file'])]
                break

        # Second, extract files
        for dx in z.namelist():
            dx1 = dx
            if pr != '' and dx1.startswith(pr):
                dx1 = dx1[len(pr):]
            if xprefix != '' and dx1.startswith(xprefix):
                dx1 = dx1[len(xprefix):]

            if dx1 != '':
                pp = os.path.join(p, dx1)
                if dx.endswith('/'):
                    # create directory
                    if not os.path.exists(pp):
                        os.makedirs(pp)
                else:
                    # extract file
                    ppd = os.path.dirname(pp)
                    if not os.path.exists(ppd):
                        os.makedirs(ppd)

                    if os.path.isfile(pp) and overwrite != 'yes':
                        if o == 'con':
                            ck.out(
                                'File '+dx+' already exists in the entry - skipping ...')
                    else:
                        fo = open(pp, 'wb')
                        fo.write(z.read(dx))
                        fo.close()
        f.close()

        if rm_zip:
            os.remove(zp)

    return {'return': 0}

##############################################################################
# import repo from current path


def import_repo(i):
    """
    Input:  {
              See action 'add' where import=yes
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['import'] = 'yes'
    return add(i)

##############################################################################
# resolve dependencies for a repo


def deps(i):
    """
    Input:  {
              (data_uoa)      - repo UOA
                  or
              (path)          - path to .cmr.json

              (current_repos) - list of repos being updated (to avoid infinite recursion)

              (how)           - 'pull' (default) or 'add'

              (version)       - checkout version (default - stable)
              (branch)        - git branch
              (checkout)      - git checkout
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o = i.get('out', '')

    duoa = i.get('data_uoa', '')

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa = duoa.lower()

    # Added repos to avoid duplication/recursion
    cr = i.get('current_repos', [])

    how = i.get('how', '')
    if how == '':
        how = 'pull'

    p = i.get('path', '')
    if p == '':
        r = ck.access({'action': 'load',
                       'module_uoa': work['self_module_uoa'],
                       'data_uoa': duoa})
        if r['return'] > 0:
            return r
        dr = r['dict']
        p = dr.get('path', '')

    if p != '':
        # path to repo description
        pp = os.path.join(p, ck.cfg['repo_file'])
        if os.path.isfile(pp):
            r = ck.load_json_file({'json_file': pp})
            if r['return'] > 0:
                return r

            d = r['dict']

            # Check checkouts
            version = i.get('version', '')
            branch = i.get('branch', '')
            checkout = i.get('checkout', '')

            if version != '':
                cx = d.get('dict', {}).get('checkouts', {}).get(version, {})
                branch = cx.get('branch', '')
                checkout = cx.get('checkout', '')

            ppp = os.getcwd()

            os.chdir(p)

            if branch != '':
                if o == 'con':
                    ck.out('  ====================================')
                    ck.out('  git checkout '+branch)
                    ck.out('')

                r = ck.run_and_get_stdout({'cmd': ['git', 'checkout', branch]})
                ck.out(r.get('stdout', ''))
                ck.out(r.get('stderr', ''))

            if checkout != '':
                if o == 'con':
                    ck.out('  ====================================')
                    ck.out('  git checkout '+checkout)
                    ck.out('')

                r = ck.run_and_get_stdout(
                    {'cmd': ['git', 'checkout', checkout]})
                ck.out(r.get('stdout', ''))
                ck.out(r.get('stderr', ''))

            os.chdir(ppp)

            rp1 = d.get('dict', {}).get('repo_deps', [])
            if len(rp1) == 0:
                rp1 = d.get('repo_deps', [])  # for backwards compatibility ...

            rp2 = []
            rp = []

            if len(rp1) > 0:
                for xruoa in rp1:
                    if type(xruoa) != list:  # for backwards compatibility
                        ruoa = xruoa.get('repo_uoa', '')
                        if xruoa.get('repo_uid', '') != '':
                            ruoa = xruoa['repo_uid']
                        if ruoa != '' and ruoa not in cr:
                            rp2.append(xruoa)

            # Add dependencies on other repositories (but avoid duplication)
            if len(rp2) == 0:
                if o == 'con':
                    ck.out('  No dependencies on other repositories found!')
            else:
                for xruoa in rp2:
                    ruoa = xruoa.get('repo_uoa', '')
                    if xruoa.get('repo_uid', '') != '':
                        ruoa = xruoa['repo_uid']
                    rurl = xruoa.get('repo_url', '')
                    if ruoa != '':
                        x = '  Dependency on repository '+ruoa+' '

                        # Check if this repo exists
                        r = ck.access({'action': 'load',
                                       'module_uoa': work['self_module_uoa'],
                                       'data_uoa': ruoa})
                        if r['return'] > 0:
                            if r['return'] != 16:
                                return r
                            rp.append(xruoa)
                            x += ': should be resolved ...'
                        else:
                            # If explicit branch, still add !
                            branch = xruoa.get('branch', '')
                            checkout = xruoa.get('checkout', '')
                            stable = xruoa.get('stable', '')
                            version = xruoa.get('version', '')

                            if branch != '' or checkout != '' or stable != '' or version != '':
                                xruoa['ignore_pull'] = 'yes'
                                rp.append(xruoa)
                                x += ': should be switched to explicit branch ...'
                            else:
                                x += ': Ok'

                        if o == 'con':
                            ck.out(x)

            if len(rp) > 0:
                for xruoa in rp:
                    ruoa = xruoa.get('repo_uoa', '')
                    ruid = xruoa.get('repo_uid', '')
                    rurl = xruoa.get('repo_url', '')

                    branch = xruoa.get('branch', '')
                    checkout = xruoa.get('checkout', '')
                    stable = xruoa.get('stable', '')
                    version = xruoa.get('version', '')

                    ignore_pull = xruoa.get('ignore_pull', '')

                    if o == 'con':
                        ck.out('')
                        x = ''
                        if ruid != '':
                            x = ' ('+ruid+')'
                        ck.out('  Resolving dependency on repo: '+ruoa+x)
                        ck.out('')

                    if ruid != '':
                        cr.append(ruid)
                    else:
                        cr.append(ruoa)

                    ii = {'action': how,
                          'module_uoa': work['self_module_uoa'],
                          'data_uoa': ruoa,
                          'current_repos': cr,
                          'url': rurl,
                          'ignore_pull': ignore_pull,
                          'branch': branch,
                          'checkout': checkout,
                          'stable': stable,
                          'version': version,
                          'out': o}
                    if ruid != '':
                        ii['data_uid'] = ruid
                    if how == 'add':
                        ii['gitzip'] = 'yes'
                    r = ck.access(ii)
                    if r['return'] > 0:
                        return r

    return {'return': 0, 'current_repos': cr}

##############################################################################
# print dependencies on other shared repositories


def print_deps(i):
    """
    Input:  {
              data_uoa                   - data UOA of the repo
                 or
              repo_deps                  - dict with dependencies on other shared repos

              (out_prefix)               - output prefix befor each string
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              repo_deps
            }

    """

    o = i.get('out', '')

    op = i.get('out_prefix', '')

    duoa = i.get('data_uoa', '')
    if duoa != '':
        # Get configuration
        r = ck.load_repo_info_from_cache({'repo_uoa': duoa})
        if r['return'] > 0:
            return r

        d = r['dict']
        rp1 = d.get('dict', {}).get('repo_deps', [])
    else:
        rp1 = i['repo_deps']

    if len(rp1) == 0:
        rp1 = d.get('repo_deps', [])  # for compatibility ...

    if o == 'con' and len(rp1) > 0:
        for q in rp1:
            ruoa = q.get('repo_uoa', '')
            ruid = q.get('repo_uid', '')
            rurl = q.get('repo_url', '')

            x = op+ruoa
            if ruid != '':
                x += '; '+ruid
            elif rurl != '':
                x += '; '
            if rurl != '':
                x += '; '+rurl

            ck.out(x)

    return {'return': 0, 'repo_deps': rp1}

##############################################################################
# add more dependencies


def add_more_deps(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              repo_deps    - list with dependencies on other repositories ...
            }

    """

    rp = []

    r = ck.inp(
        {'text': 'Would you like to add extra dependencies on other shared repositories (y/N)?: '})
    x = r['string'].lower()
    if x == 'yes' or x == 'y':
        ck.out('')
        ck.out('Use the following format: repo UOA; (repo UID) (; repo URL)')
        ck.out('For example:')
        ck.out('  ck-autotuning')
        ck.out(
            '  ck-dissemination-modules;;https://github.com/gfursin/ck-dissemination-modules.git')
        ck.out('')
        ck.out('Press Enter to stop adding repositories!')
        ck.out('')

        while True:
            r = ck.inp({'text': ''})
            x = r['string'].strip()
            if x == '':
                break

            z = {}

            y = x.split(';')
            if len(y) > 0:
                z['repo_uoa'] = y[0].strip()
                if len(y) > 1:
                    z['repo_uid'] = y[1].strip()
                    if len(y) > 2:
                        z['repo_url'] = y[2].strip()

            if len(z) > 0:
                rp.append(z)

    return {'return': 0, 'repo_deps': rp}

##############################################################################
# Find location of the repository (see ticket #45)
# Technically speaking it doesn't follow CK concept
# to always find path to CK entries (and thus to the repo description),
# but it is more intuitive.
# That's why we also added option --meta to revert back
# to original functionality and find path to repo meta


def find(i):
    """
    Input:  {
              (meta)       - if 'yes', return location of repo entry with meta
                             rather than path to the repository
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    if i.get('meta', '') != 'yes':
        i['action'] = 'where'
    else:
        i['common_func'] = 'yes'

    return ck.access(i)

##############################################################################
# renew repository (remove fully and pull again)


def renew(i):
    """
    Input:  {
              data_uoa                   - data UOA of the repo

              (stable)                   - take stable version (highly experimental)
              (checkout)                 - checkout (default - stable)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if global writing is allowed
    r = ck.check_writing({})
    if r['return'] > 0:
        return r

    o = i.get('out', '')

    duoa = i.get('data_uoa', '')
    if duoa == '':
        return {'return': 1, 'error': 'repository UOA is not specified'}

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa = duoa.lower()

    # Get configuration (not from Cache - can be outdated info!)
#    r=ck.load_repo_info_from_cache({'repo_uoa':duoa})
    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uoa'],
                   'data_uoa': duoa})
    if r['return'] > 0:
        return r

    p = r.get('dict', {}).get('path', '')
    d = r['dict']
    dn = r.get('data_name', '')

    shared = d.get('shared', '')
    url = d.get('url', '')

    if shared != 'git' and url == '':
        return {'return': 1, 'error': 'this repository is not shared and can not be renewed'}

    # first delete
    ii = {'action': 'rm',
          'module_uoa': work['self_module_uoa'],
          'data_uoa': duoa,
          'all': 'yes'}
    if o == 'con':
        ii['out'] = 'con'
    r = ck.access(ii)
    if r['return'] > 0:
        return r

    # pull again
    ii = {'action': 'pull',
          'module_uoa': work['self_module_uoa'],
          'data_uoa': duoa,
          'data_name': dn,
          'url': url,
          'stable': i.get('stable', ''),
          'checkout': i.get('checkout', '')}
    if o == 'con':
        ii['out'] = 'con'
    return ck.access(ii)

##############################################################################
# show remote repo in a browser


def browse(i):
    """
    Input:  {
              data_uoa                   - data UOA of the repo
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    duoa = i.get('data_uoa', '')
    if duoa == '':
        return {'return': 1, 'error': 'repository UOA is not specified'}

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa = duoa.lower()

    # Get configuration (not from Cache - can be outdated info!)
#    r=ck.load_repo_info_from_cache({'repo_uoa':duoa})
    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uoa'],
                   'data_uoa': duoa})
    if r['return'] > 0:
        return r

    p = r.get('dict', {}).get('path', '')
    d = r['dict']
    dn = r.get('data_name', '')

    shared = d.get('shared', '')
    url = d.get('url', '')

    if shared != 'git' and url == '':
        return {'return': 1, 'error': 'this repository is not shared'}

    import webbrowser
    webbrowser.open(url)

    return {'return': 0}

##############################################################################
# describe repository for Artifact Evaluation


def describe(i):
    """
    Input:  {
              (dict)  - dict with current repo description
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              (dict)  - updated dict with current repo description
            }

    """

    d = i.get('dict', {})

    a = d.get('artifact_pack_description', {})

    ck.out('')
    ck.out('Please, provide description of your artifact pack (see http://cTuning.org/ae for more details):')
    ck.out('')

    r = ck.inp(
        {'text': 'Enter title of your artifact pack (or associated paper): '})
    x = r['string']
    if x != '':
        a['title'] = x

    r = ck.inp({'text': 'List contributors: '})
    x = r['string']
    if x != '':
        a['contributors'] = x

    r = ck.inp({'text': 'Enter artifact abstract: '})
    x = r['string']
    if x != '':
        a['description'] = x

    r = ck.inp({'text': 'Enter license of the whole artifact pack: '})
    x = r['string']
    if x != '':
        a['license'] = x

    r = ck.inp({'text': 'Enter version/revision of the whole artifact pack: '})
    x = r['string']
    if x != '':
        a['version'] = x

    r = ck.inp({'text': 'How delivered (URL, DOI, OCRID, etc): '})
    x = r['string']
    if x != '':
        a['how_delivered'] = x

    r = ck.inp({'text': 'Describe software dependencies: '})
    x = r['string']
    if x != '':
        a['software_dependencies'] = x

    r = ck.inp({'text': 'Describe hardware dependencies: '})
    x = r['string']
    if x != '':
        a['hardware_dependencies'] = x

    r = ck.inp({'text': 'Describe data sets: '})
    x = r['string']
    if x != '':
        a['datasets'] = x

    r = ck.inp({'text': 'Describe installation procedure: '})
    x = r['string']
    if x != '':
        a['installation'] = x

    r = ck.inp({'text': 'Describe possible experiment parameterization: '})
    x = r['string']
    if x != '':
        a['parameterization'] = x

    r = ck.inp({'text': 'Describe experiment workflow: '})
    x = r['string']
    if x != '':
        a['experiment_workflow'] = x

    r = ck.inp({'text': 'Describe evaluation procedure and expected output: '})
    x = r['string']
    if x != '':
        a['evaluation'] = x

    r = ck.inp({'text': 'Acknowledgments: '})
    x = r['string']
    if x != '':
        a['acknowledgments'] = x

    r = ck.inp({'text': 'Misc notes: '})
    x = r['string']
    if x != '':
        a['notes'] = x

    d['artifact_pack_description'] = a

    return {'return': 0, 'dict': d}

##############################################################################
# form URL from hostname, hostext and port


def form_url(i):
    """
    Input:  {
              (url)                      - if type=='remote' or 'git', URL of remote repository or git repository
              (hostname)                 - if !='', automatically form url above (add http:// + /ck?)
              (port)                     - if !='', automatically add to url above
              (hostext)                  - if !='', add to the end of above URL instead of '/ck?' -
                                           useful when CK server is accessed via Apache2, IIS or other web servers
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              url          - formed URL
            }

    """

    url = i.get('url', '')

    if i.get('hostname', '') != '':
        url = 'http://'+i['hostname']

        if i.get('port', '') != '':
            url += ':'+i['port']

        if i.get('hostext', '') != '':
            url += '/'+i['hostext']
        else:
            url += '/ck?'

    return {'return': 0, 'url': url}

##############################################################################
# show repositories and their status


def show(i):
    """
    Input:  {
              (data_uoa) - repo UOA

              (reset)    - if 'yes', reset repos

              (stable)   - take stable version (highly experimental)
              (version)  - checkout version (default - stable)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o = i.get('out', '')

    curdir = os.getcwd()

    duoa = i.get('data_uoa', '')

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa = duoa.lower()

    reset = i.get('reset', '')

    stable = i.get('stable', '')
    version = i.get('version', '')
    if stable == 'yes':
        version = 'stable'

    r = ck.list_data({'module_uoa': work['self_module_uoa'],
                      'data_uoa': duoa})
    if r['return'] > 0:
        return r

    if o == 'con':
        ck.out('Please wait - it may take some time ...')
        ck.out('')

    r = ck.reload_repo_cache({})  # Ignore errors

    # Init header.
    pp = [({'branch': 'branch', 'origin': 'origin', 'checkout': 'local',
            'path': 'path', 'type': 'type', 'url': 'url', 'data_uoa': 'data_uoa'})]
    il = 0
    for q in ck.cache_repo_info:
        # Get repo info
        qq = ck.cache_repo_info[q]

        d = qq['dict']

        t = d.get('shared', '')

        if t != '':
            duoa = qq['data_uoa']

            if len(duoa) > il:
                il = len(duoa)

            p = d.get('path', '')
            url = d.get('url', '')

            branch = ''
            origin = ''
            checkout = ''

            if os.path.isdir(p):
                # Detect status
                os.chdir(p)

                if reset == 'yes':
                    r = ck.run_and_get_stdout(
                        {'cmd': ['git', 'checkout', 'master']})

                if version != '':
                    cx = qq.get('dict', {}).get(
                        'checkouts', {}).get(version, {})
                    branch = cx.get('branch', '')
                    checkout = cx.get('checkout', '')

                    if branch != '':
                        r = ck.run_and_get_stdout(
                            {'cmd': ['git', 'checkout', branch]})

                    if checkout != '':
                        r = ck.run_and_get_stdout(
                            {'cmd': ['git', 'checkout', checkout]})

                # FGG TBD: we may need to add explicit check for branch/checkout in repo_deps here?
                # OR MAYBE NOT - need to think ...

                # Get current branch
                r = ck.run_and_get_stdout(
                    {'cmd': ['git', 'rev-parse', '--abbrev-ref', 'HEAD']})
                if r['return'] == 0 and r['return_code'] == 0:
                    branch = r['stdout'].strip()

                # Get origin hash
                r = ck.run_and_get_stdout(
                    {'cmd': ['git', 'rev-parse', '--short', 'origin/HEAD']})
                if r['return'] == 0 and r['return_code'] == 0:
                    origin = r['stdout'].strip()

                # Get current hash (append '-dirty' on dirty working tree)
                r = ck.run_and_get_stdout(
                    {'cmd': ['git', 'describe', '--match=NeVeRmAtCh', '--always', '--abbrev', '--dirty']})
                if r['return'] == 0 and r['return_code'] == 0:
                    checkout = r['stdout'].strip()

            pp.append({'branch': branch, 'origin': origin, 'checkout': checkout,
                       'path': p, 'type': t, 'url': url, 'data_uoa': duoa})

    # Print
    for q in pp:
        name = q['data_uoa']

        x = name+' '*(il-len(name))

        branch = q.get('branch', '')
        origin = q.get('origin', '')
        checkout = q.get('checkout', '')
        url = q.get('url', '')

        if branch != '' or 'origin' or checkout != '' or url != '':
            x += ' ( '+branch+' ; '+origin+' ; '+checkout+' ; '+url+' )'

        ck.out(x)

    os.chdir(curdir)

    return {'return': 0}

##############################################################################
# reset git repos to default branch and latest checkout (or specific one)


def reset(i):
    """
    Input:  {
              (data_uoa) - repository UOA

              (stable)        - take stable version (highly experimental)
              (version)       - checkout version (default - stable)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['reset'] = 'yes'

    return show(i)

##############################################################################
# rename repo


def ren(i):
    """
    Input:  {
              data_uoa  - repo UOA

              (new_data_uoa)
                 or
              xcids[0]           - {'data_uoa'} - new data UOA
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    duoa = i.get('data_uoa', '')

    if duoa == '':
        return {'return': 1, 'error': 'repo is not defined'}

    if ck.cfg.get('force_lower', '') == 'yes':
        duoa = duoa.lower()

    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uid'],
                   'data_uoa': duoa})
    if r['return'] > 0:
        return r

    dd = r['dict']
    dp = r['path']
    duoa_real = r['data_uoa']
    dname = r['data_name']

    nduoa = i.get('new_data_uoa', '')

    if nduoa == '':
        xcids = i.get('xcids', [])
        if len(xcids) > 0:
            xcid = xcids[0]
            nduoa = xcid.get('data_uoa', '')

    if nduoa == '':
        xcids = i.get('cids', [])
        if len(xcids) > 0:
            nduoa = xcids[0]

    if nduoa == '':
        return {'return': 1, 'error': 'new repo name is not defined'}

    if ck.cfg.get('allowed_entry_names', '') != '':
        import re

        anames = ck.cfg.get('allowed_entry_names', '')

        if not re.match(nduoa, a):
            return {'return': 1, 'error': 'found disallowed characters in names (allowed: "'+anames+'")'}

    if ck.cfg.get('force_lower', '') == 'yes':
        nduoa = nduoa.lower()

    if nduoa == 'local' or nduoa == 'default':
        return {'return': 1, 'error': 'new repo name already exists'}

    # Check if such repo doesn't exist
    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uid'],
                   'data_uoa': nduoa})
    if r['return'] == 0:
        return {'return': 1, 'error': 'repo already exists'}

    # Update .ckr.json
    dpp = dd.get('path', '')
    if dpp != '':
        pckr = os.path.join(dpp, ck.cfg['repo_file'])

        r = ck.load_json_file({'json_file': pckr})
        if r['return'] > 0:
            return r

        dckr = r['dict']

        x = dckr.get('data_uoa', '')
        if x != '' and x == duoa_real:
            dckr['data_uoa'] = nduoa

        x = dckr.get('data_alias', '')
        if x != '' and x == duoa_real:
            dckr['data_alias'] = nduoa

        x = dckr.get('data_name', '')
        if x != '' and x == duoa_real:
            dckr['data_name'] = nduoa

        r = ck.save_json_to_file({'json_file': pckr, 'dict': dckr})
        if r['return'] > 0:
            return r

    # Rename repo entry using internal command
    r = ck.access({'action': 'ren',
                   'module_uoa': work['self_module_uid'],
                   'data_uoa': duoa,
                   'new_data_uoa': nduoa,
                   'common_func': 'yes'})
    if r['return'] > 0:
        return r

    # Recache repos
    r1 = recache({'out': o})
    if r1['return'] > 0:
        return r1

    return r

##############################################################################
# rename repo


def rename(i):
    """
    Input:  {
               See "ck ren repo --help"
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return ren(i)

##############################################################################
# copy repo (forbidden)


def copy(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return cp(i)

##############################################################################
# copy repo (forbidden)


def cp(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return {'return': 1, 'error': 'copying CK repositories is forbidden to avoid duplication of CK entries. Create a new one instead and move CK entries there'}

##############################################################################
# init CK repo in a given directory


def new_init(i):
    """
    Input:  {
              (data_uoa) - repo name
              (data_uid) - repo UID
              (url)      - URL if shared
              (deps)     - list of deps on other repositories separated by comma
              (path)     - path where to initialize a repository
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if global writing is allowed
    r = ck.check_writing({})
    if r['return'] > 0:
        return r

    # Check output
    o = i.get('out', '')
    oo = ''
    if o == 'con':
        oo = o

    # Check path
    path = os.getcwd()
    if i.get('path', '') != '':
        path = i['path']
        if not os.path.isdir(path):
            return {'return': 1, 'error': 'path not found'}

    # Check name
    data_uoa = i.get('data_uoa', '')
    data_uid = i.get('data_uid', '')

    if data_uoa == '':
        # Check from .ckr.json
        pckr = os.path.join(path, ck.cfg['repo_file'])
        if os.path.isfile(pckr):
            r = ck.load_json_file({'json_file': pckr})
            if r['return'] > 0:
                return r
            d = r['dict']

            data_uoa = d.get('data_uoa', '')
            data_uid = d.get('data_uid', '')

            if data_uoa != '':
                ck.out('Detected CK repo name: '+data_uoa)

    if data_uoa == '':
        # Try to detect from .ckr.json
        r = ck.inp({'text': 'Enter CK repository name: '})
        if r['return'] > 0:
            return r
        data_uoa = r['string'].strip()

    # Check if already exists
    exists = False
    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uid'],
                   'data_uoa': data_uoa})
    if r['return'] > 0 and r['return'] != 16:
        return r
    if r['return'] == 0:
        exists = True

        r = ck.inp({'text': 'CK repository "'+data_uoa +
                    '" already exists. Update (y/N)? '})
        if r['return'] > 0:
            return r
        s = r['string'].strip().lower()

        if s == '' or s == 'n' or s == 'no':
            return {'return': 1, 'error': 'CK repository already exists'}

    # Check URL
    url = i.get('url', '')
    if url == '':
        # Attempt to check from current Git dir
        pgit = os.path.join(path, '.git', 'config')
        if os.path.isfile(pgit):
            r = ck.load_text_file({'text_file': pgit, 'split_to_list': 'yes'})
            if r['return'] > 0:
                return r
            ll = r['lst']

            for l in ll:
                l = l.strip()
                if l.startswith('url ='):
                    url = l[5:].strip()
                    ck.out('Detected URL: '+url)
                    break

    # prepare deps
    repo_deps = []

    deps = i.get('deps', '').strip().split(',')

    for q in deps:
        q = q.strip()
        if q != '':
            repo_deps.append({'repo_uoa': q})

    # Create or update repo
    ii = {'module_uoa': work['self_module_uid'],
          'data_uoa': data_uoa,
          'quiet': 'yes',
          'path': path,
          'out': oo}

    if data_uid != '':
        ii['data_uid'] = data_uid

    if exists:
        ii['action'] = 'update'
    else:
        ii['action'] = 'add'

    if url != '':
        ii['shared'] = 'yes'
        ii['url'] = url

    if len(repo_deps) > 0:
        ii['repo_deps'] = repo_deps

    r = ck.access(ii)
    return r
