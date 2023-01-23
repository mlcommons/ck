#
# Collective Knowledge (dealing with .dot graph files)
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
# converting .dot file made by machine learning algorithms to active decision tree

def convert_to_decision_tree(i):
    """
    Input:  {
              input_file          - .dot file
              output_file         - CK json decision tree file
              (caption)           - add caption, if needed
              (labels)            - Yes/No by default (can be True/False) 
              (problem_threshold) - float; if samples1/samples2 in the final leaf is more than this threshold
                                    add *X* to the final answer to show that there is a possible misprediction.
                                    By default = 0.12
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              labels
              decisions
              link_yes
              link_no
            }

    """

    dlabels=i.get('labels',[])
    if len(dlabels)==0: dlabels=cfg['labels']

    fi=i['input_file']
    fo=i['output_file']

    cap=i.get('caption','')

    s=''
    r=ck.load_text_file({'text_file':fi, 
                         'split_to_list':'yes'})
    if r['return']>0: return r
    lst=r['lst']

    pt=i.get('problem_threshold','')
    if pt=='': pt=0.12
    pt=float(pt)

    jl=1
    labels={}
    kl=1
    decisions={}
    link={}
    link_yes={}
    link_no={}

    mo=False

    # Detecting all labels (leafs) and decisions
    for j in range(0, len(lst)):
        q=lst[j]

        ll=''
        j1=q.find(' ')
        if j1>0:
           ll=q[:j1].strip()

        classes={}

        j0=q.find('\\nvalue = [')
        if j0>0 and q.find('"X[')<0:
           j2=q.find('[label="')
           if j2>0:
              sjl=str(jl)
              x=q[:j2+8]+'*L'+sjl+'*\\n'+q[j2+8:]

              lst[j]=x

              labels[sjl]={'dot_label':ll}

              j3=q.find(']',j0+1)
              vals=q[j0+11:j3].strip().replace('\\n',', ')

              svalsx=vals.split(' ')
              svals=[]

              for vv in svalsx:
                  if vv!='':
                     if vv.endswith('.'):
                        vv=vv[:-1]
                     if vv.endswith(','):
                        vv=vv[:-1]
                     vv=int(vv)
                     svals.append(vv)

              if len(svals)==2:
                 # True of False classifier
                 v0=svals[0]
                 v1=svals[1]

                 if v0>v1: value=False
                 else: value=True
              else:
                 # Multiple objects
                 mo=True

                 im=max(svals)

                 xx=[]

                 value=-1
                 for ivv in range(0, len(svals)):
                     vv=svals[ivv]
                     if float(vv)==float(im):
                        value=ivv
                        break

                 if value!=-1:
                    classes[vals]={'class':value, 'count':vv, 'sum':sum(svals)}

              labels[sjl]['value']=value

              jl+=1
        else:
           j1=q.find('[label="')
           if j1>0:
              j2=q.find('\\n',j1+1)
              j3=q.find(']',j1+1)
              j4=q.find(' ',j1+1)
              j5=q.find(' ',j4+1)

              dx={}
              dx['feature']=q[j1+10:j3]
              dx['comparison']=q[j4+1:j5]
              dx['value']=q[j5+1:j2]

              j1=q.find(' ')
              l1=q[:j1].strip()

              decisions[ll]=dx

           j1=q.find(' -> ')
           if j1>0:
              j2=q.find(';', j1+1)
              j2x=q.find('[',j1+1)
              if j2x<j2: j2=j2x

              ll2=q[j1+4:j2].strip()

              if ll in link: 
                 lbb='no'
                 link_no[ll2]=ll
              else:
                 link[ll]='+'
                 link_yes[ll2]=ll
                 lbb='yes'

              lst[j]=q[:j2]+'[label="'+lbb+'"];'

        # Remove gini (difficult to interpret)
        q=lst[j]

        qq=''

        j1=q.find('value = [')
        if j1>0:
           j2=q.find(']',j1)
           if j2>0:
              qx=q[j1+9:j2].strip().replace('\\n',', ')

              qa=qx.split(' ')
              qb=[]

              for vv in qa:
                  if vv!='':
                     if vv.endswith('.'):
                        vv=vv[:-1]
                     if vv.endswith(','):
                        vv=vv[:-1]
                     vv=int(vv)
                     qb.append(vv)

              if len(qb)==2:
                 # YES/NO
                 final_answer=dlabels[0]
                 if qb[0]<qb[1]: final_answer=dlabels[1]

                 problem=False
                 if qb[0]<qb[1] and qb[1]!=0 and (float(qb[0])/float(qb[1]))>pt: problem=True
                 if qb[0]>=qb[1] and qb[0]!=0 and (float(qb[1])/float(qb[0]))>pt: problem=True
                 if problem: final_answer='*'+final_answer+'*'

                 q=q[:j1]+dlabels[0]+' ('+str(qb[0])+') / '+dlabels[1]+' ('+str(qb[1])+')\\n\\n'+final_answer+q[j2+1:]
              else:
                 # Multiple
                 xx=classes.get(qx,{})
                 xxc=xx.get('class',-1)
                 xxn=xx.get('count',1)
                 xxs=xx.get('sum',1)

                 ss=''
                 if xxc!=-1:
                    ss='S'+str(xxc)+' ('+str(xxn)+')\\n'

                 q=q[:j1]+ss+q[j2+1:]

        j1=q.find('gini = ')
        if j1>0:
           j2=q.find('\\n',j1)
           if j2>0:
              q=q[:j1]+qq+q[j2+2:]

        s+=q+'\n'

        # If first line, add caption
        if j==0 and cap!='':
           s+='label="'+cap+'";\n'
           s+='fontsize=16;\n'
           s+='fontname=Helvetica;\n'
           s+='fontcolor=Blue;\n'
           s+='labelloc=top;\n'
           s+='labeljust=center;\n'
           s+='\n'

    # Finding path to a given leaf
    for ll in labels:
        l=labels[ll]

        dl=l['dot_label']

        dt=[]

        lx=dl
        value=''
        while lx!='0':
           x=''
           if lx in link_yes:
              lx=link_yes[lx]
           else:
              lx=link_no[lx]
              x='not '

           dt.append(x)
           dt.append(decisions[lx])

        # reverse for top bottom check
        dt1=[]
        ldt=len(dt)
        for q in range(0, ldt, 2):
            dt1.append(dt[ldt-q-2])
            dt1.append(dt[ldt-q-1])

        l['decision']=dt1

    # Save labels + decisions file
    r=ck.save_json_to_file({'json_file':fo, 'dict':labels})
    if r['return']>0: return r

    # Update .dot file
    r=ck.save_text_file({'text_file':fi, 'string':s})
    if r['return']>0: return r

    return {'return':0, 'labels':labels, 'decisions':decisions, 'link_yes':link_yes, 'link_no':link_no}
