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

        name = user['first']+' '+user['last']+' ('+user['affiliation']+')'

        print (name)

        html += '  <li>'+name+'\n'

    html += '</ul>\n'

    print (html)

    fo = f+'.html'

    cmind.utils.save_txt(fo, html)


    return {'return':0}


if __name__ == '__main__':
    main()
