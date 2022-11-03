from cmind import utils
import os
import json

def preprocess(i):
    env = i['env']
    state = i['state']

    submitter = env.get('CM_MLPERF_SUBMITTER', 'MLCommons')
    hw_name = env.get('CM_HW_NAME', "default")
    backend = env.get('CM_BACKEND', '')
    backend_version = env.get('CM_BACKEND_VERSION', '')
    sut_suffix = ''
    backend_name = ''
    if backend:
        backend_name = env.get('CM_BACKEND_NAME', backend)
        sut_suffix = "-" + backend
        backend_desc = backend_name
        if backend_version:
            sut_suffix += "-" + backend_version
            backend_desc += ' v' + backend_version
    sut = hw_name + sut_suffix
    path = i['run_script_input']['path']
    sut_path = os.path.join(path, "suts", sut + ".json")
    if os.path.exists(sut_path) and env.get('CM_SUT_DESC_CACHE', '') == "yes":
        state['CM_SUT_META'] = json.load(open(sut_path))
    else:
        print("Generating SUT description file for " + sut)
        hw_path = os.path.join(path, "hardware", hw_name + ".json")
        if os.path.exists(hw_path):
            state['CM_HW_META'] = json.load(open(hw_path))
            state['CM_SUT_META'] = state['CM_HW_META']
            state['CM_SUT_META']['framework'] = backend_desc
            os_name = env.get('CM_HOST_OS_FLAVOR', '').capitalize()
            os_version = env.get('CM_HOST_OS_VERSION', '')
            if os_name and os_version:
                os_name_string = os_name + " " + os_version
            os_type = env.get('CM_HOST_OS_TYPE', '')
            kernel = env.get('CM_HOST_OS_KERNEL_VERSION', '')
            if os_type and kernel:
                os_name_string += " (" + os_type + "-" + kernel
                glibc_version = env.get('CM_HOST_OS_GLIBC_VERSION', '')
                if glibc_version:
                    os_name_string += '-glibc' + glibc_version
                os_name_string += ')'
            python_version = env.get('CM_PYTHON_VERSION', '')
            compiler = env.get('CM_COMPILER_FAMILY', '')
            compiler_version = env.get('CM_COMPILER_VERSION', '')
            state['CM_SUT_META']['submitter'] = submitter
            state['CM_SUT_META']['operating_system'] = os_name_string
            state['CM_SUT_META']['other_software_stack'] = "Python: " + python_version + ", " + compiler + "-" + compiler_version
            if 'host_processor_core_count' not in state['CM_SUT_META']:
                state['CM_SUT_META']['host_processor_core_count'] = env.get('CM_HOST_CPU_TOTAL_CORES', '')
            if 'host_processor_model_name' not in state['CM_SUT_META']:
                state['CM_SUT_META']['host_processor_model_name'] = env.get('CM_HOST_CPU_MODEL_NAME', '')
            if 'host_processors_per_node' not in state['CM_SUT_META']:
                state['CM_SUT_META']['host_processors_per_node'] = env.get('CM_HOST_CPU_SOCKETS', '')
            if 'host_processor_caches' not in state['CM_SUT_META']:
                state['CM_SUT_META']['host_processor_caches'] = "L1d cache: " + env.get('CM_HOST_CPU_L1D_CACHE_SIZE', ' ') + \
                        ", L1i cache: " + env.get('CM_HOST_CPU_L1I_CACHE_SIZE', ' ') + ", L2 cache: " + \
                        env.get('CM_HOST_CPU_L2_CACHE_SIZE', ' ') + \
                        ", L3 cache: " + env.get('CM_HOST_CPU_L3_CACHE_SIZE', ' ')
            if 'host_processor_frequency' not in state['CM_SUT_META']:
                state['CM_SUT_META']['host_processor_frequency'] = env.get('CM_HOST_CPU_MAX_MHZ','')
            if 'CM_SUT_SW_NOTES' in env:
                sw_notes = env['CM_SUT_SW_NOTES']
            else:
                sw_notes = ''
            state['CM_SUT_META']['sw_notes'] = sw_notes

            state['CM_SUT_META'] = dict(sorted(state['CM_SUT_META'].items()))

            sut_file = open(sut_path, "w")
            json.dump(state['CM_SUT_META'], sut_file, indent = 4)
            sut_file.close()
        else:
            print("HW description file for " + hw_name + " not found")
            return {'return':1, 'error': "HW description file not found"}

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
