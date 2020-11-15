#
# Collective Knowledge - common functionality for MLPerf benchmarking.
#
# See CK LICENSE.txt for licensing details.
# See CK COPYRIGHT.txt for copyright details.
#
# Developers:
# - Leo Gordon, leo@dividiti.com
# - Anton Lokhmotov, anton@dividiti.com
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)

import getpass
import os
import sys
from pprint import pprint


def init(i):
    """
    Not to be called directly.
    """

    return {'return':0}


def compare_experiments_image_classification(frame_predictions):
    epsilon = 1e-5 # 1/1000th of a percent (1e-3 * 1e-2)
    max_delta = 0
    num_mismatched_files = 0
    num_mismatched_classes = 0
    num_mismatched_probabilities = 0
    num_mismatched_elementary_keys = 0
    for file_name in sorted(frame_predictions[0]):
        ck.out( 'Checking {}...'.format(file_name) )
        fp0 = frame_predictions[0][file_name]
        fp1 = frame_predictions[1][file_name]
        # Check elementary keys.
        for key in [ 'accuracy_top1', 'accuracy_top5', 'accuracy_topn', 'class_correct', 'class_topmost' ]:
            fp0_value = fp0[key]
            fp1_value = fp1[key]
            if fp0_value != fp1_value:
                ck.out( '- mismatched key {}: {} != {}'.format(key, fp0_value, fp1_value) )
                num_mismatched_elementary_keys += 1
        # Check topn.
        index = 0
        any_mismatched_classes = False
        any_mismatched_probabilities = False
        for (fp0_topn, fp1_topn) in zip(fp0['topn'], fp1['topn']):
            # Compare classes.
            if fp0_topn['index'] != fp1_topn['index']:
                ck.out( '- mismatched classes at index {}: {} != {}'.format(index, fp0_topn['index'], fp1_topn['index']) )
                num_mismatched_classes += 1
                any_mismatched_classes = True
            # Compare probabilities.
            delta = abs(fp0_topn['prob'] - fp1_topn['prob'])
            if delta > epsilon:
                ck.out( '- mismatched probabilities at index {}: | {:.5f} - {:.5f} | = {:.5f} > {:.5f}'.format(index, fp0_topn['prob'], fp1_topn['prob'], delta, epsilon) )
                num_mismatched_probabilities += 1
                any_mismatched_probabilities = True
            if delta > max_delta: max_delta = delta
            index += 1
        if any_mismatched_classes or any_mismatched_probabilities:
            num_mismatched_files += 1

    rdict = { 'return':0,
              'epsilon':epsilon,
              'max_delta':max_delta,
              'num_mismatched_files':num_mismatched_files,
              'num_mismatched_classes':num_mismatched_classes,
              'num_mismatched_probabilities':num_mismatched_probabilities,
              'num_mismatched_elementary_keys':num_mismatched_elementary_keys
    }

    return rdict


def compare_experiments_object_detection(frame_predictions):
    # Probabilities.
    epsilon_prob   = 1e-5 # 1/1000th of a percent (1e-3 * 1e-2)
    max_delta_prob = 0.0
    num_mismatched_probabilities = 0
    # Bounding boxes.
    epsilon_bbox   = [1.0, 1.0, 1.0, 1.0] # 1 pixel in any direction
    max_delta_bbox = [0.0, 0.0, 0.0, 0.0]
    num_mismatched_bboxes = 0
    # Squared distances of the centre of mass.
    epsilon_dist   = 100.0 # 10.0 squared
    max_delta_dist = 0.0
    num_mismatched_distances = 0
    # Files and classes.
    num_mismatched_files = 0
    num_mismatched_classes = 0

    for file_name in sorted(frame_predictions[0]):
        ck.out( 'Checking {}...'.format(file_name) )
        fp0 = frame_predictions[0][file_name]
        fp1 = frame_predictions[1][file_name] 
        if len(fp0['detections']) == len(fp1['detections']):
            mismatch_detected_objects_count = False
        else:
            ck.out( '- mismatch detected objects count: {} != {}'.format(len(fp0['detections']), len(fp1['detections'])) )
            mismatch_detected_objects_count = True

        index = 0
        any_mismatched_classes = False
        any_mismatched_probabilities = False
        any_mismatched_bbox = False
        for (fpa, fpb) in zip(fp0['detections'], fp1['detections']):
            # Extract the coordinates.
            fpa_x1 = fpa['bbox'][0]
            fpa_y1 = fpa['bbox'][1]
            fpa_x2 = fpa['bbox'][2]
            fpa_y2 = fpa['bbox'][3]
            fpb_x1 = fpb['bbox'][0]
            fpb_y1 = fpb['bbox'][1]
            fpb_x2 = fpb['bbox'][2]
            fpb_y2 = fpb['bbox'][3]
            # Compute the distance to the centre of mass.
            fpa_dist = ((fpa_x2-fpa_x1)*(fpa_x2-fpa_x1) + (fpa_y2-fpa_y1)*(fpa_y2-fpa_y1))/4
            fpb_dist = ((fpb_x2-fpb_x1)*(fpb_x2-fpb_x1) + (fpb_y2-fpb_y1)*(fpb_y2-fpb_y1))/4
            # Compare the distances.
            delta_dist = abs(fpa_dist - fpb_dist)
            if delta_dist > epsilon_dist:
                ck.out( '- mismatched distances at index {}: [{}] != [{}]'.format(index, fpa_dist, fpb_dist) )
                num_mismatched_distances += 1
            if delta_dist > max_delta_dist: max_delta_dist = delta_dist
            # Compare classes.
            if fpa['class'] != fpb['class']:
                ck.out( '- mismatched classes at index {}: [{}] != [{}]'.format(index, fpa['class'], fpb['class']) )
                num_mismatched_classes += 1
                any_mismatched_classes = True
            # Compare probabilities.
            delta_prob = abs(fpa['prob'] - fpb['prob'])
            if delta_prob > epsilon_prob:
                ck.out( '- mismatched probabilities at index {}: | {:.5f} - {:.5f} | = {:.5f} > {:.5f}'.format(index, fpa['prob'], fpb['prob'], delta_prob, epsilon_prob) )
                num_mismatched_probabilities += 1
                any_mismatched_probabilities = True
            if delta_prob > max_delta_prob: max_delta_prob = delta_prob
            # Compare coordinates.
            delta_x1 = abs(fpa_x1 - fpb_x1)
            delta_y1 = abs(fpa_y1 - fpb_y1)
            delta_x2 = abs(fpa_x2 - fpb_x2)
            delta_y2 = abs(fpa_y2 - fpb_y2)
            if delta_x1 > epsilon_bbox[0] or delta_y1 > epsilon_bbox[1] or delta_x2 > epsilon_bbox[2] or delta_y2 > epsilon_bbox[3]:
                ck.out( '- mismatched bbox at index {}: [{}] != [{}]'.format(index, fpa['bbox'], fpb['bbox']) )
                any_mismatched_bbox = True
                num_mismatched_bboxes += 1
            if delta_x1 > max_delta_bbox[0]: max_delta_bbox[0] = delta_x1
            if delta_y1 > max_delta_bbox[1]: max_delta_bbox[1] = delta_y1
            if delta_x2 > max_delta_bbox[2]: max_delta_bbox[2] = delta_x2
            if delta_y2 > max_delta_bbox[3]: max_delta_bbox[3] = delta_y2
            index += 1

        if mismatch_detected_objects_count or any_mismatched_probabilities or any_mismatched_bbox:
            num_mismatched_files +=1

    rdict = { 'return':0,
              'epsilon_prob':epsilon_prob,
              'max_delta_prob':max_delta_prob,
              'epsilon_bbox':epsilon_bbox,
              'max_delta_bbox':max_delta_bbox,
              'epsilon_dist':epsilon_dist,
              'max_delta_dist':max_delta_dist,
              'num_mismatched_files':num_mismatched_files,
              'num_mismatched_classes':num_mismatched_classes,
              'num_mismatched_distances':num_mismatched_distances,
              'num_mismatched_probabilities':num_mismatched_probabilities
    }

    return rdict


def compare_experiments(i):
    """
    Input:  {
                (cids[])            - up to 2 CIDs of entries to compare (interactive by default)
                (repo_uoa)          - experiment repository ('*' by default)
                (extra_tags)        - extra tags to search for CIDs
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    """
    cids = i.get('cids')
    repo_uoa = i.get('repo_uoa', '*')
    extra_tags = i.get('extra_tags', 'mlperf,accuracy')

    # Return an error if more than 2 CIDs have been provided.
    if len(cids) > 2:
        return {'return':1, 'error': 'only support up to 2 CIDs'}

    # Interactively select experiment entries if fewer than 2 CID have been provided.
    for i in range(len(cids),2):
        ck.out( 'Select experiment #{} for comparison:'.format(i) )
        pick_exp_adict = { 'action':       'pick_an_experiment',
                           'module_uoa':   'mlperf',
                           'repo_uoa':     repo_uoa,
                           'extra_tags':   extra_tags,
        }
        r=ck.access( pick_exp_adict )
        if r['return']>0: return r
        cids.append( r['cid'] )

    # Collect frame predictions.
    ck.out( '\nExperiments to compare:' )
    experiment_types  = []
    frame_predictions = []
    accuracy_top1     = []
    accuracy_top5     = []
    accuracy_mAP      = []
    accuracy_recall   = []
    for cid in cids:
        r=ck.parse_cid({'cid': cid})
        if r['return']>0:
            return { 'return': 1, 'error': "Cannot parse CID '{}'".format(cid) }
        else:
            repo_uoa    = r.get('repo_uoa','')
            module_uoa  = r.get('module_uoa','')
            data_uoa    = r.get('data_uoa','')

        # Load experimental point.
        load_point_adict = {    'action':           'load_point',
                                'repo_uoa':         repo_uoa,
                                'module_uoa':       module_uoa,
                                'data_uoa':         data_uoa,
        }
        r=ck.access( load_point_adict )
        if r['return']>0: return r

        point0001_characteristics_list = r['dict']['0001']['characteristics_list']
        point0001_characteristics0_run = point0001_characteristics_list[0]['run']
        point0001_frame_predictions    = point0001_characteristics0_run['frame_predictions']
        ck.out( '- {}: {} predictions'.format(cid, len(point0001_frame_predictions)) )
        frame_predictions.append(point0001_frame_predictions)

        # Load pipeline to determine experiment type from tags.
        load_pipeline_adict = { 'action':           'load_pipeline',
                                'repo_uoa':         repo_uoa,
                                'module_uoa':       module_uoa,
                                'data_uoa':         data_uoa,
        }
        r=ck.access( load_pipeline_adict )
        if r['return']>0: return r

        tags = r['pipeline']['tags'].split(',')
        if 'image-classification' in tags:
            experiment_types.append('image-classification')
            accuracy_top1.append(point0001_characteristics0_run['accuracy_top1'])
            accuracy_top5.append(point0001_characteristics0_run['accuracy_top5'])
        if 'object-detection' in tags:
            experiment_types.append('object-detection')
            accuracy_mAP.append(point0001_characteristics0_run['mAP'])
            accuracy_recall.append(point0001_characteristics0_run['recall'])

    unique_experiment_types = list(set(experiment_types))
    if len(unique_experiment_types)!=1:
        return { 'return': 2, 'error': "Mixed experiment types: '{}'".format(str(unique_experiment_types)) }
    experiment_type = unique_experiment_types[0]
    ck.out('Experiment type: {}'.format(experiment_type))
    if experiment_type=='image-classification':
        rdict = compare_experiments_image_classification(frame_predictions)
        rdict['delta_top1']   = accuracy_top1[0] - accuracy_top1[1]
        rdict['delta_top5']   = accuracy_top5[0] - accuracy_top1[1]
    elif experiment_type=='object-detection':
        rdict = compare_experiments_object_detection(frame_predictions)
        rdict['delta_mAP']    = accuracy_mAP[0] - accuracy_mAP[1]
        rdict['delta_recall'] = accuracy_recall[0] - accuracy_recall[1]
    else:
        return { 'return': 3, 'error': "Unknown experiment type: '{}'".format(experiment_type) }

    pprint( rdict )

    return rdict


def list_experiments(i):
    """
    Input:  {
                (repo_uoa)          - experiment repository name ('*' by default)
                (extra_tags)        - extra tags to filter
                (add_meta)          - request to return metadata with each experiment entry
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    """

    repo_uoa        = i.get('repo_uoa', '*')
    extra_tags      = i.get('extra_tags')
    all_tags        = 'mlperf' + ( ',' + extra_tags if extra_tags else '' )
    add_meta        = i.get('add_meta')

    search_adict    = { 'action':       'search',
                        'repo_uoa':     repo_uoa,
                        'module_uoa':   'experiment',
                        'data_uoa':     '*',
                        'tags':         all_tags,
                        'add_meta':     add_meta,
    }
    r=ck.access( search_adict )
    if r['return']>0: return r

    list_of_experiments = r['lst']

    repo_to_names_list = {}
    for entry in list_of_experiments:
        repo_uoa    = entry['repo_uoa']
        data_uoa    = entry['data_uoa']
        if not repo_uoa in repo_to_names_list:
            repo_to_names_list[ repo_uoa ] = []
        repo_to_names_list[ repo_uoa ] += [ data_uoa ]

    if i.get('out')=='con':
        for repo_uoa in repo_to_names_list:
            experiments_this_repo = repo_to_names_list[ repo_uoa ]
            ck.out( '{} ({}) :'.format(repo_uoa, len(experiments_this_repo) ) )
            for data_uoa in experiments_this_repo:
                ck.out( '\t' + data_uoa )
            ck.out( '' )

    return {'return':0, 'lst': list_of_experiments, 'repo_to_names_list': repo_to_names_list}


def pick_an_experiment(i):
    """
    Input:  {
                (repo_uoa)          - experiment repository ('*' by default)
                (extra_tags)        - extra tags to filter
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    """

    repo_uoa        = i.get('repo_uoa', '*')
    extra_tags      = i.get('extra_tags')

    list_exp_adict  = { 'action':       'list_experiments',
                        'module_uoa':   'mlperf',
                        'repo_uoa':     repo_uoa,
                        'extra_tags':   extra_tags,
    }
    r=ck.access( list_exp_adict )
    if r['return']>0: return r

    if len(r['lst'])==0:
        return {'return':1, 'error':'No experiments to choose from - please relax your filters'}

    all_experiment_names = [ '{repo_uoa}:{module_uoa}:{data_uoa}'.format(**entry_dict) for entry_dict in r['lst']]

    select_adict = {'action': 'select_string',
                    'module_uoa': 'misc',
                    'options': all_experiment_names,
                    'default': '0',
                    'question': 'Please select one of the experiment entries',
    }
    r=ck.access( select_adict )
    if r['return']>0:
        return r
    else:
        cid = r['selected_value']

    return {'return':0, 'cid': cid}

