from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    
    env = i['env']
    env['+ CFLAGS'] = env.get('+ CFLAGS', [])
    env['+ CXXFLAGS'] = env.get('+ CXXFLAGS', [])
    env['+ FFLAGS'] = env.get('+ FFLAGS', [])
    env['+ LDFLAGS'] = env.get('+ LDFLAGS', [])
    
    if "FAST_COMPILATION" in env:
        DEFAULT_COMPILER_FLAGS = env.get("FAST_COMPILER_FLAGS", "-O3")
        DEFAULT_LINKER_FLAGS = env.get("FAST_LINKER_FLAGS", "-O3 -flto")
    elif "DEBUG_COMPILATION" in env:
        DEFAULT_COMPILER_FLAGS = env.get("DEBUG_COMPILER_FLAGS", "-O0")
        DEFAULT_LINKER_FLAGS = env.get("DEBUG_LINKER_FLAGS", "-O0")
    else:
        DEFAULT_COMPILER_FLAGS = env.get("DEFAULT_COMPILER_FLAGS", "-O2")
        DEFAULT_LINKER_FLAGS = env.get("DEFAULT_LINKER_FLAGS", "-O2")
    
    env['+ CFLAGS'] += DEFAULT_COMPILER_FLAGS.split(" ")
    env['+ CXXFLAGS'] += DEFAULT_COMPILER_FLAGS.split(" ")
    env['+ FFLAGS'] += DEFAULT_COMPILER_FLAGS.split(" ")
    env['+ LDFLAGS'] += DEFAULT_LINKER_FLAGS.split(" ")

    env['+ CFLAGS'] = list(set(env['+ CFLAGS']))
    env['+ CXXFLAGS'] = list(set(env['+ CFLAGS']))
    env['+ FFLAGS'] = list(set(env['+ CFLAGS']))
    env['+ LDFLAGS'] = list(set(env['+ CFLAGS']))

    if env['CM_C_COMPILER_BIN'] == 'icc':
        if env['CM_CPUINFO_Vendor_ID'] == 'GenuineIntel':
            if int(env['CM_CPUINFO_CPU_family']) >= 0:
                env['+ CFLAGS'] += ["-ipo"]
    if env['CM_C_COMPILER_BIN'] == 'gcc':
        if env['CM_HOST_CPU_VENDOR_ID'] == 'AMD':
            if int(env['CM_HOST_CPU_FAMILY']) >= 0:
                env['+ CFLAGS'] += ["-march=znver2", "-flto"]

    return {'return':0}
