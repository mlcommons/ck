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
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return': 0}

##############################################################################
# Add module


def add(i):
    """
    Input:  {
              (repo_uoa)          - repo UOA
              module_uoa          - normally should be 'module' already
              data_uoa            - UOA of the module to be created

              (desc)              - module description
              (license)           - module license
              (copyright)         - module copyright
              (developer)         - module developer
              (developer_email)   - module developer
              (developer_webpage) - module developer
              (actions)           - dict with actions {"func1":{}, "func2":{} ...}
              (actions_redirect)  - dict with actions redrect {"func":"real func", ...}
              (dict)              - other meta description to add to entry

              (quiet)             - minimal interaction
              (func)              - just add one dummy action
              (support_web)       - if 'yes', make it a web API, i.e. allow an access to this function in the CK server
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output of the 'add' kernel function
            }

    """

    # Check if global writing is allowed
    r = ck.check_writing({'module_uoa': work['self_module_uoa']})
    if r['return'] > 0:
        return r

    o = i.get('out', '')

    # Find path to module 'module' to get dummies
    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uoa'],
                   'data_uoa': work['self_module_uoa'],
                   'common_func': 'yes'})
    if r['return'] > 0:
        return r
    p = r['path']

    pm = os.path.join(p, cfg['dummy_module'])
    pma = os.path.join(p, cfg['dummy_module_action'])

    # Load module dummy
    r = ck.load_text_file({'text_file': pm})
    if r['return'] > 0:
        return r
    spm = r['string']

    # Load module action dummy
    r = ck.load_text_file({'text_file': pma})
    if r['return'] > 0:
        return r
    spma = r['string']

    # Prepare meta description
    desc = i.get('desc', '')
    license = i.get('license', '')
    copyright = i.get('copyright', '')
    developer = i.get('developer', '')
    developer_email = i.get('developer_email', '')
    developer_webpage = i.get('developer_webpage', '')
    actions = i.get('actions', {})
    actions_redirect = i.get('actions_redirect', {})

    func = i.get('func', '')
    if func != '':
        if ck.cfg.get('allowed_action_names', '') != '':
            import re

            anames = ck.cfg.get('allowed_action_names', '')

            if not re.match(anames, func):
                return {'return': 1, 'error': 'found disallowed characters in the action name (allowed: "'+anames+'")'}

        if '-' in func:
            func1 = func.replace('-', '_')
            actions_redirect[func] = func1

        actions[func] = {}

    quiet = i.get('quiet', '')

    # If console mode, ask some questions
    if quiet != 'yes' and o == 'con':
        if desc == '':
            ck.out('')
            r = ck.inp({'text': 'Add brief module description: '})
            desc = r['string']

        if license == '' and ck.cfg.get('default_license', '') != '':
            ck.out('')
            r = ck.inp(
                {'text': 'Add brief module license (or Enter to use "'+ck.cfg['default_license']+'"): '})
            license = r['string']
            if license == '':
                license = ck.cfg['default_license']

        if copyright == '' and ck.cfg.get('default_copyright', '') != '':
            ck.out('')
            r = ck.inp(
                {'text': 'Add brief module copyright (or Enter to use "'+ck.cfg['default_copyright']+'"): '})
            copyright = r['string']
            if copyright == '':
                copyright = ck.cfg['default_copyright']

        if developer == '' and ck.cfg.get('default_developer', '') != '':
            ck.out('')
            r = ck.inp(
                {'text': 'Add module\'s developer (or Enter to use "'+ck.cfg['default_developer']+'"): '})
            developer = r['string']
            if developer == '':
                developer = ck.cfg['default_developer']

        if developer_email == '' and ck.cfg.get('default_developer_email', '') != '':
            ck.out('')
            r = ck.inp({'text': 'Add module\'s developer email (or Enter to use "' +
                        ck.cfg['default_developer_email']+'"): '})
            developer_email = r['string']
            if developer_email == '':
                developer_email = ck.cfg['default_developer_email']

        if developer_webpage == '' and ck.cfg.get('default_developer_webpage', '') != '':
            ck.out('')
            r = ck.inp({'text': 'Add module\'s developer webpage (or Enter to use "' +
                        ck.cfg['default_developer_webpage']+'"): '})
            developer_webpage = r['string']
            if developer_webpage == '':
                developer_webpage = ck.cfg['default_developer_webpage']

        if len(actions) == 0:
            act = '*'
            while act != '':
                ck.out('')

                r = ck.inp(
                    {'text': 'Add action function (or Enter to stop): '})
                act = r['string'].strip()
                if act != '':

                    if ck.cfg.get('allowed_action_names', '') != '':
                        import re

                        anames = ck.cfg.get('allowed_action_names', '')

                        if not re.match(anames, act):
                            return {'return': 1, 'error': 'found disallowed characters in the action name (allowed: "'+anames+'")'}

                    actions[act] = {}

                    if '-' in act:
                        act1 = act.replace('-', '_')
                        actions_redirect[act] = act1

                    fweb = i.get('support_web', '')
                    if fweb != '':
                        if fweb != 'yes':
                            fweb = ''

#                r1=ck.inp({'text':'Support web (y/N): '})
#                x=r1['string'].lower()
#                if x=='yes' or x=='y':
#                   fweb='yes'
                    if fweb != '':
                        actions[act]['for_web'] = fweb

                    r1 = ck.inp({'text': 'Add action description: '})
                    adesc = r1['string']
                    if adesc != '':
                        actions[act]['desc'] = adesc

    ck.out('')

    # Prepare meta description
    dd = {}
    if desc != '':
        dd['desc'] = desc
    spm = spm.replace('$#desc#$', desc)

    if license != '':
        dd['license'] = license
    spm = spm.replace('$#license#$', license)

    if copyright != '':
        dd['copyright'] = copyright
    spm = spm.replace('$#copyright#$', copyright)

    dev = ''
    if developer != '':
        dev = developer
        dd['developer'] = developer

    if developer_email != '':
        if dev != '':
            dev += ', '
        dev += developer_email
        dd['developer_email'] = developer_email

    if developer_webpage != '':
        if dev != '':
            dev += ', '
        dev += developer_webpage
        dd['developer_webpage'] = developer_webpage

    spm = spm.replace('$#developer#$', dev)

    dd['actions'] = actions
    if len(actions_redirect) > 0:
        dd['actions_redirect'] = actions_redirect

    # Substitute actions
    for act in actions:
        adesc = actions[act].get('desc', 'TBD: action description')
        if act in actions_redirect:
            act = actions_redirect[act]
        spm += '\n'+spma.replace('$#action#$', act).replace('$#desc#$', adesc)

    dx = i.get('dict', {})

    r = ck.merge_dicts({'dict1': dx, 'dict2': dd})
    if r['return'] > 0:
        return r

    # Add entry (it will ask further questions about alias and user-friendly name)
    i['common_func'] = 'yes'
    i['dict'] = dx
    i['sort_keys'] = 'yes'
    r = ck.access(i)
    if r['return'] > 0:
        return r

    # Add module code
    p = r['path']
    pf = os.path.join(p, ck.cfg['module_full_code_name'])

    if o == 'con':
        ck.out('')
        ck.out('Creating module code '+pf+' ...')

    # Write module code
    rx = ck.save_text_file({'text_file': pf, 'string': spm})
    if rx['return'] > 0:
        return rx

    return r

##############################################################################
# show info about modules
# Notice that we now suggest to use "ck list_modules misc"


def show(i):
    """
    Input:  {
               (the same as list; can use wildcards)


            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    of = i.get('out_file', '')
    if of != '':
        xof = os.path.splitext(of)

    html = False
    if o == 'html' or i.get('web', '') == 'yes':
        html = True

    h = ''

    unique_repo = False
    if i.get('repo_uoa', '') != '':
        unique_repo = True

    import copy
    ii = copy.deepcopy(i)

    ii['out'] = ''
    ii['action'] = 'list'
    ii['add_meta'] = 'yes'

    rx = ck.access(ii)
    if rx['return'] > 0:
        return rx

    ll = sorted(rx['lst'], key=lambda k: k['data_uoa'])

    if html:
        h += 'You can install and reuse CK modules as follows:\n'
        h += '<pre>\n'
        h += ' ck pull repo:{Repo UOA - see below}\n'
        h += ' ck help {module UOA - see below}\n'
        h += '</pre>\n'

        h += 'You can check a JSON API of a given action of a given module as follows:\n'
        h += '<pre>\n'
        h += ' ck {module action - see below} {module UOA} --help\n'
        h += '</pre>\n'

        h += 'You can add your own dummy CK module as follows:\n'
        h += '<pre>\n'
        h += ' ck add module:{my module alias}\n'
        h += '</pre>\n'

        h += 'You can add a new action to the CK module as follows:\n'
        h += '<pre>\n'
        h += ' ck add_action module:{my module alias}\n'
        h += '</pre>\n'

        h += 'See <a href="https://github.com/ctuning/ck/wiki">CK documentation</a>\n'
        h += ' and the latest <a href="http://cKnowledge.org/rpi-crowd-tuning">CK paper</a> for further details.\n'

        h += '<p>\n'
        h += '<table cellpadding="4" border="1" style="border-collapse: collapse; border: 1px solid black;">\n'

        h += ' <tr>\n'
        h += '  <td nowrap><b>#</b></td>\n'
        h += '  <td nowrap><b>Module&nbsp;UOA with JSON API<br>(Python module/wrapper/plugin)</b></td>\n'
        h += '  <td nowrap><b>Repo UOA</b></td>\n'
        h += '  <td><b>Description and actions</b></td>\n'
        h += ' </tr>\n'

    repo_url = {}
    repo_private = {}

    private = ''
    num = 0
    for l in ll:
        ln = l['data_uoa']
        lr = l['repo_uoa']

        lr_uid = l['repo_uid']
        url = ''
        if lr == 'default':
            url = 'https://github.com/ctuning/ck/tree/master/ck/repo'
        elif lr_uid in repo_url:
            url = repo_url[lr_uid]
        else:
            rx = ck.load_repo_info_from_cache({'repo_uoa': lr_uid})
            if rx['return'] > 0:
                return rx
            url = rx.get('dict', {}).get('url', '')
            repo_private[lr_uid] = rx.get('dict', {}).get('private', '')
            repo_url[lr_uid] = url

        private = repo_private.get(lr_uid, '')

#        if lr not in cfg.get('skip_repos',[]) and private!='yes' and url!='':
        if lr not in cfg.get('skip_repos', []) and private != 'yes' and url != '':
            num += 1

            lm = l['meta']
            ld = lm.get('desc', '')

            actions = lm.get('actions', {})

            if lr == 'default':
                to_get = ''
            elif url.find('github.com/ctuning/') > 0:
                to_get = 'ck pull repo:'+lr
            else:
                to_get = 'ck pull repo --url='+url

            ###############################################################
            if html:
                h += ' <tr>\n'

                x1 = ''
                x2 = ''
                z1 = ''
                z11 = ''
                if url != '':
                    x1 = '<a href="'+url+'">'
                    x2 = '</a>'

                    url2 = url

                    if url2.endswith('.git'):
                        url2 = url2[:-4]

                    if '/tree/master/' not in url2:
                        url2 += '/tree/master/module/'
                    else:
                        url2 += '/module/'

                    z1 = '<a href="'+url2+ln+'/module.py">'
                    z11 = '<a href="'+url2+ln+'/.cm/meta.json">'

                h += '  <td nowrap valign="top"><a name="' + \
                    ln+'">'+str(num)+'</b></td>\n'

                h += '  <td nowrap valign="top">'+z1+ln+x2 + \
                    '</b> <i>('+z11+'CK meta'+x2+')</i></td>\n'

                h += '  <td nowrap valign="top"><b>'+x1+lr+x2+'</b></td>\n'

                h += '  <td valign="top">'+ld+'\n'

                if len(actions) > 0:
                    h += '<ul>\n'
                    for q in sorted(actions):
                        qq = actions[q]
                        qd = qq.get('desc', '')
                        h += '<li>"ck <i>'+q+'</i> '+ln+'"'
                        if qd != '':
                            h += ' - '+qd
                    h += '</ul>\n'

                h += '</td>\n'

                h += ' </tr>\n'

            ###############################################################
            elif o == 'mediawiki':
                x = lr
                if url != '':
                    x = '['+url+' '+lr+']'
                ck.out('')
                ck.out('=== '+ln+' ('+lr+') ===')
                ck.out('')
                ck.out('Desc: '+ld)
                ck.out('<br>CK Repo URL: '+x)
                if to_get != '':
                    ck.out('<br>How to get: <i>'+to_get+'</i>')
                ck.out('')
                if len(actions) > 0:

                    ck.out('Actions (functions):')
                    ck.out('')

                    for q in sorted(actions):
                        qq = actions[q]
                        qd = qq.get('desc', '')
                        ck.out('* \'\''+q+'\'\' - '+qd)

            ###############################################################
            elif o == 'con' or o == 'txt':
                if unique_repo:
                    ck.out('')
                    s = ln+' - '+ld

                else:
                    ss = ''
                    if len(ln) < 35:
                        ss = ' '*(35-len(ln))

                    ss1 = ''
                    if len(lr) < 30:
                        ss1 = ' '*(30-len(lr))

                    s = ln+ss+'  ('+lr+')'
                    if ld != '':
                        s += ss1+'  '+ld

                ck.out(s)

                if len(actions) > 0:
                    ck.out('')
                    for q in sorted(actions):
                        qq = actions[q]
                        qd = qq.get('desc', '')
                        ck.out('  * '+q+' - '+qd)

    if html:
        h += '</table>\n'

        if of != '':
            r = ck.save_text_file({'text_file': of, 'string': h})
            if r['return'] > 0:
                return r

    return {'return': 0, 'html': h}
