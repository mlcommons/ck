#
# Collective Knowledge (processing XML)
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
# validate XML against DTD

def validate(i):
    """
    Input:  {
              (data_uoa) - if specified use DTD file from that entry
              (dtd_module_uoa) - if specified use DTD file from that entry, otherwise 'xml'
              dtd_file   - DTD file
              xml_file   - XML file to be validated
            }

    Output: {
              return       - return code =  0, if successfully validated
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    from lxml import etree

    ocon=i.get('out','')=='con'

    # Checking entry with DTD if needed
    p=''
    duoa=i.get('data_uoa','')
    dd={}
    if duoa!='':
       muoa=i.get('dtd_module_uoa','')
       if muoa=='': muoa=i.get('module_uoa','')

       r=ck.access({'action':'load',
                    'module_uoa':muoa,
                    'data_uoa':duoa})
       if r['return']>0: return r

       p=r['path']
       dd=r['dict']

    # Checking DTD file
    dtd_file=i.get('dtd_file','')
    if dtd_file=='': 
       dtd_file=dd.get('dtd_file','')
    if dtd_file=='': 
       return {'return':1, 'error':'"dtd_file" is not specified'}

    if p!='':
       dtd_file=os.path.join(p, dtd_file)

    if not os.path.isfile(dtd_file):
       return {'return':1, 'error':'DTD file not found ('+dtd_file+')'}

    xml_file=i.get('xml_file','')
    if xml_file=='': 
       return {'return':1, 'error':'"xml_file" is not specified'}

    if not os.path.isfile(xml_file):
       return {'return':1, 'error':'XML file not found ('+xml_file+')'}

    # Load DTD
    fdtd=open(dtd_file)
    DTD=etree.DTD(fdtd)

    # Load XML
    xml=etree.parse(xml_file)

    # Validate
    validated=DTD.validate(xml)
 
    fdtd.close()

    if not validated:
       return {'return':1, 'error':'XML was not validated:\n'+str(DTD.error_log.filter_from_errors())}

    if ocon:
       ck.out('XML file was successfully validated against DTD!')

    return {'return':0}


##############################################################################
# generate XML element
def generate_element(root, d):

    import os
    from lxml import etree

    if type(d)!=list:
       return {'return':1, 'error':'unknown format - expected list but got "'+str(type(d))+'"'}

    for l in d:
        if type(l)!=dict:
           return {'return':1, 'error':'unknown format - expected dict in a list but got "'+str(type(d))+'"'}

        if len(l)>1:
           return {'return':1, 'error':'unknown format - dict must have size 1 but got "'+str(len(l))+'"'}

        k=list(l.keys())[0]

        e=etree.Element(k)

        v=l[k]

        if type(v)==list:
           r=generate_element(e,v)
           if r['return']>0: return r
        else:
           v=str(v)
           if v!='':
              # Check $% %$
              if v.startswith('$%'):
                 j=v.find('%$')
                 if j>0:
                    v1=v[2:j].strip()
                    v=v[j+2:].strip()

                    # Convert JSON to dict (attributes)
                    r=ck.convert_json_str_to_dict({'str':v1, 'skip_quote_replacement':'yes'})
                    if r['return']>0: return r
                    attributes=r['dict']

                    e=etree.Element(k, attrib=attributes)

              e.text=v

        root.append(e)

    return {'return':0}

##############################################################################
# generate XML from DICT (JSON)

def generate(i):
    """
    Input:  {
              (json_file) - JSON file with dict in a specific format (starts with list, all leafs are also lists or values)
                 or
              (dict)      - dict in a specific format (starts with list, all leafs are also lists or values)

              (root_key)           - root name (such as "proceedings")
              (root_attributes)    - root attributes

              xml_file    - file to save XML

              (dtd_file)  - DTD file to validate produced XML

              if dtd_file!='':
                (data_uoa)       - if specified use DTD file from that entry
                (dtd_module_uoa) - if specified use DTD file from that entry, otherwise 'xml'

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    from lxml import etree

    ocon=i.get('out','')=='con'

    xml_file=i.get('xml_file','')
    if xml_file=='':
       return {'return':1, 'error':'"xml_file" is not defined'}

    # Get dictionary
    jf=i.get('json_file','')
    if jf!='':
       r=ck.load_json_file({'json_file':jf})
       if r['return']>0: return r

       d=r['dict']
    else:
       d=i.get('dict',[])

    # Prepare XML root
    root_key=i.get('root_key','')
    if root_key=='': root_key='root'

    attributes=i.get('root_attributes',{})
#    root = etree.Element('proceeding', ts='05/09/2017', ver='10.1')

    root = etree.Element(root_key, attrib=attributes)

    # Prepare XML doc (recursively)
    if ocon: ck.out('* Generating XML ...')
    r=generate_element(root,d)
    if r['return']>0: return r

#    root.append(r['element'])

    # Save to XML file
    if ocon: ck.out('* Recording XML ...')
    xml = etree.ElementTree(root)
    xml.write(xml_file, xml_declaration=True, encoding='UTF-8', pretty_print=True) 

    # Validating XML file
    dtd_file=i.get('dtd_file','')
    if dtd_file!='':
       if ocon: ck.out('* Validating XML ...')

       duoa=i.get('data_uoa','')
       muoa=i.get('dtd_module_uoa','')
       if muoa=='':
          muoa=work['self_module_uid']

       r=validate({'data_uoa':duoa,
                   'dtd_module_uoa':muoa,
                   'dtd_file':dtd_file,
                   'xml_file':xml_file})
       if r['return']>0: return r

    return {'return':0}
