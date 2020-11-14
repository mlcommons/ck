#
# Collective Knowledge (checking and installing software)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Leo Gordon, leo@dividiti.com
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)


def init(i):
    """
    Not to be called directly. Sets the path to the vqe_plugin.
    """

    return {'return':0}


def iterate(i):
    """
    Input:  {
                (any_params)        - any command line parameters, some of which (being iterable) given as lists/ranges

                    Please note the expected command line syntax for iterable values:

                --alpha=val         - a single value of any type

                --beta,=10,20,30    - a list of values (comma-separated)
                --beta:=10:20:30    - a list of values (colon-separated)

                --delta:12:18       - a range of integer values (step=1 by default), inclusive of both lower and upper bounds.
                --delta:12:18:3     - a range of integer values (step=3), inclusive of both lower and upper bounds.
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck iterate cmdgen --alpha,=11,22,33 --beta:-9:-7 --delta=single --gamma:=one:two:three
            ck iterate cmdgen --alpha,=11,22,33 --beta:-9:-7 --delta=single --gamma:=one:two:three --out=json
    """
    import re

    interactive     = i.get('out')=='con'

    input_params    = i.copy()
    for unwanted_key in ('action', 'repo_uoa', 'module_uoa', 'data_uoa', 'cid', 'cids', 'xcids', 'out'):
        input_params.pop(unwanted_key, None)

    index_name  = []
    index_range = []

    for param_name in input_params.keys():
        param_value = input_params[param_name]
        matchObj = re.match('(\w+)([,:])?((-?\d+):(-?\d+)(?:\:(\d+))?)?$', param_name)
        if matchObj:
            pure_name   = matchObj.group(1)
            index_name.append( pure_name )
            if matchObj.group(2)==None:
                index_range.append( [param_value] )
            elif matchObj.group(3):
                range_from  = int(matchObj.group(4))
                range_to    = int(matchObj.group(5))
                range_step  = int(matchObj.group(6)) if matchObj.group(6) else 1
                index_range.append( [ str(n) for n in range(range_from, range_to+1, range_step) ] )
            else:
                delimiter   = matchObj.group(2)
                index_range.append( param_value.split(delimiter) )
        else:
            return {'return':1, 'error':"Could not recognize parameter '{}'".format(param_name)}

    if interactive:
        print(dict(zip(index_name, index_range)))
        print('-'*80)

    dimensions  = len(index_name)
    multi_idx   = [0] * dimensions
    current_dim = dimensions-1
    param_dicts = []
    while True:
        multi_value = {index_name[i]: index_range[i][multi_idx[i]] for i in range(dimensions) }
        param_dicts.append( multi_value )

        if interactive:
            print(multi_value)

        if current_dim>=0:
            multi_idx[current_dim] += 1
        # carry avalanche:
        while current_dim>=0 and multi_idx[current_dim]>=len(index_range[current_dim]):
            multi_idx[current_dim] = 0
            current_dim -= 1
            if current_dim>=0:
                multi_idx[current_dim] += 1

        if current_dim>=0:
            current_dim = dimensions-1
        else:
            break

    return {'return':0, 'param_dicts': param_dicts}


def gen(i):
    """
    Input:  {
                data_uoa            - specific entry that contains recipe for building the command
                (any_map_params)    - any command line parameters (supported by build_map)

                    Please note the expected command line syntax for iterable values:

                --alpha=val         - a single value of any type

                --beta,=10,20,30    - a list of values (comma-separated)
                --beta:=10:20:30    - a list of values (colon-separated)

                --delta:12:18       - a range of integer values (step=1 by default), inclusive of both lower and upper bounds.
                --delta:12:18:3     - a range of integer values (step=3), inclusive of both lower and upper bounds.
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck gen cmdgen:ls
            ck gen cmdgen:ls --mode=long --home
            ck gen cmdgen:ls --mode,=long,short,single
            ck gen cmdgen:ls --mode=short --files:=$PATH
    """

    import re
    from copy import deepcopy
    from pprint import pprint

    interactive     = i.get('out')=='con'

    load_adict = {  'action':           'load',
                    'repo_uoa':         i.get('repo_uoa', ''),
                    'module_uoa':       i['module_uoa'],
                    'data_uoa':         i['data_uoa'],
    }
    r=ck.access( load_adict )
    if r['return']>0: return r

    entry_dict  = r['dict']
    if interactive:
        print("Entry contents:")
        pprint(entry_dict)
        print("")

    build_map   = entry_dict.get('build_map', {})
    defaults    = entry_dict.get('defaults', {})

    i['action'] = 'iterate'
    i['out']    = ''
    r=ck.access( i )
    if r['return']>0: return r
    param_dicts = r['param_dicts']

    cmds    = []
    for input_params in param_dicts:

        # Accumulating values:
        #
        accu        = deepcopy( entry_dict.get('accu_init', {}) )
        for param_name in input_params:
            param_value = input_params[param_name]

            if param_name in build_map:
                specific_accu_map = build_map[param_name]

                # Start with the specific value:
                accu_map = specific_accu_map.get(param_value)

                # if not found, try matching a pattern:
                if accu_map == None:
                    for pattern_candidate in specific_accu_map:
                        if re.search('^'+pattern_candidate+'$', param_value):
                            accu_map = specific_accu_map[pattern_candidate]

                # if still not found, try the universal default:
                if accu_map == None:
                    accu_map = specific_accu_map.get('###')

                # if still not found, fail gracefully:
                if accu_map==None:
                    return {'return':1, 'error':"build_map[{}] is missing both '{}' and '###' values".format(param_name, param_value)}

                for accu_name in accu_map:
                    if accu_name not in accu:
                        accu[accu_name] = []    # manual vivification

                    accu_value_list = accu_map[accu_name]
                    if type(accu_value_list)!=list:
                        accu_value_list = [ accu_value_list ]

                    for accu_value in accu_value_list:
                        accu[accu_name].append( accu_value.replace('###', param_value) )

        if False and interactive:
            print('-'*80)
            print("Accu contents:")
            pprint(accu)
            print("")

        # Substitute the accumulated values into command template:
        #
        anchor_regexpr  = '((?:<<<|{{{)(\??)(\w+)(.?)(?:>>>|}}}))'
        subst_output    = entry_dict['cmd_template']
        can_substitute  = bool( re.search(anchor_regexpr, subst_output) )
        iteration       = 0

        while can_substitute:
            subst_input = subst_output
            for match in re.finditer(anchor_regexpr, subst_input):
                expression, optional, anchor_name, accu_sep = match.group(1), match.group(2), match.group(3), match.group(4)
                if anchor_name in accu:
                    if anchor_name in input_params:
                        return {'return':1, 'error':"Both input_params and accu contain '{}' anchor, ambiguous substitution".format(anchor_name)}
                    else:
                        accu_value_list = accu[anchor_name]
                        if type(accu_value_list)!=list:
                            accu_value_list = [ accu_value_list ]
                        subst_output = subst_output.replace(expression, accu_sep.join(accu_value_list) )

                        # print("Substituting {} -> {} from accu".format(expression, accu_sep.join(accu[anchor_name])))
                elif anchor_name in input_params:
                    subst_output = subst_output.replace(expression, input_params[anchor_name] )

                    # print("Substituting {} -> {} from input_params".format(expression, input_params[anchor_name]))
                elif anchor_name in defaults:
                    default_value_list = defaults[anchor_name]
                    if type(default_value_list)!=list:
                        default_value_list = [ default_value_list ]
                    subst_output = subst_output.replace(expression, accu_sep.join(default_value_list) )

                    # print("Substituting {} -> {} from defaults".format(expression, defaults[anchor_name]))
                elif optional=='?':
                    # print("Substituting optional {} -> ''".format(expression))
                    subst_output = subst_output.replace(expression, '')
                else:
                    return {'return':1, 'error':"Neither input_params nor accu contain substitution for non-optional '{}' anchor".format(anchor_name)}

                # print("input={}\noutput={}\n".format(subst_input, subst_output))

            can_substitute  = bool( re.search(anchor_regexpr, subst_output) )
            if interactive:
                iteration += 1
                # print("Substitution iteration #{}".format(iteration))


        if subst_output not in cmds:
            cmds.append( subst_output )
            if interactive:
                print('# ' + '-'*40 +' cmd #{}: '.format(len(cmds)) + '-'*40 )
                print("\n{}\n".format(subst_output.replace(' --', ' \\\n    --')))

    return { 'return': 0, 'cmds': cmds }


def run(i):
    """
    Input:  {
                data_uoa            - specific entry that contains recipe for building the command
                (any_map_params)    - any command line parameters (supported by build_map)
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck run cmdgen:ls
            ck run cmdgen:ls --mode=long --home
            ck run cmdgen:ls --mode,=long,short,single
            ck run cmdgen:ls --mode=short --files:=$PATH
    """

    import os

    interactive = i.get('out')=='con'

    i['action'] = 'gen'
    i['out']    = ''
    r=ck.access( i )
    if r['return']>0: return r
    cmds = r['cmds']

    for cmd_idx in range(len(cmds)):
        cmd = cmds[cmd_idx]
        if interactive:
            print('# ' + '='*40 +' cmd #{}: '.format(cmd_idx+1) + '='*40 )
            print("Running command:\n\t"+cmd)
            print('')
        os.system(cmd)

    if interactive:
        print('='*90)

    return { 'return': 0 }


def show(i):
    """
    Input:  {
                (data_uoa)          - name of the SUT entry
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck show sut:velociti
    """

    from pprint import pprint

    interactive     = i.get('out')=='con'
    data_uoa = i.get('data_uoa')
    if data_uoa:
        load_adict = {  'action':           'load',
                        'module_uoa':       i['module_uoa'],
                        'data_uoa':         data_uoa,
        }
        r=ck.access( load_adict )
        if r['return']>0: return r

        entry_dict = r['dict']

        if interactive:
            pprint(entry_dict)

    return { 'return': 0 }


def map_keys(i):
    """
    Input:  {
                data_uoa            - specific entry that contains recipe for building the command
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck map_keys cmdgen:ls
            ck map_keys cmdgen:benchmark_tflite_loadgen
    """

    interactive     = i.get('out')=='con'

    load_adict = {  'action':           'load',
                    'repo_uoa':         i.get('repo_uoa', ''),
                    'module_uoa':       i['module_uoa'],
                    'data_uoa':         i['data_uoa'],
    }
    r=ck.access( load_adict )
    if r['return']>0: return r

    entry_dict  = r['dict']
    build_map   = entry_dict.get('build_map', {})
    map_keys    = list(build_map.keys())

    if interactive:
        print("\n".join(map_keys))

    return { 'return': 0, 'map_keys': map_keys }


def map_values(i):
    """
    Input:  {
                data_uoa            - specific entry that contains recipe for building the command
                option              - the map name for which the values are sought
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck map_values cmdgen:ls --option=mode
    """

    interactive     = i.get('out')=='con'

    load_adict = {  'action':           'load',
                    'repo_uoa':         i.get('repo_uoa', ''),
                    'module_uoa':       i['module_uoa'],
                    'data_uoa':         i['data_uoa'],
    }
    r=ck.access( load_adict )
    if r['return']>0: return r

    entry_dict  = r['dict']
    build_map   = entry_dict.get('build_map', {})
    option      = i['option']
    map_values  = list(build_map[option].keys())

    if interactive:
        print("\n".join(map_values))

    return { 'return': 0, 'map_values': map_values }

