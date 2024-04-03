"""
Testing MLPerf loadgen
"""

import numpy as np

print ('')
print ('- Importing MLPerf loadgen library ...')
import mlperf_loadgen as lg
print ('  SUCCESS!')

print ('')
print ('- Importing CM library ...')
import cmind as cm
print ('  SUCCESS!')

print ('')
print ('- List CM repos ...')
print ('')
r = cm.access({'action':'ls', 'automation':'repo', 'out':'con'})
print ('')
print ('  SUCCESS!')
