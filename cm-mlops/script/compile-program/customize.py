from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']

    env = i['env']
    CPPFLAGS = env.get('+ CPPFLAGS', [])
    env['CM_C_COMPILER_FLAGS'] = " ".join(env.get('+ CFLAGS', []) + CPPFLAGS)
    env['CM_CXX_COMPILER_FLAGS'] = " ".join(env.get('+ CXXFLAGS', []) + CPPFLAGS)
    env['CM_F_COMPILER_FLAGS'] = " ".join(env.get('+ FFLAGS', []))

    CPATH = env.get('+CPATH', [ ])
    env['CM_C_INCLUDE_PATH'] = " -I".join([" "] + env.get('+C_INCLUDE_PATH', []) + CPATH)
    env['CM_CPLUS_INCLUDE_PATH'] = " -I".join([" "] + env.get('+CPLUS_INCLUDE_PATH', []) + CPATH)
    env['CM_F_INCLUDE_PATH'] = " -I".join([" "] + env.get('+F_INCLUDE_PATH', []) + CPATH)

    # If windows, need to extend it more ...
    if os_info['platform'] == 'windows' and env.get('CM_COMPILER_FAMILY','')!='LLVM':
        print ("WARNING: compile-program script should be extended to support flags for non-LLVM compilers on Windows")
        return {'return':0}

    LDFLAGS = env.get('+ LDFLAGS', [])

    env['CM_C_LINKER_FLAGS'] = " ".join(env.get('+ LDCFLAGS', []) + LDFLAGS)
    env['CM_CXX_LINKER_FLAGS'] = " ".join(env.get('+ LDCXXFLAGS', []) + LDFLAGS)
    env['CM_F_LINKER_FLAGS'] = " ".join(env.get('+ LDFFLAGS', []) + LDFLAGS)

    if env.get('CM_LINKER_LANG', 'C') == "C":
        env['CM_LINKER_BIN'] = env['CM_C_COMPILER_BIN']
        env['CM_LINKER_WITH_PATH'] = env['CM_C_COMPILER_WITH_PATH']
        env['CM_LINKER_COMPILE_FLAGS'] = env['CM_C_COMPILER_FLAGS']
        env['CM_LINKER_FLAGS'] = env['CM_C_LINKER_FLAGS']

    elif env.get('CM_LINKER_LANG', 'C') == "CXX":
        env['CM_LINKER_BIN'] = env['CM_CXX_COMPILER_BIN']
        env['CM_LINKER_WITH_PATH'] = env['CM_CXX_COMPILER_WITH_PATH']
        env['CM_LINKER_COMPILE_FLAGS'] = env['CM_CXX_COMPILER_FLAGS']
        env['CM_LINKER_FLAGS'] = env['CM_CXX_LINKER_FLAGS']

    elif env.get('CM_LINKER_LANG', 'C') == "F":
        env['CM_LINKER_BIN'] = env['CM_F_COMPILER_BIN']
        env['CM_LINKER_WITH_PATH'] = env['CM_F_COMPILER_WITH_PATH']
        env['CM_LINKER_COMPILE_FLAGS'] = env['CM_F_COMPILER_FLAGS']
        env['CM_LINKER_FLAGS'] = env['CM_F_LINKER_FLAGS']

    env['CM_LD_LIBRARY_PATH'] = " -L".join([" " ] + env.get('+LD_LIBRARY_PATH', []))
    env['CM_SOURCE_FOLDER_PATH'] = env['CM_SOURCE_FOLDER_PATH'] if 'CM_SOURCE_FOLDER_PATH' in env else env['CM_TMP_CURRENT_SCRIPT_PATH'] if 'CM_TMP_CURRENT_SCRIPT_PATH' in env else ''

    return {'return':0}

def postprocess(i):

    return {'return':0}
