import os
from cmind import utils
    
# Pring help about script
def print_help(i):

    meta = i['meta']
    path = i['path']

    print ('')
    print ('Help for this CM script ({},{}):'.format(meta.get('alias',''), meta.get('uid','')))

    print ('')
    print ('Path to this automation recipe: {}'.format(path))

    variations = meta.get('variations',{})
    if len(variations)>0:
        print ('')
        print ('Available variations:')
        print ('')
        for v in sorted(variations):
            print ('  _'+v)

    input_mapping = meta.get('input_mapping', {})
    if len(input_mapping)>0:
        print ('')
        print ('Available flags mapped to environment variables:')
        print ('')
        for k in sorted(input_mapping):
            v = input_mapping[k]

            print ('  --{}  ->  --env.{}'.format(k,v))

    input_description = meta.get('input_description', {})
    if len(input_description)>0:
        # Check if has important ones (sort)
        sorted_keys = []
        all_keys = sorted(list(input_description.keys()))

        for k in sorted(all_keys, key = lambda x: input_description[x].get('sort',0)):
            v = input_description[k]
            if v.get('sort',0)>0:
                sorted_keys.append(k)
        
        
        print ('')
        print ('Available flags (Python API dict keys):')
        print ('')
        for k in all_keys:
            v = input_description[k]
            n = v.get('desc','')

            x = '  --'+k
            if n!='': x+='  ({})'.format(n)

            print (x)

        if len(sorted_keys)>0:
            print ('')
            print ('Main flags:')
            print ('')
            for k in sorted_keys:
                v = input_description[k]
                n = v.get('desc','')

                x = '  --'+k

                d = None
                if 'default' in v:
                    d = v.get('default','')

                if d!=None:
                    x+='='+d

                c = v.get('choices',[])
                if len(c)>0:
                    x+='   {'+','.join(c)+'}'

                if n!='': x+='   ({})'.format(n)

                print (x)



    print ('')
    input ('Press Enter to see common flags for all scripts')

    return {'return':0}
