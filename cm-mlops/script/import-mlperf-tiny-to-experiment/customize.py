import cmind as cm
from cmind import utils

import os
import subprocess
import json

file_summary_json = 'mlperf-inference-summary.json'
file_result = 'cm-result.json'

fix_benchmark_names = {'anomaly_detection':'ad',
                       'image_classification':'ic',
                       'keyword_spotting':'kws',
                       'visual_wake_words':'vww'}

def preprocess(i):

    env = i['env']

    cur_dir = os.getcwd()

    # Query cache for results dirs
    r = cm.access({'action':'find',
                   'automation':'cache,541d6f712a6b464e',
                   'tags':'get,repo,mlperf-tiny-results'})
    if r['return']>0: return r

    lst = r['list']

    for c in lst:
        path = os.path.join(c.path, 'repo')

        if os.path.isdir(path):
            meta = c.meta

            tags = meta['tags']

            version = ''
            for t in tags:
                if t.startswith('version-'):
                    version = 'v'+t[8:]
                    break

            r = convert_repo_to_experiment(path, version, env)
            if r['return']>0: return r

    print ('')

    return {'return':0}


def convert_repo_to_experiment(path, version, env):
    print ('')
    print ('Processing MLPerf repo from CM cache path: {}'.format(path))
    print ('* Version: {}'.format(version))

    cur_dir = os.getcwd()

    # Get Git URL
    os.chdir(path)

    burl = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
    url = burl.decode('UTF-8').strip()

    print ('* Git URL: {}'.format(url))

    # Create virtual experiment entries
    experiments = {}

    for division in ['closed', 'open']:
        p1 = os.path.join(path, division)
        if os.path.isdir(p1):
            print ('  * Processing division: {}'.format(division))

            companies = os.listdir(p1)

            for company in companies:
                p2 = os.path.join (p1, company)
                if os.path.isdir(p2):
                    print ('    * Processing company: {}'.format(company))

                    presults = os.path.join(p2, 'results')
                    psystems = os.path.join(p2, 'systems')
                    pcode = os.path.join(p2, 'code')

                    if os.path.isdir(presults) and os.path.isdir(psystems) and os.path.isdir(pcode):
                        #  Exception for OctoML
                        presults2 = [presults]

                        if company == 'OctoML' and version == 'v1.0':
                            presults2 = []

                            p3 = os.listdir(presults)
                            for p3x in p3:
                                p3y = os.path.join(presults, p3x)
                                if os.path.isdir(p3y):
                                    presults2.append(p3y)

                        for presult in presults2:
                            systems = os.listdir(presult)
                            for system in systems:
                                psystem = os.path.join(presult, system)
                                if os.path.isdir(psystem):
                                    print ('      * Processing result for system: {}'.format(system))

                                    # Check system file
                                    psystem_desc = os.path.join(psystems, system+'.json')
                                    psystem_dict = {}

                                    print ('                                File: {}'.format(psystem_desc))

                                    # Check exceptions
                                    if version == 'v1.0':
                                        if company == 'OctoML':
                                            x = os.path.basename(presult)
                                            psystem_desc = os.path.join(psystems, 'system_description_'+system.replace('-','')+'_'+x+'.json')
                                        elif company == 'STMicroelectronics':
                                            psystem_desc = os.path.join(psystems, system, system+'_system_description.json')
                                            if not os.path.isfile(psystem_desc):
                                                psystem_desc = os.path.join(psystems, system, system.replace('-','_')+'_system_description.json')
                                        elif company == 'syntiant':
                                            psystem_desc = os.path.join(psystems, system, system+'.json')
                                        elif company == 'hls4ml':
                                            psystem_desc = os.path.join(psystems, 'system_description_pynq.json')
                                    elif version == 'v0.7':
                                        if company == 'renesas':
                                            psystem_desc = os.path.join(psystems, system+'_System_Description.json')
                                        elif company == 'STMicroelectronics':
                                            psystem_desc = os.path.join(psystems, system, system+'_system_description.json')
                                            if not os.path.isfile(psystem_desc):
                                                psystem_desc = os.path.join(psystems, system, system.replace('-','_')+'_system_description.json')
                                        elif company == 'syntiant':
                                            psystem_desc = os.path.join(psystems, system, system+'.json')
                                        elif company == 'hls4ml-finn':
                                            psystem_desc = os.path.join(psystems, 'system_description_'+system[:4]+'.json')


                                    if os.path.isfile(psystem_desc):
                                        x = ''
                                        if version == 'v1.0':
                                            if company == 'OctoML':
                                                x='}\n\t"'
                                            elif company == 'syntiant':
                                                x='"\n\t"'
                                            elif company == 'hls4ml':
                                                x='dummy'
                                        elif version == 'v0.7':
                                            if company == 'syntiant':
                                                x='"\n\t"'

                                        if x!='':
                                            r = utils.load_txt(psystem_desc)
                                            if r['return']>0: return r

                                            s = r['string']

                                            j = s.find(x)
                                            if j>=0:
                                                s=s[:j+1]+','+s[j+1:]

                                            if s.endswith(',\n'):
                                                s=s[:-2]+'}'

                                            psystem_dict = json.loads(s)

                                        else:
                                            r = utils.load_json(psystem_desc)
                                            if r['return']>0: return r
                                            psystem_dict = r['meta']

                                    else:
                                        print ('           * Warning: system description not found in {}'.format(psystem_desc))
                                        input ('             Press <Enter> to continue')

                                    for benchmark in os.listdir(psystem):
                                        pbenchmark = os.path.join(psystem, benchmark)
                                        if os.path.isdir(pbenchmark):
                                            print ('         * Processing benchmark: {}'.format(benchmark))

                                            models = ['']

                                            # May have retrained models
                                            pperf = os.path.join(pbenchmark, 'performance', 'results.txt')
                                            if not os.path.isfile(pperf):
                                                pperf = os.path.join(pbenchmark, 'performance', 'performance_results.txt')

                                            if not os.path.isfile(pperf):
                                                # likely models
                                                models = []

                                                for model in os.listdir(pbenchmark):
                                                    pmodel = os.path.join(pbenchmark, model)
                                                    if os.path.isdir(pmodel):
                                                        models.append(model)

                                            for model in models:

                                                results = {}

                                                if model!='':
                                                    print ('           * Processing model: {}'.format(model))
                                                    pbenchmark = os.path.join(psystem, benchmark, model)

                                                perf_file_type=0
                                                pperf = os.path.join(pbenchmark, 'performance', 'results.txt')
                                                if not os.path.isfile(pperf):
                                                    pperf = os.path.join(pbenchmark, 'performance', 'performance_results.txt')
                                                    perf_file_type=1 # outdated/weird

                                                paccuracy = os.path.join(pbenchmark, 'accuracy', 'results.txt')
                                                if not os.path.isfile(paccuracy):
                                                    paccuracy = os.path.join(pbenchmark, 'accuracy', 'accuracy_results.txt')

                                                penergy = os.path.join(pbenchmark, 'energy', 'results.txt')

                                                if os.path.isfile(pperf) and os.path.isfile(paccuracy):
                                                    r = utils.load_txt(pperf)
                                                    if r['return']>0: return r

                                                    s = r['string']

                                                    median_throughput=0

                                                    x1='Median throughput is ' if perf_file_type==0 else 'Throughput   :'
                                                    x2=21 if perf_file_type==0 else 18

                                                    j = s.find(x1)
                                                    if j>=0:
                                                        j1 = s.find(' inf./sec.', j)
                                                        if j1>=0:
                                                            median_throughput=float(s[j+x2:j1].strip())
                                                            results['median_throughput']=median_throughput
                                                            results['median_throughput_metric']='inf./sec.'
                                                            results['Result']=median_throughput
                                                            results['_Result']=median_throughput

                                                    if median_throughput==0:
                                                        print ('           * Warning: median_throughput was not detected in {}'.format(pperf))
                                                        input ('             Press <Enter> to continue')

                                                    r = utils.load_txt(paccuracy, split=True)
                                                    if r['return']>0: return r

                                                    lines = r['list']

                                                    found=False

                                                    for line in lines:
                                                        j = line.find('ulp-mlperf: ')
                                                        if j>=0:
                                                           j1 = line.find(':', j+12)
                                                           if j1>=0:
                                                               accuracy_key = 'accuracy_'+line[j+12:j1]
                                                               value = line[j1+2:]

                                                               if value.endswith('%'):
                                                                   value = value[:-1]
                                                                   results[accuracy_key+'_metric']='%'

                                                               value = float(value)

                                                               results[accuracy_key] = value

                                                               if not found:
                                                                   # first value
                                                                   results['Accuracy'] = value
                                                                   results['_Accuracy'] = value


                                                               found = True

                                                    if not found:
                                                        print ('           * Warning: accuracy not found in the file {}'.format(paccuracy))
                                                        input ('             Press <Enter> to continue')

                                                else:
                                                    print ('           * Warning: performance or accuracy files are not present in this submission')
                                                    input ('             Press <Enter> to continue')

                                                if os.path.isfile(penergy):
                                                    r = utils.load_txt(penergy)
                                                    if r['return']>0: return r

                                                    s = r['string']

                                                    median_throughput=0

                                                    j = s.find('Median throughput is ')
                                                    if j>=0:
                                                        j1 = s.find(' inf./sec.', j)
                                                        if j1>=0:
                                                            median_throughput=float(s[j+21:j1])

                                                            results['median_energy_median_throughput']=median_throughput
                                                            results['median_energy_median_throughput_metric']='inf./sec.'

                                                    if median_throughput==0:
                                                        print ('           * Warning: median_throughput was not detected in {}'.format(penergy))
                                                        input ('             Press <Enter> to continue')
                                                    else:
                                                        median_energy_cost=0

                                                        j = s.find('Median energy cost is ')
                                                        if j>=0:
                                                            j1 = s.find(' uJ/inf.', j)
                                                            if j1>=0:
                                                                median_energy_cost=float(s[j+22:j1])

                                                                results['median_energy_cost']=median_energy_cost
                                                                results['median_energy_cost_metric']='uj/inf.'

                                                        if median_energy_cost==0:
                                                            print ('           * Warning: median_energy_cost was not detected in {}'.format(penergy))
                                                            input ('             Press <Enter> to continue')

                                                print ('           * Results dict: {}'.format(results))

                                                # Finalizing keys
                                                results.update(psystem_dict)

                                                xbenchmark = benchmark if benchmark not in fix_benchmark_names else fix_benchmark_names[benchmark]

                                                results['git_url']=url+'/tree/master/'+division+'/'+company

                                                results['version']=version
                                                results['__version']=version
                                                results['Organization']=company
                                                results['__Organization']=company
                                                results['Division']=division
                                                results['Benchmark']=xbenchmark
                                                results['__System']=system

                                                if model!='':
                                                    results['Model']=model
                                                    results['__Model']=model


                                                # Prepare experiment name
                                                cm_name = 'mlperf-tiny--{}--'+division+'--'+xbenchmark
                                                print ('           * CM experiment name: {}'.format(cm_name))

                                                name_all = cm_name.format('all')
                                                name_ver = cm_name.format(version)

                                                for name in [name_all, name_ver]:
                                                    if name not in experiments: experiments[name]=[]
                                                    experiments[name].append(results)


                    else:
                        print ('      * Warning: some directories are not present in this submission')
                        input ('        Press <Enter> to continue')

    os.chdir(cur_dir)

    r=utils.save_json(file_summary_json, experiments)
    if r['return']>0: return r

    env_target_repo=env.get('CM_IMPORT_TINYMLPERF_TARGET_REPO','').strip()
    target_repo='' if env_target_repo=='' else env_target_repo+':'

    # Checking experiment
    print ('')
    for name in experiments:
        print ('    Preparing experiment artifact "{}"'.format(name))

        tags = name.split('--')
        if 'mlperf' not in tags: tags.insert(0, 'mlperf')

        # Checking if experiment already exists
        r = cm.access({'action':'find',
                       'automation':'experiment,a0a2d123ef064bcb',
                       'artifact':target_repo+name})
        if r['return']>0: return r

        lst = r['list']

        if len(lst)==0:
            r = cm.access({'action':'add',
                           'automation':'experiment,a0a2d123ef064bcb',
                           'artifact':target_repo+name,
                           'tags':tags})
            if r['return']>0: return r

            path = r['path']
        else:
            path = lst[0].path

        results = experiments[name]

        # Check if already date directory
        dirs = os.listdir(path)

        path2 = ''
        for d in dirs:
            dd = os.path.join(path, d)
            if os.path.isdir(dd):
                path2 = dd
                break

        if path2=='':

            r = utils.get_current_date_time({})
            if r['return']>0: return r

            date_time = r['iso_datetime'].replace(':','-').replace('T','.')

            path2 = os.path.join(path, date_time)

            os.makedirs(path2)

        # Check if cm-result.json
        fresult = os.path.join(path2, file_result)

        if os.path.isfile(fresult):
            r=utils.load_json(fresult)
            if r['return']>0: return r

            existing_results = r['meta']

            # Need to check which ones to add
            for result in existing_results:
                found = False

                # New results
                for result2 in results:
                    matched = True

                    # Need to iterate over keys in the new results since old results can have more keys (derivates, etc)
                    for k in result2:
                        if k!='uid':
                            if k not in result or result2[k]!=result[k]:
                                matched = False
                                break

                    if matched:
                        found = True
                        break

                if not found:
                    results.append(result)

        # Check extra keys
        final_results=[]
        for result in results:
            # Generate UID
            if 'uid' not in result:
                r=utils.gen_uid()
                if r['return']>0: return r

                result['uid'] = r['uid']

        # Write results
        r=utils.save_json(fresult, results)
        if r['return']>0: return r


    return {'return':0}
