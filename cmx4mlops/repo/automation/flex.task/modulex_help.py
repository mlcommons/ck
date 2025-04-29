# Author and developer: Grigori Fursin

import os
from cmind import utils

def print_help(i):

    meta = i['meta']
    path = i['path']

    if len(meta) == 0 and path == '':
        return {'return':0}

    print ('')
    print ('Help for the Flex Task ({},{}):'.format(meta.get('alias',''), meta.get('uid','')))

    alias = meta.get('alias', '')
    uid = meta.get('uid', '')
    tags = ','.join(meta.get('tags', []))

    print ('')
    print (f'  Path:  {path}')
    print (f'  Alias: {alias}')
    print (f'  UID:   {uid}')
    print (f'  Tags:  {tags}')

    input_description = meta.get('input_description', {})
    if len(input_description)>0:
        # Check if has important ones (sort)
        all_keys = sorted(list(input_description.keys()))

        print ('')
        print ('  Available CLI flags (the same as Python API dict keys):')
        print ('')
        for k in all_keys:
            v = input_description[k]
            n = v.get('desc','')

            x = f'    --{k}'

            d = None
            if 'default' in v:
                d = v.get('default','')

            if d != None:
                if type(d) == bool: d = str(d).lower()
                x += f'={d}'

            c = v.get('choices',[])
            if len(c)>0:
                x += '   {'+','.join(c)+'}'

            if n != '': x += '   {}'.format(n)

            print (x)

    output_description = meta.get('output_description', {})
    if len(output_description)>0:
        # Check if has important ones (sort)
        all_keys = sorted(list(output_description.keys()))

        print ('')
        print ('  Output Python API dict keys:')
        print ('')
        for k in all_keys:
            v = output_description[k]
            n = v.get('desc','')

            x = f"    * '{k}'"

            if n != '': x += '   {}'.format(n)

            print (x)

    return {'return':0}
