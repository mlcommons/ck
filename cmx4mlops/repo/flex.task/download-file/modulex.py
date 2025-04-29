# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow
    cmind = i['cmind']

    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    env = _input2.get('env', {})
    url = _input.get('url', '')
    filename = _input.get('filename', '')
    check_file = _input.get('check_file', '')
    md5sum = _input.get('md5sum', '')
    directory = _input.get('directory', '')
    tool = _input.get('tool', '')
    verify_ssl = _input.get('verify_ssl', False)
    unzip = _input.get('unzip', False)
    clean_after_unzip = _input.get('clean_after_unzip', False)
    strip_folders = _input.get('strip_folders', 0)
    clean = _input.get('clean', False)
    timeout = _input.get('timeout', None)

    # Check input correctness
    if url == '':
        return cmind.prepare_error(1, 'URL is empty')

    if timeout == '': timeout = None

    if type(url) == list:
        urls = url
    else:
        if ',' in url:
            urls = url.split(',')
        else:
            urls = [url]

    if type(filename) == list:
        files = filename
    else:
        if ',' in filename:
            files = filename.split(',')
        elif filename != '':
            files = [filename]
        else:
            files = []

    if type(md5sum) == list:
        md5sums = md5sum
    else:
        if ',' in md5sum:
            md5sums = md5sum.split(',')
        elif md5sum != '':
            md5sums = [md5sum]
        else:
            md5sums = []

    ###################################################################
    workdir = os.getcwd()

    if directory == '':
        path_to_files = workdir
    else:
        if os.path.isabs(directory):
            path_to_files = directory
        else:
            path_to_files = os.path.join(workdir, directory)

        if os.path.isdir(path_to_files):
            if clean:
                if verbose:
                    print ('')
                    print (f'RUN rm {path_to_files}')
                import shutil
                shutil.rmtree(path_to_files)

        if not os.path.isdir(path_to_files):
            os.makedirs(path_to_files)

    ###################################################################
    # Check file
    rrr = {'return':0, 'path_to_files': path_to_files}

    if check_file != '':
        check_file_with_path = os.path.join(path_to_files, check_file)
        if os.path.isfile(check_file_with_path):
            rrr['path_to_check_file'] = check_file_with_path
            return rrr

    ########\###########################################################
    # Prepare CMDs
    rr = {}

    success = False
    error = ''
    for u in range(0, len(urls)):
        url = urls[u]

        if len(files)>0:
            filename = files[u]
        else:
            urltail = os.path.basename(url)
            urlhead = os.path.dirname(url)

            if "." in urltail and "/" in urlhead:
                # Check if ? after filename
                j = urltail.find('?')
                if j>0:
                    urltail=urltail[:j]
                filename = urltail

            else:
                filename = "index.html"

        filename_with_path = os.path.join(path_to_files, filename)

        # Check if need to clean
        if os.path.isfile(filename_with_path) and clean:
            os.remove(filename_with_path)

        # Download if doesn't exist
        if not os.path.isfile(filename_with_path):
            if tool == 'cmx':
                rr = cmind.x({'action':'download_file',
                              'automation':self_meta['use']['flex.common'],
                              'url':url,
                              'filename':filename,
                              'path':directory,
                              'verify': verify_ssl,
                              'control': {'out':out},
                              'verbose': verbose})
                if rr['return'] == 0:
                    success = True
                else:
                    error = rr['error']

            else:
                return {'return':1, 'error':f'download tool {tool} is not yet supported in Flex Task'}
        else:
            success = True

        if success:
            if len(md5sums)>0:
                md5sum = md5sums[u]

                if verbose:
                    print ('')
                    print (f'RUN Checking md5sum for {filename}: {md5sum}')

                r = cmind.x({'action':'md5sum',
                             'automation':self_meta['use']['flex.common'],
                             'filename':filename_with_path})
                if r['return'] >0: return r

                md5sum_calculated = r['md5sum']

                if md5sum_calculated != md5sum:
                    error = f'md5sum failed: {md5sum_calculated}'
                    success = False

        if success:
            break    

    if not success:
        return {'return':1, 'error':f"failed downloading file from {','.join(urls)}\n{error}"}

    filesize = os.path.getsize(filename_with_path)

    if unzip:
        if filename.endswith('.zip'):
            if verbose:
                print ('')
                print (f'RUN unzip {filename_with_path}')

            if strip_folders != '': strip_folders = int(strip_folders)

            ii = {'action':'unzip_file',
                  'automation':self_meta['use']['flex.common'],
                  'filename':filename_with_path,
                  'path':directory,
                  'strip_folders':strip_folders}

            r= cmind.x(ii)
            if r['return'] >0: return r

            if clean_after_unzip:
                if verbose:
                    print (f'RUN rm {filename_with_path}')

                os.remove(filename_with_path)

        else:
            return {'return':1, 'error':f'extension is not yet supported for unzip {filename}'}
          

    ###################################################################
    # Check file again
    if check_file != '':
        check_file_with_path = os.path.join(path_to_files, check_file)
        if os.path.isfile(check_file_with_path):
            rrr['path_to_check_file'] = check_file_with_path

    rrr['path_to_file'] = filename_with_path
    rrr['features'] = {'file_size': filesize}

    if console:
        if verbose:
            print ('')
            print (f'FILE {filename_with_path}')
        else:
            print (f'Downloaded file: {filename_with_path}')

    return rrr
