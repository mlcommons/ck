import os
import csv
import json
import cmind

def main():
    f = os.environ.get('CM_PROCESS_AE_USERS_INPUT_FILE','')

    print ('Input CSV file: {}'.format(f))

    users = []
    with open(f, 'r') as ff:
        csvreader = csv.DictReader(ff)
        for row in csvreader:
            if len(row)>0:
                users.append(row)

    print ('')
    html = '<ul>\n'
    for user in sorted(users, key = lambda u: (u['last'].lower(), u['first'].lower())):

        full_name = user['first']+' '+user['last']
        
        name = full_name + ' ('+user['affiliation']+')'

        print (name)

        html += '  <li>'+name+'\n'

        # Checking contributor
        r = cmind.access({'action':'find',
                          'automation':'contributor',
                          'artifact':full_name})
        if r['return']>0: return r

        lst = r['list']

        if len(lst)==0:
            print ('  CM contributor not found!')

            meta = {
                    'challenges': [
                      'ae-micro2023'
                    ],
                    'last_participation_date': '202309',
                    'name': full_name,
                    'organization': user['affiliation']
                   }

            print ('  Adding to mlcommons@ck ...')
            r = cmind.access({'out':'con',
                              'action':'add',
                              'automation':'contributor,68eae17b590d4f8f', # Need UID since using common function
                              'artifact':'mlcommons@ck:'+full_name,
                              'meta':meta,
                              'common':True
                              })
            if r['return']>0: return r


    html += '</ul>\n'

    fo = f+'.html'

    print ('')
    print ('Saved HTML to {}'.format(fo))
    
    cmind.utils.save_txt(fo, html)



    return {'return':0}


if __name__ == '__main__':
    r=main()
    if r['return']>0:
        cmind.error(r)
