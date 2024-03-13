# Taken from https://github.com/mlcommons/croissant/pull/564/files (@mkuchnik)

import os
import mlcroissant as mlc

def main():
    
    url = os.environ.get('CM_PRINT_CROISSANT_URL', '')

    if url=='':
        print ('Error: --url is not specified')
        exit(1)
    
    ds = mlc.Dataset(url)
    metadata = ds.metadata.to_json()

    print ('')
    print ('Croissant meta data URL: {}'.format(url))
    print ('')
    print (f"{metadata['name']}: {metadata['description']}")

    print ('')
    for x in ds.records(record_set="default"):
        print(x)

if __name__ == '__main__':
    main()
