import cmind

r=cmind.access('ls contributor .')
if r['return']>0: 
    cmind.error(r)

for l in r['list']:
    meta = l.meta

    org = meta.get('organization','').strip()

    if org!='' and org.endswith(')'):
        org = org[:-1]

        j=org.rfind('(')
        if j>0:
           org = org[:j-1]+', '+org[j+1:]

           meta['organization'] = org
           print (meta['alias'])
           print ('  '+org)

           ii={'action':'update',
               'automation':'contributor',
               'artifact':meta['uid'],
               'meta':meta,
               'replace':True}

           r=cmind.access(ii)
           print (r)
           if r['return']>0:
               cmind.error(r)
