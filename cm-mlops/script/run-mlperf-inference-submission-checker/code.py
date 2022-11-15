# Developer: Grigori Fursin

import os
import pandas

def main():
    print ('=========================================================')

    print ('Searching for summary.csv ...')

    if os.path.isfile('summary.csv'):
        print ('Converting to json ...')

        import pandas

        df = pandas.read_csv('summary.csv').T

        print ('')
        print (df)
        print ('')

        df.to_json('summary.json', orient='columns', indent=4)

    print ('=========================================================')

if __name__ == '__main__':
    main()
