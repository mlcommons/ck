#
# Copyright (c) 2019 cTuning foundation.
# See CK COPYRIGHT.txt for copyright details.
#
# SPDX-License-Identifier: BSD-3-Clause.
# See CK LICENSE.txt for licensing details.
#
# Collective Knowledge - raw data access (JSON).
#
# Developers:
# - Nikolay Istomin, Xored.
# - Anton Lokhmotov, dividiti.
# - Leo Gordon, dividiti.
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)

import os
import sys
import json
import re
import traceback
from collections import defaultdict
from pprint import pprint

import pandas as pd
import numpy as np

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
# Get raw data for visualization widget.

def get_raw_data(i):
    """
    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """
    prefilter_mode = i.get('prefilter_mode', 'image_classification_singlestream')
    prefilter_config = cfg['prefilter_config'][prefilter_mode]

    def get_experimental_results_from_cache(cache_dir=None, cache_file=None):
        if cache_dir is None:
            # Check this module's directory.
            cache_repo_uoa    = 'ck-mlperf'
            cache_module_uoa  = 'module'
            cache_data_uoa    = 'mlperf.inference'
            r = ck.access({'action':'find',
                'repo_uoa':cache_repo_uoa, 'module_uoa':cache_module_uoa, 'data_uoa':cache_data_uoa})
            if r['return']>0:
                ck.out('Error: %s' % r['error'])
                exit(1)
            cache_dir = r['path']

        if os.path.exists(cache_dir):
            ck.out("Loading the results table(s) from cache at '%s' ..." % cache_dir)
            if cache_file is None:
                # Check all zip files in the cache directory.
                dfs = []
                for cache_file in os.listdir(cache_dir):
                    if cache_file.endswith(".zip"):
                        ck.out("- '%s'" % cache_file)
                        cache_path = os.path.join(cache_dir, cache_file)
                        df = pd.read_pickle(cache_path)
                        df['Cache'] = cache_file
                        df.set_index('Cache', drop=True, append=True, inplace=True)
                        dfs.append(df)
                df = pd.concat(dfs)
            else:
                cache_path = os.path.join(cache_dir, cache_file)
                df = pd.read_pickle(cache_path)
        else:
            ck.out("No cache at '%s' ..." % cache_dir)
            df = pd.DataFrame()
        return df

    def df_as_record(df):
        for index, record in df.to_dict(orient='index').items():
            indices = index if isinstance(index, list) else [ index ]
            record.update({ n:v for n,v in zip(df.index.names, indices) })
            yield record

    def to_value(i):
        if type(i) is str and i.startswith('http'):
            return '<a href="%s">Link</a>' % i

        if type(i) is np.ndarray:
            return i.tolist()

        if isinstance(i, np.int64):
            return int(i)

        if isinstance(i, np.float64):
            return float(i)

        return i

    # Only the official v0.5 results which are cached in this module's directory.
#    df = get_experimental_results_from_cache(cache_file='mlperf-inference-v0.5-results.zip')
#    df = df.set_index('ID', drop=True)
    # All the results in this module's directory.
    df = get_experimental_results_from_cache(cache_file=None)
    
    debug_output = i.get('out')=='con'
    table = []
    for record in df_as_record(df):
        row = {}
        props = [
            'ID',
            'Division',
            'Category',
            'Submitter',
            'System',
            'Task',
            'Benchmark',
            'Scenario',
            'Processor',
            'Processor #',
            'Accelerator',
            'Accelerator #',
#            'Software',
            'FF_M',
            'FF_E',
            'FF_D',
            'FF_S',
            'Details',
            'Code',
            'Notes'
        ]
        for prop in props:
            row[prop] = to_value(record.get(prop, ''))
        row['Software'] = { 'title': 'Software', 'cmd':  record.get('Software', '') }
        row['Invalid?'] = len([ note for note in record.get('Notes', '') if str(note) == 'Result = INVALID' ])

        for score in prefilter_config['score_columns']:
            score_no_scenario = score[0:5] # e.g. A_NMT
            row[score_no_scenario] = np.nan_to_num(record.get(score, 0.0))

        table.append(row)
        if debug_output:
            ck.out(str(row))

    merged_table = table

    return { 'return': 0, 'table': merged_table }


##############################################################################
# Get raw config for visualization widget.

def get_raw_config(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    data_config = cfg['data_config']
    data_config['return'] = 0

    return data_config
