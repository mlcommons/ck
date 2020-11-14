#
# Collective Knowledge (Grigori's misc research functions)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

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
    return {'return':0}


##############################################################################
# Just a centralized place to get a home directory

def get_home_dir(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    from os.path import expanduser
    home_dir = expanduser("~")

    if i.get('out', '') == 'con':
        ck.out(home_dir)

    return {'return':0, 'home_dir':home_dir}


##############################################################################
# Replace string in file

def replace_string_in_file(i):
    """
    Input:  {
              file
              (file_out)  - if !='', use this file for output, otherwise overwrite original one!
              string      - string to replace
              replacement - replacement string
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              (updated)    - if 'yes', files was updated
            }

    """

    import copy

    o=i.get('out','')

    fin=i['file']
    s1=i['string']
    s2=i['replacement']

    fout=i.get('file_out','')
    if fout=='': fout=fin

    rx=ck.load_text_file({'text_file':fin})
    if rx['return']>0: return rx

    s=rx['string']
    sx=s.replace(s1,s2)

    r={'return':0, 'updated':'no'}

    if s!=sx or fin!=fout:
       r=ck.save_text_file({'text_file':fout, 'string':sx})
       r['updated']='yes'

    return r

##############################################################################
# updating json file

def refresh_json(i):
    """
    Input:  {
              json_file     - file with json
              (output_file) - if !='' use this file for output instead of rewriting original file
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    jf=i['json_file']

    of=i.get('output_file','')
    if of=='': of=jf

    r=ck.load_json_file({'json_file':jf})
    if r['return']>0: return r

    d=r['dict']

    return ck.save_json_to_file({'json_file':of, 'dict':d, 'sort_keys':'yes'})

##############################################################################
# process all files recursively using some action

def process_all_files_recursively(i):
    """
    Input:  {
               (path)     - starting path (or current)
               (pattern)  - file pattern
               (cmd)      - perform action with a file

               (ck)       - call CK access
               (file_key) - substitute this key in 'ck' with file name with full path
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')

    p=i.get('path','')
    if p=='':
       p=os.getcwd()

    cka=i.get('ck',{})
    fk=i.get('file_key','')

    pat=i.get('pattern','')

    if o=='con':
       ck.out('')
       x=''
       if pat!='': x=' ('+pat+')'
       ck.out('Obtaining list of all files'+x+'. May take some time ...')

    r=ck.list_all_files({'path':p, 'pattern':pat, 'all':'yes'})
    if r['return']>0: return r

    lst=r['list']

    for qq in lst:
        if p=='': q=qq
        else:     q=os.path.join(p,qq)

        if len(cka)>0:
           if fk!='':
              cka[fk]=q

           if o=='con':
              ck.out('  '+q)

           r=ck.access(cka)
           if r['return']>0: return r

    return {'return':0, 'list':lst}

##############################################################################
# merge dictionaries in 2 files

def merge_dicts(i):
    """
    Input:  {
              file1   - dict1
              file2   - dict2
              (file3) - output to this file. If empty use file1
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    f1=i.get('file1','')
    f2=i.get('file2','')

    if f1=='' or f2=='':
       return {'return':1, 'error':'--file1 and --file2 should be specified'}

    fo=i.get('file3','')
    if fo=='': fo=f1

    r=ck.load_json_file({'json_file':f1})
    if r['return']>0: return r
    d1=r['dict']

    r=ck.load_json_file({'json_file':f2})
    if r['return']>0: return r
    d2=r['dict']

    if type(d1)==list and type(d2)==list:
       for q in d2:
           d1.append(q)
    else:
       r=ck.merge_dicts({'dict1':d1, 'dict2':d2})
       if r['return']>0: return r
       d1=r['dict1']

    r=ck.save_json_to_file({'json_file':fo, 'dict':d1})
    if r['return']>0: return r

    return {'return':0}

##############################################################################
# sort JSON file

def sort_json_file(i):
    """
    Input:  {
              json_file     - file with json
              (output_file) - if !='' use this file for output instead of rewriting original file
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return refresh_json(i)

##############################################################################
# add key to meta/files of different entries

def add_key(i):
    """
    Input:  {
              data            - CID of entries to update (can be wild cards)
              (tags)          - prune entries by tags

              key             - key in flat format
              value           - value

              (ignore_update) - ignore update info in entries
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    data=i.get('data','')
    if data=='':
       return {'return':1, 'error':'"data" is not defined'}

    tags=i.get('tags','')

    key=i.get('key','')
    if key=='':
       return {'return':1, 'error':'"key" is not defined'}

    value=i.get('value','')
    if value=='':
       return {'return':1, 'error':'"value" is not defined'}

    iu=i.get('ignore_update','')

    # Search entries
    r=ck.access({'action':'search',
                 'cid':data,
                 'tags':tags})
    if r['return']>0: return r
    lst=r['lst']

    llst=len(lst)

    if llst>0 and o=='con':
       ck.out('Updating '+str(llst)+' entries ...')
       ck.out('')

    # Iterate over entries
    for l in lst:
        ruid=l['repo_uid']
        ruoa=l['repo_uoa']
        muid=l['module_uid']
        muoa=l['module_uoa']
        duid=l['data_uid']
        duoa=l['data_uoa']

        if o=='con':
           ck.out('* '+ruoa+':'+muoa+':'+duoa)

        # Load meta
        r=ck.access({'action':'load',
                     'repo_uoa':ruid,
                     'module_uoa':muid,
                     'data_uoa':duid})
        if r['return']>0: return r
        d=r['dict']

        # Updating dict
        r=ck.set_by_flat_key({'dict':d,
                              'key':key,
                              'value':value})
        if r['return']>0: return r

        # Store meta
        r=ck.access({'action':'update',
                     'repo_uoa':ruid,
                     'module_uoa':muid,
                     'data_uoa':duid,
                     'dict':d,
                     'substitute':'yes',
                     'ignore_update':iu})
        if r['return']>0: return r

    return {'return':0}

##############################################################################
# internal file to ignore files/directories from templates

def prepare_entry_template_ignore_files(dr, files):
    lst=['.cm','tmp']
    return lst

##############################################################################
# prepare template for a given entry
# (trying to unify templates for CK when adding program, soft, package, program, dataset, etc)

def prepare_entry_template(i):
    """
    Input:  {
              original_module_uoa - add template for this original module 
              (template)          - force using this template
              (skip_custom_note)  - if 'yes', do not print note about customization at the end

              all params from "ck add" function
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import shutil

    o=i.get('out','')
    oo=''
    if o=='con': oo=o

    omuoa=i.get('original_module_uoa','')
    ruoa=i.get('repo_uoa','')
    duoa=i.get('data_uoa','')

    # Check user-friendly name
    if duoa=='' and o=='con':
       r=ck.inp({'text': 'Enter alias for your entry without spaces such as "tool.cmake": '})
       if r['return']>0: return r
       duoa=r['string'].strip()
       i['data_uoa']=duoa
       ck.out('')

    # Search templates
    tuoa=i.get('template','')
    truoa=i.get('template_repo','')

    if tuoa=='':
       lst=[{'data_uid':'', 'data_uoa':'', 'repo_uid':'', 'info':{'data_name':'Empty entry'}, 'meta':{'sort':9999}}] # Add it to the end

       c=None

       if tuoa=='':
          if oo=='con':
             ck.out('Searching for templates ...')

          ii={'action':'search',
              'module_uoa':omuoa,
              'data_uoa':tuoa,
              'add_info':'yes',
              'add_meta':'yes',
              'search_dict':{'template':'yes'}}
          r=ck.access(ii)
          if r['return']>0: return r

          lst+=r['lst']

       if len(lst)==1:
          c=lst[0]

       # Make selection
       if oo=='con' and len(lst)>1:
          ck.out('')

          r=select_uoa({'text':'Select template for the new entry', 
                        'choices':lst})
          if r['return']>0: return r

          c=r['choice']

          ck.out('')

       if c!=None:
          tuoa=c['data_uid']
          truoa=c['repo_uid']

    d=i.get('dict',{})

    if tuoa!='':
       # Attempt to load entry
       ii={'action':'load',
           'module_uoa':omuoa,
           'data_uoa':tuoa,
           'repo_uoa':truoa}
       r=ck.access(ii)
       if r['return']>0: return r

       p=os.path.realpath(r['path'])

       d.update(r['dict'])

    i['action']='add'
    i['module_uoa']=omuoa

    i['common_func']='yes'
    i['sort_keys']='yes'

    i['dict']=d
    
    r=ck.access(i)
    if r['return']>0: return r

    pnew=r['path']

    # Copy files to a new entry if template
    if tuoa!='':
       d=os.listdir(p)
       for f in d:
           if f!='.cm' and not f.endswith('.pyc') and 'tmp' not in f:
              porig2=os.path.join(p,f)
              pnew2=os.path.join(pnew,f)

              try:

                 if os.path.isdir(porig2):
                    shutil.copytree(porig2, pnew2, ignore=shutil.ignore_patterns('.cm', '*tmp*', '*.pyc'))
                 else:
                    shutil.copyfile(porig2, pnew2)

              except IOError as e: 
                 return {'return':1, 'error':'problem copying files from template ('+str(e)+')'}

    # Print info about customization
    if i.get('skip_custom_note', '')!='yes' and oo=='con':
       ck.out('')
       ck.out('DO NOT FORGET to finish manually updating this JSON meta (tags, paths, dependencies, etc):')
       ck.out('')
       ck.out(' * JSON meta:   '+os.path.join(pnew, ck.cfg['subdir_ck_ext'], ck.cfg['file_meta']))
       ck.out(' * Other files: '+pnew)

    return r

##############################################################################
# Universal string selector.
#
# Given an ordered list of options (strings)

def select_string(i):
    """
    Input:  {
                options         - an ordered list of strings to select from
                (question)      - the question to ask
                (default)       - default selection
                (no_autoselect) - if "yes", enforce the interactive choice even if there is only 1 option
                (no_autoretry)  - if "yes", bail out on any unsuitable input, do not offer to retry
                (no_skip_line)  - if "yes", do not skip a line after each option
                (first_match)   - if "yes", take the first match in case there are multiple
            }

    Output: {
                selected_index  - an index < len(options)
                selected_value  - the string value at selected_index

                return          - return code =  0, if successful
                                              >  0, if error
                (error)         - error text if return > 0
            }

    """

    import copy

    question    = i.get('question', 'Please select from the options above')
    options     = copy.deepcopy( i.get('options') )
    default     = i.get('default', None)
    auto_select = i.get('no_autoselect', '') != 'yes'
    auto_retry  = i.get('no_autoretry', '') != 'yes'
    skip_line   = i.get('no_skip_line', '') != 'yes'
    first_match = i.get('first_match', '') == 'yes'

    if not options or len(options)==0:
        return {'return': 1, 'error': 'No options provided - please check the docstring for correct syntax'}

    num_options = len(options)

    for j in range(num_options):
        if not isinstance(options[j], list):
            options[j] = [ options[j] ]

        ck.out("{:>2}) {}".format(j, options[j][0]))
        for extra_line in options[j][1:]:
            ck.out('    {}'.format(extra_line))
        if skip_line:
            ck.out('')

    ck.out('')
    num_matches = 0

    if len(options)==1 and auto_select:
        ck.out('Since there is only one option, auto-selecting it')
        response = '0'
        selected_index = 0
        num_matches = 1

    while num_matches!=1:

        r = ck.inp({'text': "{}{}: ".format(question, ' [ hit return for "{}" ]'.format(default) if default!=None and len(default) else '')})
        response = r['string']

        if response=='' and default!=None:
            response = default

        try:                                    # try to convert into int() and see if it works
            error_message = None

            selected_index = int(response)
            if selected_index < num_options:
                num_matches = 1
            else:
                error_message = 'Selected index is out of range [0..{}]'.format(num_options-1)
        except:
            num_matches = 0
            for j in reversed(range(num_options)):
                if response in options[j][0]:
                    selected_index = j
                    num_matches += 1

            if num_matches>1 and first_match:
                break
            elif num_matches!=1:
                error_message = 'Instead of 1 unique match there were {}'.format(num_matches)

        if error_message:
            if auto_retry:
                ck.out( error_message + ", please try again" )
            else:
                return { 'return': 1, 'response': response, 'error': error_message }

    selected_value = options[selected_index][0] if selected_index >= 0 else ''

    if i.get('out')=='con':
        ck.out('You selected [{}] == "{}"'.format(selected_index, selected_value))

    return { 'return':0, 'response': response, 'selected_index': selected_index, 'selected_value': selected_value }


##############################################################################
# Search for entries of a specific type using a mix of tags AND variations
#

def search_in_variations(i):
    """
    Input:  {
                tags                - the query, a mixture of tags and variations
                (query_module_uoa)  - entries of which type to search for
                (add_info)          - each entry found will also contain 'info' dictionary ('meta' is obligatory)
            }

    Output: {
                lst             - a list of entries found (may be empty)

                return          - return code =  0, if successful
                                              >  0, if error
                (error)         - error text if return > 0
            }

    """

    tags        = i.get('tags')
    module_uoa  = i.get('query_module_uoa', '*')
    add_info    = i.get('add_info', '')

    required_tags_list = tags
    if not type(required_tags_list)==list:
        required_tags_list = required_tags_list.split(',')

    required_tags_set = set(required_tags_list)   # NB: this variable gets locked in the closure for efficiency of the following function:

    def tags_and_variations_merging_callback(i):
        """ A callback function that knows how to merge tags and variations
            and how to match the resulting set against the query.
        """

        meta = i.get('meta',{})
        supported_variations_set    = set(meta.get('variations',{}).keys())
        tags_and_variations         = set(meta.get('tags',{})) | supported_variations_set

        matched_bool                = tags_and_variations >= required_tags_set
        i['required_variations']    = list( supported_variations_set & required_tags_set )

        return { 'return': 0, 'skip': ( '' if matched_bool else 'yes' ) }

    r=ck.access({'action':'list',
                   'module_uoa': module_uoa,
                   'add_meta':'yes',
                   'add_info':add_info,
                   'download_tags':tags, # These tags are not influencing main functionality but used for auto-download of components from the CK platform
                   'filter_func_addr': tags_and_variations_merging_callback,
    })

    if r['return']>0: return r
    if i.get('out')=='con':
        for entry in r['lst']:
            print("{}:{}:{}".format(entry['repo_uoa'], entry['module_uoa'], entry['data_uoa']))

    return r


##############################################################################
# List variations of an entry or a group of entries
#

def list_variations(i):
    """
    Input:  {
                tags                - the query, a mixture of tags and variations
                (query_module_uoa)  - entries of which type to search for
                (variation_prefix)  - an optional prefix to filter the variations
                (separator)         - an optional string to separate the results (BEWARE: CK does not support trailing spaces!)
            }

    Output: {
                return          - return code =  0, if successful
                                              >  0, if error
                (error)         - error text if return > 0
            }

    """

    tags                = i.get('tags')
    query_module_uoa    = i.get('query_module_uoa', '*')
    variation_prefix    = i.get('variation_prefix', '')
    separator           = i.get('separator', '\n')

    r=ck.access({'action':'search_in_variations',
                   'module_uoa': 'misc',
                   'query_module_uoa': query_module_uoa,
                   'tags': tags,
    })
    if r['return']>0: return r

    # merge all available variations into a set:
    variations_found = set()
    for entry_dict in r['lst']:
        variations_found |= set(entry_dict['meta'].get('variations',{}).keys())

    # collect the matching ones into a list
    variations_found = [variation for variation in variations_found if variation.startswith(variation_prefix)]

    if i.get('out')=='con':
        print(separator.join(variations_found))

    return {'return':0, 'variations':variations_found}



##############################################################################
# Universal UOA selector (improved version forked 
# from ck-autotuning:module:choice and ck.kernel)

def select_uoa(i):
    """
    Input:  {
              choices      - list from search function
              (text)       - selection text
              (skip_enter) - if 'yes', do not select 0 when user presses Enter
              (skip_sort)  - if 'yes', do not sort array
            }

    Output: {
              return  - return code =  0, if successful
                                    >  0, if error
              (error) - error text if return > 0
              choice  - {dict of selection from lst}
            }

    """

    se=i.get('skip_enter','')

    lst=i.get('choices',[])

    # Prepare data_name and then data_uoa

    if i.get('skip_sort','')!='yes':
       slst=sorted(lst, key=lambda v: (v.get('meta',{}).get('sort',0), v.get('info',{}).get('data_name',''), v['data_uoa']))
    else:
       slst=lst

    array={}
    n=0

    for x in slst:
        sn=str(n)
        array[sn]=x

        duoa=x['data_uoa']
        name=x.get('info',{}).get('data_name','')
        if name=='': name=duoa

        s=sn+') '+name
        if duoa!='': s+=' (--template='+duoa+')'

        ck.out(s)

        n+=1

    ck.out('')

    text=i.get('text','')
    if text=='': text='Select UOA'

    s=text
    if se!='yes': s+=' (or press Enter for 0)'
    s+=': '

    rx=ck.inp({'text':s})
    y=rx['string'].strip()

    if y=='' and se!='yes': y='0' 

    if y not in array:
       return {'return':1, 'error':'number is not recognized'}

    return {'return':0, 'choice':array[y]}

##############################################################################
# list CK kernel functions

def list_kernel_functions(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy

    o=i.get('out','')

    of=i.get('out_file','')
    if of!='':
       xof=os.path.splitext(of)

    html=False
    if o=='html' or i.get('web','')=='yes':
       html=True

    h=''
    h2=''
    hcfg=''
    if i.get('new','')=='yes':
       ii=copy.deepcopy(i)
       ii['ck_title']='Shared CK kernel functions and configurations'
       r=preload_html_for_lists(ii)
       if r['return']>0: return r

       h=r['html_start']+'\n'
       h2=r['html_stop']+'\n'

       hcfg=h

    p=ck.work['env_root'] # Internal CK path

    pk=os.path.join(p, 'ck', 'kernel.py')
    if not os.path.isfile(pk):
       return {'return':1, 'error':'Can\'t find kernel in '+pk}

    r=ck.load_text_file({'text_file':pk, 'split_to_list':'yes'})
    if r['return']>0: return r

    l=r['lst']

    funcs={}
    desc=[]
    ld=0
    target=''

    cfg=[]
    cfg_start=False

    ll=len(l)
    for k in range(0, ll):
        x=l[k]

        if x.startswith('cfg={'):
           cfg_start=True

        if cfg_start:
           cfg.append(x)
           if x=='    }':
              cfg_start=False

        if x.startswith('##################'):
           desc=[]
           ld=k

        if x.startswith('# '):
           x1=x[2:].strip()
           if x1.startswith('TARGET: '):
              target=x1[8:]
           else:
              desc.append(x1)

        if x.startswith('def '):
           j1=x.find('(')
           j2=x.find(')', j1+1)
           j3=x.find(':')

           fn=x[4:j1]
           i=x[j1+1:j2]
           rem=x[j3+1:]

           api=[]

           k+=1

           found=False
           first=False
           while not found or k<ll:
              x=l[k]
              if x.strip().startswith('"""'):
                 if first:
                    found=True
                    break
                 else:
                    first=True
              elif first:
                 api.append(x)
              k+=1
           
           if found:
              funcs[fn]={'api':api,
                         'input':i,
                         'rem':rem,
                         'desc':desc,
                         'line':ld,
                         'target':target}

           api=[]
           desc=[]
           target=''

    # Process functions
    if html:
       h+='We encourage you to reuse these portable productivity functions (Python 2.6+ and 3+) from the CK modules or in your own Python scripts:\n'
       h+='\n'
       h+='<pre>\n'
       h+='    import ck.kernel as ck\n'
       h+='\n'
       h+='    ck.out("Hello world")\n'
       h+='\n'
       h+='    r=ck.access({"action":"ls", "module_uoa":"env", "out":"con"})\n'
       h+='    if r["return"]>0: ck.err(r)\n'
       h+='    print (r["lst"])\n'
       h+='\n'
       h+='    r=ck.load_json_file({"json_file":"my_file.json", "dict":{"test":"yes"}})\n'
       h+='    if r["return"]>0: return r\n'
       h+='\n'
       h+='    r=ck.save_text_file({"text_file":"my_file.txt", "string":"test=yes\\n"})\n'
       h+='    if r["return"]>0: return r\n'
       h+='\n'
       h+='</pre>\n'

       h+='See <a href="https://github.com/ctuning/ck/wiki">CK documentation for further details</a>.\n'

       h+='<p>\n'
       h+='<table cellpadding="4" border="1" style="border-collapse: collapse; border: 1px solid black;">\n'

       h+=' <tr>\n'
       h+='  <td nowrap><b>#</b></td>\n'
       h+='  <td nowrap><b>Function name</b></td>\n'
       h+='  <td nowrap><b>Note and API</b></td>\n'
       h+=' </tr>\n'

    hdev=h

    num1=0
    num2=0
    for f in sorted(funcs):
        x=funcs[f]

        api=x['api']
        i=x['input']
        rem=x['rem']
        line=x['line']
        desc=x['desc']
        target=x['target']

        xapi='<i>'
        for y in desc:
            j=y.find('\\n=')
            if j>=0: 
               y=y[:j]
            xapi+=y
        xapi+='</i>\n'

        xapi+='<p>\n'
        xapi+='<pre>\n'
        for y in api:
            xapi+=y+'\n'
        xapi+='</pre>\n'

        url='https://github.com/ctuning/ck/blob/master/ck/kernel.py'

        x=''
        if target!='':
           x+='<p>&nbsp;&nbsp;&nbsp;<i>for '+target+'</i>'

        if 'end users' in target or 'end-users' in target:
           num1+=1
           num=num1
        else:
           num2+=1
           num=num2

        zh=' <tr>\n'
        zh+='  <td nowrap valign="top"><a name="'+f+'">'+str(num)+'</td>\n'
        zh+='  <td nowrap valign="top"><a href="'+url+'#L'+str(line+1)+'"><b>ck.'+f+'('+i+')</b></a>'+x+'</b></td>\n'
        zh+='  <td nowrap valign="top">'+xapi+'</td>\n'
        zh+=' </tr>\n'

        if 'end users' in target or 'end-users' in target:
           h+=zh
        else:
           hdev+=zh

    # Prepare config
    hcfg+='You can access the following CK internal variables:\n'
    hcfg+='\n'
    hcfg+='<pre>\n'
    hcfg+='    import ck.kernel as ck\n'
    hcfg+='\n'
    hcfg+='    print (ck.cfg)\n'
    hcfg+='</pre>\n'

    hcfg+='See <a href="https://github.com/ctuning/ck/wiki">CK documentation for further details</a>.\n'

    hcfg+='<p>\n'
    hcfg+='<pre>\n'
    for x in cfg:
        hcfg+=x+'\n'
    hcfg+='</pre>\n'
    hcfg+=h2

    if html:
       h+='</table>\n'
       h+=h2
       hdev+='</table>\n'
       hdev+=h2

       if of!='':
          r=ck.save_text_file({'text_file':of+'.html', 'string':h})
          if r['return']>0: return r

          r=ck.save_text_file({'text_file':of+'-dev.html', 'string':hdev})
          if r['return']>0: return r

          r=ck.save_text_file({'text_file':of+'-dev-cfg.html', 'string':hcfg})
          if r['return']>0: return r

    return {'return':0}

##############################################################################
# list repositories

def list_repos(i):
    """
    Input:  {
               (the same as ck search; can use wildcards)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy

    o=i.get('out','')

    of=i.get('out_file','')
    if of!='':
       xof=os.path.splitext(of)

    html=False
    if o=='html' or i.get('web','')=='yes':
       html=True

    h=''
    h2=''
    if i.get('new','')=='yes':
       ii=copy.deepcopy(i)
       ii['ck_title']='Shared CK repositories'
       r=preload_html_for_lists(ii)
       if r['return']>0: return r

       h=r['html_start']+'\n'
       h2=r['html_stop']+'\n'

    unique_repo=False
    if i.get('repo_uoa','')!='': unique_repo=True

    import copy
    ii=copy.deepcopy(i)

    ii['out']=''
    ii['module_uoa']=cfg['module_deps']['repo']
    ii['action']='list'
    ii['add_meta']='yes'
    ii['time_out']=-1

    rx=ck.access(ii)
    if rx['return']>0: return rx

    ll=rx['lst']

    if html:
       h+='<h2>Please check our new <a href="http://ReuseResearch.com/c.php?c=repo">beta browser</a> for CK components!</h2>\n'

       h+='<br>\n'

       h+='<p>Users share their reusable CK components (code, data, models) and workflows/pipelines using CK-compatible repositories and archives\n'
       h+='(for example, see this <a href="https://github.com/dividiti/ck-rpi-optimization">CK repository</a>\n'
       h+='with a complete compiler crowd-tuning workflow, an <a href="http://cKnowledge.org/rpi-crowd-tuning">automatically generated interactive article</a>,\n'
       h+='and a <a href="http://cKnowledge.org/dashboard">public interactive dashboard</a>).\n'
       h+='Most of them are shared with the permissive 3-clause BSD license or CC-BY to accelerate technology transfer!\n'

       h+='<p>You can run and reuse workflows, <a href="http://cKnowledge.org/shared-modules.html">modules</a> and other components with a common API from below repositories:\n'
       h+='<pre>\n'
       h+=' ck pull repo:{Repo UOA - see below}\n'
       h+='</pre>\n'

       h+='<p>You can add dependency on a given repository in your own CK repository by editing your .ckr.json file as follows:\n'
       h+='<pre>\n'
       h+=' {\n'
       h+='   ...\n'
       h+='   "dict": {\n'
       h+='      "repo_deps": [\n'
       h+='         {\n'
       h+='           "repo_uoa": "ck-tensorflow",\n'
       h+='           "repo_url": "https://github.com/ctuning/ck-tensorflow"\n'
       h+='         }\n'
       h+='         ...\n'
       h+='      ]\n'
       h+='      ...\n'
       h+='   }\n'
       h+='}\n'
       h+='</pre>\n'

       h+='<p>Feel free to add description of your own CK repository to <a href="https://github.com/ctuning/ck-env/blob/master/cfg/list-of-repos/.cm/meta.json">this JSON file</a> - just open a PR on this <a href="https://github.com/ctuning/ck-env">GitHub repo</a>.\n'
       h+='You can obtain the main key for your entry (DATA UID) as well as data_uoa (DATA ALIAS) using this command: ck info repo:{my repo name}. You can then obtain and add "dict" using this command: ck load repo:{my repo name} --min .\n'

       h+='<p>See <a href="https://github.com/ctuning/ck/wiki">CK documentation</a>,\n'
       h+=' <a href="https://github.com/ctuning/ck/wiki#contributing">"how to contribute" guide</a>\n'
       h+=' and <a href="https://github.com/ctuning/ck/wiki#user-content-reusable-ck-components">already shared reusable components</a> for further details.\n'

       h+='<p>\n'
       h+='<table cellpadding="4" border="1" style="border-collapse: collapse; border: 1px solid black;">\n'

       h+=' <tr>\n'
       h+='  <td nowrap><b>#</b></td>\n'
       h+='  <td nowrap><b>Repository UOA</b></td>\n'
       h+='  <td nowrap><b>Workflow</b></td>\n'
       h+='  <td><b>Description</b></td>\n'
       h+=' </tr>\n'

    repos={}
    repo_url={}
    repo_private={}

    # Check which already manually added from cfg:list-of-repos
    rruoa=i.get('repo_uoa','')

    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['cfg'],
                 'data_uoa':cfg['cfg-list-of-repos']})
    if r['return']>0 and r['return']!=16: return r
    if r['return']==0:
       repos=r['dict']
       if rruoa=='': rruoa=r['repo_uid']

    # Going through already described repos and add missing ones
    private=''
    remote=''
    for l in ll:

        lr=l['data_uoa']
        lr_uid=l['data_uid']

        url=''

        if lr=='default':
           url='https://github.com/ctuning/ck/tree/master/ck/repo'
        else:
           rx=ck.load_repo_info_from_cache({'repo_uoa':lr_uid})
           if rx['return']>0: return rx
           url=rx.get('dict',{}).get('url','')
           private=rx.get('dict',{}).get('private','')
           remote=rx.get('dict',{}).get('remote','')

        if lr not in cfg.get('skip_repos',[]) and remote!='yes' and private!='yes' and url!='':
           if lr_uid not in repos:
              repos[lr_uid]={'data_uoa':lr}

    # Try to fill in missing information or find duplicates
    to_delete=[]
    for repo_uid in list(repos.keys()):
        x=repos[repo_uid]

        repo_uoa=x['data_uoa']

        d=x.get('dict',{})
      
        # Find real repo and get .ckr.json
        rx=ck.access({'action':'where',
                      'module_uoa':cfg['module_deps']['repo'],
                      'data_uoa':repo_uoa})
        if rx['return']==0: 
           pckr=os.path.join(rx['path'], ck.cfg['repo_file'])
           if os.path.isfile(pckr):
              rx=ck.load_json_file({'json_file':pckr})
              if rx['return']>0: return rx

              rxd=rx['dict']

              dx=rxd['dict']

              if 'path' in dx:
                 del(dx['path'])

              real_repo_uid=rxd['data_uid']

              # Check if mismatch of real uid and current one (old bug - should be fixed now)
              if real_repo_uid!=repo_uid:
                 ck.out('')
                 ck.out('WARNING: repo UID mismatch for '+repo_uoa+' ('+real_repo_uid+' != '+repo_uid+')')
                 ck.out('')

#                 r=ck.inp({'text':'  update correct one and remove old (Y/n)?'})
#                 if r['return']>0: return r
#                 xx=r['string'].strip().lower()
                 if True: #xx!='n':
                    if real_repo_uid not in repos:
                       repos[real_repo_uid]=copy.deepcopy(repos[repo_uid])
                    else:
                       if not 'dict' in repos[real_repo_uid]:
                          repos[real_repo_uid]['dict']={}
                       repos[real_repo_uid]['dict'].update(d)

                    to_delete.append(repo_uid)
              else:
                 # light update
                 for k in dx:
                     if k not in d:
                        d[k]=dx[k]

    # Delete duplicates (old bug)
    for tod in to_delete:
        if tod in repos: 
           ck.out('* Deleting '+tod)
           del(repos[tod])

    # Record list
    if rruoa=='': rruoa='ck-env'

    r=ck.access({'action':'update',
                 'module_uoa':cfg['module_deps']['cfg'],
                 'data_uoa':cfg['cfg-list-of-repos'],
                 'repo_uoa':rruoa,
                 'dict':repos,
                 'substitute':'yes',
                 'sort_keys':'yes',
                 'ignore_update':'yes'})
    if r['return']>0: return r
    
    # Show repos
    num=0
    for repo in sorted(repos, key=lambda k: repos[k]['data_uoa']):
        l=repos[repo]

        lr=l['data_uoa']
        lr_uid=repo

        d=l.get('dict',{})

        if d.get('skip_from_index','')=='yes':
           continue

        url=d.get('url','')
        external_url=d.get('external_url','')
        rd=d.get('repo_deps',{})

        ld=d.get('desc','')

        workflow_desc=d.get('workflow_desc','')

        to_get=''
        if url.find('github.com/ctuning/')>0:
           to_get='ck pull repo:'+lr
        elif url!='':
           to_get='ck pull repo --url='+url
        elif external_url!='':
           to_get='[ <a href=\"'+external_url+'\">external link</a> ]'

        num+=1

        ###############################################################
        if html:
           h+=' <tr>\n'

           x1=''
           x1readme=''
           x2=''
           z1=''
           z11=''
           url2=''

           if url!='' and url.startswith('git@'):
              url=url.replace(':','/').replace('git@','https://')

           if url=='' and lr=='default':
              url='https://github.com/ctuning/ck/tree/master/ck/repo'

           if url!='':
              x1='<a href="'+url+'">'
              x1readme='<a href="'+url+'#readme">'
              x2='</a>'

              url2=url

              if url2.endswith('.git'):
                 url2=url2[:-4]

              if '/tree/master/' not in url2:
                 url2+='/tree/master/'
              else:
                 url2+='/'

              z1='<a href="'+url2+'.ckr.json">'

           # TD
           h+='  <td nowrap valign="top"><a name="'+lr+'">'+str(num)+'</b></td>\n'
                                                     
           # TD
           x5=''
           if url!='':
              x5='<br><ul>( '+x1readme+'README'+x2+' ; '+z1+'JSON meta</a> )'

           h+='  <td nowrap valign="top">'+x1+lr+x2+''+x5+'</td>\n'

           # TD
           workflow_desc=workflow_desc.replace('$#repo_url#$',url2)

           if d.get('ck_artifact','')!='' or d.get('reproducible_article','')=='yes' or d.get('passed_artifact_evaluation','')=='yes':
              if workflow_desc!='': workflow_desc+='<p>'
              workflow_desc+='reproducible&nbsp;paper\n'
              if d.get('passed_artifact_evaluation','')=='yes':
                 workflow_desc+='-&nbsp;passed&nbsp;<a href="http://cTuning.org/ae">Artifact&nbsp;Evaluation</a>:\n'
                 workflow_desc+='<p><center><img src="https://www.acm.org/binaries/content/gallery/acm/publications/replication-badges/artifacts_evaluated_reusable_dl.jpg" width="64"></center>\n'

           h+='  <td valign="top"><center>\n'
           h+='    '+workflow_desc+'\n'
           h+='  </center></td>\n'

           # TD
           ld=ld.replace('$#repo_url#$',url2)
           h+='  <td valign="top">'+ld+'\n'

           if to_get!='':
              h+='<p>\n'
              h+='How to get:\n'
              h+='<pre>\n'
              h+=to_get+'\n'
              h+='</pre>\n'

           if len(rd)>0:
              h+='<p>Dependencies on other repositories:\n'
              h+='<ul>\n'
              for qq in sorted(rd, key=lambda k: k['repo_uoa']):
                  repo_uoa=qq['repo_uoa']
                  repo_url=qq.get('repo_url','')

                  if repo_url=='':
                     repo_url='https://github.com/ctuning/'+repo_uoa

                  if repo_url!='':
                     repo_uoa='<a href="#'+repo_uoa+'">'+repo_uoa+'</a>'

                  h+='<li>'+repo_uoa+'\n'
              h+='</ul>\n'

           h+='</td>\n'

           h+=' </tr>\n'

    ck.out('')
    ck.out('  Total repos: '+str(num))
    ck.out('')

    if html:
       h+='</table>\n'
       h+=h2

       if of!='':
          r=ck.save_text_file({'text_file':of, 'string':h})
          if r['return']>0: return r

    return {'return':0}

##############################################################################
# list modules

def list_modules(i):
    """
    Input:  {
              (new) - if 'yes', add htmls
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy

    o=i.get('out','')

    of=i.get('out_file','')
    if of!='':
       xof=os.path.splitext(of)

    html=False
    if o=='html' or i.get('web','')=='yes':
       html=True

    h=''
    h2=''
    if i.get('new','')=='yes':
       ii=copy.deepcopy(i)
       ii['ck_title']='Shared CK modules'
       r=preload_html_for_lists(ii)
       if r['return']>0: return r

       h=r['html_start']+'\n'
       h2=r['html_stop']+'\n'

    unique_repo=False
    if i.get('repo_uoa','')!='': unique_repo=True

    ii=copy.deepcopy(i)

    ii['out']=''
    ii['action']='list'
    ii['module_uoa']=cfg['module_deps']['module']
    ii['add_meta']='yes'
    ii['time_out']=-1

    rx=ck.access(ii)
    if rx['return']>0: return rx

    ll=sorted(rx['lst'], key=lambda k: k['data_uoa'])

    if html:
       h+='<h2>Please check our new <a href="http://ReuseResearch.com/c.php?c=program">beta browser</a> for CK components!</h2>\n'

       h+='<br>\n'

       h+='You can install and reuse CK modules as follows:\n'
       h+='<pre>\n'
       h+=' ck pull repo:{Repo UOA - see below}\n'
       h+=' ck help {module UOA - see below}\n'
       h+='</pre>\n'

       h+='You can check a JSON API of a given action of a given module as follows:\n'
       h+='<pre>\n'
       h+=' ck {module action - see below} {module UOA} --help\n'
       h+='</pre>\n'

       h+='You can add your own dummy CK module as follows:\n'
       h+='<pre>\n'
       h+=' ck add module:{my module alias}\n'
       h+='</pre>\n'

       h+='You can add a new action to the CK module as follows:\n'
       h+='<pre>\n'
       h+=' ck add_action module:{my module alias}\n'
       h+='</pre>\n'

       h+='See <a href="https://github.com/ctuning/ck/wiki">CK documentation</a>,\n'
       h+=' <a href="https://github.com/ctuning/ck/wiki#contributing">"how to contribute" guide</a>,\n'
       h+=' and the latest <a href="http://cKnowledge.org/rpi-crowd-tuning">CK paper</a> for further details.\n'

       h+='<p>\n'
       h+='<table cellpadding="4" border="1" style="border-collapse: collapse; border: 1px solid black;">\n'

       h+=' <tr>\n'
       h+='  <td nowrap><b>#</b></td>\n'
       h+='  <td nowrap><b>Module&nbsp;UOA with JSON API<br>(Python module/wrapper/plugin)</b></td>\n'
       h+='  <td nowrap><b>Repo UOA</b></td>\n'
       h+='  <td nowrap><b>Workflow (pipeline)?</b></td>\n'
       h+='  <td><b>Description and actions</b></td>\n'
       h+=' </tr>\n'

    repo_url={}
    repo_private={}

    private=''
    num=0

    for l in ll:
        ln=l['data_uoa']
        lr=l['repo_uoa']

        lr_uid=l['repo_uid']
        url=''
        if lr=='default':
           url='https://github.com/ctuning/ck/tree/master/ck/repo'
        elif lr_uid in repo_url:
           url=repo_url[lr_uid]
        else:
           rx=ck.load_repo_info_from_cache({'repo_uoa':lr_uid})
           if rx['return']>0: return rx
           url=rx.get('dict',{}).get('url','')
           repo_private[lr_uid]=rx.get('dict',{}).get('private','')
           repo_url[lr_uid]=url

        private=repo_private.get(lr_uid,'')

#        if lr not in cfg.get('skip_repos',[]) and private!='yes' and url!='':
        if lr not in cfg.get('skip_repos',[]) and private!='yes' and url!='':
           num+=1

           ck.out('  '+str(num)+') '+ln)

           lm=l['meta']
           ld=lm.get('desc','')

           xworkflow=lm.get('workflow','')
           workflow=lm.get('workflow_type','')
           if xworkflow=='yes' and workflow=='':
              workflow='yes'

           actions=lm.get('actions',{})

           if lr=='default':
              to_get=''
           elif url.find('github.com/ctuning/')>0:
              to_get='ck pull repo:'+lr
           else:
              to_get='ck pull repo --url='+url

           ###############################################################
           if html:
              h+=' <tr>\n'

              x1=''
              x2=''
              z1=''
              z1full=''
              z11=''
              if url!='':
                 x1='<a href="'+url+'">'
                 x2='</a>'

                 url2=url

                 if url2.endswith('.git'):
                    url2=url2[:-4]

                 if '/tree/master/' not in url2:
                    url2+='/tree/master/module/'
                 else:
                    url2+='/module/'

                 z1full=url2+ln+'/module.py'
                 z1='<a href="'+z1full+'">'
                 z11='<a href="'+url2+ln+'/.cm/meta.json">'

              h+='  <td nowrap valign="top"><a name="'+ln+'">'+str(num)+'</b></td>\n'

              h+='  <td nowrap valign="top">'+z1+ln+x2+'</b> <i>('+z11+'CK meta'+x2+')</i></td>\n'

              h+='  <td nowrap valign="top"><b>'+x1+lr+x2+'</b></td>\n'

              h+='  <td nowrap valign="top">'+workflow+'</td>\n'

              h+='  <td valign="top">'+ld+'\n'

              if len(actions)>0:
                 h+='<ul>\n'
                 for q in sorted(actions):

                     qq=actions[q]
                     qd=qq.get('desc','')

                     h+='<li>"ck <i>'+q+'</i> '+ln+'"'
                     if qd!='':
                        h+=' - '+qd

                     if z1full!='':
                        # Get API!
                        l=-1
                        rx=ck.get_api({'module_uoa':ln, 'func':q})
                        if rx['return']==0:
                           l=rx['line']

                        if l!=-1:
                           h+=' (&nbsp;<a href="'+z1full+'#L'+str(l)+'">API</a>&nbsp;)'
                 h+='</ul>\n'

              h+='</td>\n'

              h+=' </tr>\n'

           ###############################################################
           elif o=='mediawiki':
              x=lr
              if url!='':
                 x='['+url+' '+lr+']'
              ck.out('')
              ck.out('=== '+ln+' ('+lr+') ===')
              ck.out('')
              ck.out('Desc: '+ld)
              ck.out('<br>CK Repo URL: '+x)
              if to_get!='':
                 ck.out('<br>How to get: <i>'+to_get+'</i>')
              ck.out('')
              if len(actions)>0:

                 ck.out('Actions (functions):')
                 ck.out('')

                 for q in sorted(actions):
                     qq=actions[q]
                     qd=qq.get('desc','')
                     ck.out('* \'\''+q+'\'\' - '+qd)

           ###############################################################
           elif o=='con' or o=='txt':
              if unique_repo:
                 ck.out('')
                 s=ln+' - '+ld

              else:
                 ss=''
                 if len(ln)<35: ss=' '*(35-len(ln))

                 ss1=''
                 if len(lr)<30: ss1=' '*(30-len(lr))

                 s=ln+ss+'  ('+lr+')'
                 if ld!='': s+=ss1+'  '+ld

              ck.out(s)

              if len(actions)>0:
                 ck.out('')
                 for q in sorted(actions):
                     qq=actions[q]
                     qd=qq.get('desc','')
                     ck.out('  * '+q+' - '+qd)


    ck.out('')
    ck.out('  Total modules: '+str(num))
    ck.out('')

    if html:
       h+='</table>\n'
       h+=h2

       if of!='':
          r=ck.save_text_file({'text_file':of, 'string':h})
          if r['return']>0: return r

    return {'return':0}

##############################################################################
# preload HTMLs for lists of components

def preload_html_for_lists(i):
    """
    Input:  {
              (html_file_start) - ck_start_html by default
              (html_file_stop)  - ck_stop_html by default
              (ck_title)        - update title in the start file
              (out_file)        - get page name
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html_start
              html_stop
            }

    """

    import os

    out_file=i.get('out_file','')

    page_name=os.path.basename(out_file)
    if page_name.endswith('.html'):
       page_name=page_name[:-5]

    fstart=i.get('html_file_start','')
    if fstart=='': fstart='ck_start.html'

    fstop=i.get('html_file_stop','')
    if fstop=='': fstop='ck_stop.html'

    ck_title=i.get('ck_title','')

    # Load first file
    r=ck.load_text_file({'text_file':fstart})
    if r['return']>0: return r

    html_start=r['string'].replace('$#ck_title#$',ck_title)
    html_start=html_start.replace('$#ck_page#$',page_name)

    # Load second file
    r=ck.load_text_file({'text_file':fstop})
    if r['return']>0: return r

    html_stop=r['string'].replace('$#ck_title#$',ck_title)

    return {'return':0, 'html_start':html_start, 'html_stop':html_stop}

##############################################################################
# replace multiple strings in a given file

def replace_strings_in_file(i):
    """
    Input:  {
              file
              (file_out)            - if !='', use this file for output, otherwise overwrite original one!
              replacement_json_file - replacement file with multiple strings to substitute
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              (updated)    - if 'yes', files was updated
            }

    """

    import copy

    o=i.get('out','')

    fin=i['file']
    rjf=i['replacement_json_file']

    fout=i.get('file_out','')
    if fout=='': fout=fin

    rx=ck.load_text_file({'text_file':fin})
    if rx['return']>0: return rx
    s=rx['string']

    rx=ck.load_json_file({'json_file':rjf})
    if rx['return']>0: return rx
    rep=rx['dict']

    sx=s
    for k in rep:
        v=rep[k]
        sx=sx.replace(k,v)

    r={'return':0, 'updated':'no'}

    if s!=sx or fin!=fout:
       r=ck.save_text_file({'text_file':fout, 'string':sx})
       r['updated']='yes'

    return r


def transfer(i):
    """
    Input:  {
                xcids[]             - (remote) entries to be copied to a local repository, made of repo_uoa:module_uoa:data_uoa

                (source_repo_uoa)   - in case the source is remote, the specific repository on the source (optional - only needed for disambiguation)
                (target_server_uoa) - the optional target remote server (mapped as a local repository)
                (target_repo_uoa)   - the repository to store the entries on target server ('local' by default)
                (update_meta_dict)  - the dictionary with which to update the original meta.json
                (update_mmeta_dict) - the dictionary with which to update the meta dictionary inside meta.json
                (tags)              - filter the source list by tags
            }

    Output: {
                return      - return code =  0, if successful
                                          >  0, if error
                (error)     - error text if return > 0
            }
    """

    import os

    o                   = i.get('out','')
    source_addrs        = i.get('xcids', [])       # can unshift the "default entry" into this list when/if moving this method to the kernel

    source_repo_uoa     = i.get('source_repo_uoa')
    target_server_uoa   = i.get('target_server_uoa')
    target_repo_uoa     = i.get('target_repo_uoa', 'local')
    update_meta_dict    = i.get('update_meta_dict', {})
    update_mmeta_dict    = i.get('update_mmeta_dict', {})

    tags                = i.get('tags')

    if len(source_addrs)==0:
        return {'return':1, 'error': 'Need a non-empty list of source CID addresses'}

    expanded_source_addrs = {}

    for addr_pattern in source_addrs:
        search_adict = {'action':       'search',
        }
        search_adict.update( addr_pattern )
        if tags:
            search_adict['tags']            = tags
        if source_repo_uoa:
            search_adict['remote_repo_uoa'] = source_repo_uoa

        r=ck.access( search_adict )
        if r['return']>0: return r

        for found_addr in r['lst']:     # NB: remote found_addr comes with screwed up repo_uoa, we have to undo that
            source_addr = {
                'data_uoa':     found_addr['data_uoa'],
                'module_uoa':   found_addr['module_uoa'],
            }
            if addr_pattern.get('repo_uoa') and found_addr.get('repo_uoa')!=addr_pattern.get('repo_uoa'):
                source_addr.update( {
                    'remote_repo_uoa':    found_addr.get('repo_uoa'),
                    'repo_uoa':         addr_pattern.get('repo_uoa'),
                })
            else:
                source_addr['repo_uoa'] = found_addr.get('repo_uoa')

            cid = ':'.join([ source_addr['repo_uoa'], source_addr['module_uoa'], source_addr['data_uoa'] ])
            if cid in expanded_source_addrs:
                return {'return':2, 'error': "Entry {} was found on the source multiple times - please use --source_repo_uoa to disambiguate!".format(cid)}
            else:
                expanded_source_addrs[cid] = source_addr

    for source_addr in expanded_source_addrs.values():
        from_local = source_addr.get('remote_repo_uoa') == None
        if from_local and (not target_server_uoa):
            return {'return':3, 'error': 'Cannot copy the entries locally (since IDs are to be preserved)'}

        target_addr = {
            'module_uoa':       source_addr['module_uoa'],
            'data_uoa':         source_addr['data_uoa'],
        }
        if target_server_uoa:
            target_addr.update({
                'remote_repo_uoa':  target_repo_uoa,
                'repo_uoa':         target_server_uoa,
            })
        else:
            target_addr['repo_uoa'] = target_repo_uoa


        load_adict = {  'action':           'load',
        }
        load_adict.update( source_addr )
        r=ck.access( load_adict )
        if r['return']>0: return r

        meta_dict           = r['dict']
        data_uid            = r['data_uid']

        meta_dict.update( update_meta_dict )
        meta_dict.get('meta', {}).update( update_mmeta_dict )

        add_adict = {   'action':           'add',
                        'common_func':      'yes',
                        'dict':             meta_dict,              # copying meta data
                        'data_uid':         data_uid,               # copying the original data_uid
        }
        add_adict.update( target_addr )
        r=ck.access( add_adict )
        if r['return']>0: return r

        pull_adict = {  'action':           'pull',
                        'archive':          'yes',
        }
        pull_adict.update( source_addr )
        r=ck.access( pull_adict )
        if r['return']>0: return r

        zip_name = ck.cfg['default_archive_name']

        push_adict = {  'action':           'push',
                        'archive':          'yes',
                        'filename':         zip_name,
        }
        push_adict.update( target_addr )
        r=ck.access( push_adict )
        if r['return']>0: return r

        if os.path.isfile(zip_name):
            os.remove(zip_name)     # to avoid clashing with the next one

        if o=='con':
            display_source_repo = source_addr['repo_uoa'] if from_local else '{}/{}'.format(source_addr['repo_uoa'], source_addr['remote_repo_uoa'])
            display_target_repo = '{}/{}'.format(target_server_uoa, target_repo_uoa) if target_server_uoa else target_repo_uoa
            display_mod_data    = '{}:{}'.format(source_addr['module_uoa'], source_addr['data_uoa'])
            ck.out('{}:{} -> {}:{}'.format(display_source_repo, display_mod_data, display_target_repo, display_mod_data))

    return {'return':0}


def clone_server_repo(i):   # FIXME: it's probably better to zip the whole thing and transfer in one go
    """
    Input:  {
                source_repo_uoa     - which remote repo to clone

                (target_repo_uoa)   - the optional local name for the new repo (defaults to source_repo_uoa)
            }

    Output: {
                return      - return code =  0, if successful
                                          >  0, if error
                (error)     - error text if return > 0
            }
    """

    o                   = i.get('out','')
    source_repo_uoa     = i.get('source_repo_uoa')

    if not source_repo_uoa:
        return {'return':1, 'error': 'source_repo_uoa is the obligatory parameter'}

    target_repo_uoa     = i.get('target_repo_uoa', source_repo_uoa)


    add_repo_adict = {  'action':       'add',
                        'module_uoa':   'repo',
                        'data_uoa':     target_repo_uoa,
                        'quiet':        'yes',
                        'out':          o,
    }

    r=ck.access( add_repo_adict )
    if r['return']>0: return r

    transfer_adict = {  'action':           'transfer',
                        'module_uoa':       'misc',
                        'cids':             [ 'remote-ck:*:*' ],    # sic: you call with unparsed 'cids' and the method will see parsed 'xcids'
                        'source_repo_uoa':  source_repo_uoa,
                        'target_repo_uoa':  target_repo_uoa,
                        'out':              o,
    }
    r=ck.access( transfer_adict )
    if r['return']>0: return r

    return {'return':0}


def substitute_from_dict(i):
    """
    Input:  {
                input_string        - original string with placeholders for substitution
                mapping             - dictionary to subsitute from
                (input_open)        - opening marker for the keyword in the input_string
                (input_close)       - closing marker for the keyword in the input_string
                (tolerant)          - if "yes", do not fail if a keyword is missing from mapping
            }

    Output: {
                return      - return code =  0, if successful
                                          >  0, if error
                (error)     - error text if return > 0
            }
    Tests:
        ck substitute_from_dict misc --input_string='alpha $<<FOO>>$ gamma' "@@@{'mapping': {'FOO': 'beta'}}"

        ck substitute_from_dict misc --input_string='alpha$#dir_sep#$gamma $#foo#$X' \
            "@@@{'mapping': {'dir_sep': '/'}}" --input_open='$#' --input_close='#$' --tolerant
    """

    import re

    input_string    = i['input_string']
    mapping         = i['mapping']

    input_open      = i.get('input_open', '$<<')
    input_close     = i.get('input_close', '>>$')
    tolerant        = i.get('tolerant') == 'yes'

    pattern         = re.compile( '({}(\w+){})'.format(re.escape(input_open), re.escape(input_close)) )
    output_string   = input_string

    for match in re.finditer(pattern, input_string):
        expression, keyword = match.group(1), match.group(2)
        if keyword in mapping:
            output_string = output_string.replace(expression, mapping[keyword])
        elif tolerant:
            output_string = output_string.replace(expression, "")
        else:
            return {'return':1, 'error': "Could not map {} from the given dictionary".format(expression) }

    if i.get('out') == 'con':
        ck.out(output_string)

    return {'return': 0, 'output_string': output_string}


def capture_command_output(i):
    """
    Input:  {
                cmd                 - shell command with parameters to run
            }

    Output: {
                output_lines        - an array of lines of the command's output

                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Tests:
        ck capture_command_output misc --cmd='ls -1'
    """

    import subprocess

    cmd = i['cmd']

    if type(cmd)!=list:
        cmd = cmd.split()   # split on general whitespace

    try:
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE)

        stdout_lines = out.communicate()[0].decode("utf8").split("\n")

        if stdout_lines[-1] == '':
            stdout_lines.pop()  # remove the last empty element

        return {'return': 0, 'output_lines': stdout_lines}

    except:
        return {'return': 1, 'error': "Could not run the command '{}'".format(cmd) }

##############################################################################
# list CK kernel functions (md format)

def list_kernel_functions_md(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy

    o=i.get('out','')

    of=i.get('out_file','')

    h=''
    h2=''
    hcfg=''

    p=ck.work['env_root'] # Internal CK path

    pk=os.path.join(p, 'ck', 'kernel.py')
    if not os.path.isfile(pk):
       return {'return':1, 'error':'Can\'t find kernel in '+pk}

    r=ck.load_text_file({'text_file':pk, 'split_to_list':'yes'})
    if r['return']>0: return r

    l=r['lst']

    funcs={}
    desc=[]
    ld=0
    target=''

    cfg=[]
    cfg_start=False

    ll=len(l)
    for k in range(0, ll):
        x=l[k]

        if x.startswith('cfg={'):
           cfg_start=True

        if cfg_start:
           cfg.append(x)
           if x=='    }':
              cfg_start=False

        if x.startswith('##################'):
           desc=[]
           ld=k

        if x.startswith('# '):
           x1=x[2:].strip()
           if x1.startswith('TARGET: '):
              target=x1[8:]
           else:
              desc.append(x1)

        if x.startswith('def '):
           j1=x.find('(')
           j2=x.find(')', j1+1)
           j3=x.find(':')

           fn=x[4:j1]
           i=x[j1+1:j2]
           rem=x[j3+1:]

           api=[]

           k+=1

           found=False
           first=False
           while not found or k<ll:
              x=l[k]
              if x.strip().startswith('"""'):
                 if first:
                    found=True
                    break
                 else:
                    first=True
              elif first:
                 api.append(x)
              k+=1
           
           if found:
              funcs[fn]={'api':api,
                         'input':i,
                         'rem':rem,
                         'desc':desc,
                         'line':ld,
                         'target':target}

           api=[]
           desc=[]
           target=''

    # Process functions
    h+='# CK kernel functions for end-users\n'
    h+='\n'
    h+='We encourage you to reuse these portable productivity functions (Python 2.6+ and 3+) from the CK modules or in your own Python scripts:\n'
    h+='\n'
    h+='```python\n'
    h+='    import ck.kernel as ck\n'
    h+='\n'
    h+='    ck.out("Hello world")\n'
    h+='\n'
    h+='    r=ck.access({"action":"ls", "module_uoa":"env", "out":"con"})\n'
    h+='    if r["return"]>0: ck.err(r)\n'
    h+='    print (r["lst"])\n'
    h+='\n'
    h+='    r=ck.load_json_file({"json_file":"my_file.json", "dict":{"test":"yes"}})\n'
    h+='    if r["return"]>0: return r\n'
    h+='\n'
    h+='    r=ck.save_text_file({"text_file":"my_file.txt", "string":"test=yes\\n"})\n'
    h+='    if r["return"]>0: return r\n'
    h+='\n'
    h+='```\n'

    hdev=h

    num1=0
    num2=0
    for f in sorted(funcs):
        x=funcs[f]

        api=x['api']
        i=x['input']
        rem=x['rem']
        line=x['line']
        desc=x['desc']
        target=x['target']

        xapi='<i>'
        for y in desc:
            j=y.find('\\n=')
            if j>=0: 
               y=y[:j]
            xapi+=y
        xapi+='</i>\n'

        xapi+='\n'
        xapi+='```python\n'
        for y in api:
            xapi+=y+'\n'
        xapi+='```\n'

        url='https://github.com/ctuning/ck/blob/master/ck/kernel.py'

        x=''
        if target!='':
           x+='<p>&nbsp;&nbsp;&nbsp;<i>for '+target+'</i>'

        if 'end users' in target or 'end-users' in target:
           num1+=1
           num=num1
        else:
           num2+=1
           num=num2

        zh='\n## ck.'+f+'('+i+')\n\n'

        zh+=xapi+'\n'
#  <td nowrap valign="top"><a name="'+f+'">'+str(num)+'</td>\n'
#        zh+='  <td nowrap valign="top"><a href="'+url+'#L'+str(line+1)+'"><b>ck.'+f+'('+i+')</b></a>'+x+'</b></td>\n'
#        zh+='  <td nowrap valign="top">'+xapi+'</td>\n'
#        zh+=' </tr>\n'

        if 'end users' in target or 'end-users' in target:
           h+=zh
        else:
           hdev+=zh

    # Prepare config
    hcfg+='You can access the following CK internal variables:\n'
    hcfg+='\n'
    hcfg+='```python\n'
    hcfg+='    import ck.kernel as ck\n'
    hcfg+='\n'
    hcfg+='    print (ck.cfg)\n'
    hcfg+='```\n\n'

    hcfg+='See <a href="https://github.com/ctuning/ck/wiki">CK documentation for further details</a>.\n'

    hcfg+='\n'
    hcfg+='```python\n'
    for x in cfg:
        hcfg+=x+'\n'
    hcfg+='```\n'
    hcfg+=h2

    h+=h2
    hdev+=h2

    if of!='':
       r=ck.save_text_file({'text_file':of+'.md', 'string':h})
       if r['return']>0: return r

       r=ck.save_text_file({'text_file':of+'-dev.md', 'string':hdev})
       if r['return']>0: return r

       r=ck.save_text_file({'text_file':of+'-dev-cfg.md', 'string':hcfg})
       if r['return']>0: return r

    return {'return':0}
