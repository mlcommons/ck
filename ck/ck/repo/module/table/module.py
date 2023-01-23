#
# Collective Knowledge (dealing with table)
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
# draw table

def draw(i):
    """
    Input:  {
              table   - table to draw [[],[],[]...], [[],[],[]...] ...]

              (out)   - txt (default) or html
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              string       - output
            }

    """

    o=i.get('out','')

    table=i.get('table',[])

    s=''

    if len(table)>0:
       lx=len(table[0])

       lwidth=[]
       for l in range(0, lx):
           lwidth.append(-1)

       # If 'txt', check length of all entries
       if o=='txt':
          for t in table:
              for l in range(0, lx):
                  sx=str(t[l])
                  lw=lwidth[l]
                  if lw==-1 or len(sx)>lw: 
                     lwidth[l]=len(sx)


          for t in table:
              for l in range(0, lx):
                  sx=str(t[l])
                  lw=lwidth[l]

                  s+=sx.ljust(lw+2)
              s+='\n'
       else:
          s='<html>\n'
          s+=' <body>\n'
          s+='  <table border="1">\n'
          for t in table:
              s+='  <tr>\n'
              for l in range(0, lx):
                  sx=str(t[l])
                  s+='    <td>'+sx+'</td>\n'
              s+='   </tr>\n'
          s+='  </table>\n'
          s+=' </body>\n'
          s+='<html>\n'

    return {'return':0, 'string':s}

##############################################################################
# prepare table (in HTML and LaTex)

def prepare(i):
    """
    Input:  {
              table
              table_header
              (table_custom)

              (table_style)
              (header_style)
              (header_element_style)
              (element_style)
              (row_style)

              (html_before_table)
              (html_after_table)

              (tex_before_table)
              (tex_after_table)

              (record_html) - file (with path) to record produced HTML
              (record_tex) - file (with path) to record produced TEX

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html - prepared HTML
              tex  - prepared :aTex
            }

    """

    table=i['table']
    table_header=i['table_header']
    table_custom=i.get('table_custom',{})

    h=i.get('html_before_table','') # HTML
    t=i.get('tex_before_table','')  # LaTex

    ts=i.get('table_style','')
    hs=i.get('header_style','')
    rs=i.get('row_style','')
    hes=i.get('header_element_style','')
    es=i.get('element_style','')

    # Preparing Header
    h+='<table '+ts+'>\n'

    t+='    \\begin{tabular}{|'

    for x in table_header:
        t+=x.get('tex','')+'|'

    t+='}\n'

    h+=' <tr '+hs+'>\n'
    t+='     \\hline\n'
    t+='      '

    first=True
    for x in table_header:
        n=x.get('name','')

        if first:
           first=False
        else:
           t+=' & '

        t+='\\textbf{'+n+'}'

        if x.get('html_change_space','')=='yes':
           n=n.replace(' ','&nbsp;')

        h+='  <td '+hes+'>\n'
        h+='   <b>'+n+'</b>\n'
        h+='  </td>\n'

    h+=' </tr>\n'
    t+=' \\\\ \n'

    # Preparing table
    for ix in range(0, len(table)):
        x=table[ix]

        cx={}
        if ix<len(table_custom):
           cx=table_custom[ix]

        rs1=cx.get('row_style','')

        h+=' <tr '+rs+' '+rs1+'>\n'

        t+='     \\hline\n'
        t+='      '

        first=True
        for iy in range(0, len(x)):
            st={}
            if iy<len(table_header):
               st=table_header[iy]

            y=cx.get('field_'+str(iy)+'_html','')
            if y=='':
               y=str(x[iy])

            if st.get('html_change_space','')=='yes':
               y=y.replace(' ','&nbsp;')

            y=y.replace('\\newline',' ')

            h+='  <td '+es+'>\n'
            if st.get('html_before','')!='':
               h+='   '+st['html_before']
            h+='   '+str(y)+'\n'
            if st.get('html_after','')!='':
               h+='   '+st['html_after']
            h+='  </td>\n'

            z=cx.get('field_'+str(iy)+'_tex','')
            if z=='':
               z=str(x[iy])

            if first:
               first=False
            else:
               t+=' & '

            if st.get('tex_before','')!='':
               t+=st['tex_before']
            t+=' '+str(z)+' '
            if st.get('tex_after','')!='':
               t+=st['tex_after']

        t+='\\\\\n'

        h+=' </tr>\n'
        
    t+="     \\hline\n"

    # Finalizing
    h+='</table>\n'
    h+=i.get('html_after_table','')

    t+='    \\end{tabular}'
    t+='    '+i.get('tex_after_table','')

    # Check if record
    if i.get('record_html','')!='':
       r=ck.save_text_file({'text_file':i['record_html'], 'string':h})

    if i.get('record_tex','')!='':
       r=ck.save_text_file({'text_file':i['record_tex'], 'string':t})

    return {'return':0, 'html':h, 'tex':t}
