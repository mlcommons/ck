import os

if __name__ == "__main__":

    print ('')
    print ('Main script:')
    print ('ENV CM_VAR1: {}'.format(os.environ.get('CM_VAR1','')))
    print ('')

    exit(0)
