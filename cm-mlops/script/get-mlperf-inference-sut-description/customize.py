from cmind import utils
import os
import json
import shutil

def preprocess(i):
    env = i['env']
    state = i['state']

    submitter = env.get('CM_MLPERF_SUBMITTER', 'cTuning')

    auto_detected_hw_name = False
    if env.get('CM_HW_NAME', '') == '':
        host_name =  env.get('CM_HOST_SYSTEM_NAME', 'default').replace("-", "_")
        env['CM_HW_NAME'] = host_name
        auto_detected_hw_name = True

    hw_name = env['CM_HW_NAME']

    backend = env.get('CM_MLPERF_BACKEND', '')
    backend_version = env.get('CM_MLPERF_BACKEND_VERSION', '')
    sut_suffix = ''
    backend_name = ''
    backend_desc = ''
    if backend:
        backend_name = env.get('CM_MLPERF_BACKEND_NAME', backend)
        sut_suffix = "-" + backend
        backend_desc = backend_name
        if backend_version:
            sut_suffix += "-" + backend_version
            backend_desc += ' v' + backend_version

    sut = hw_name + sut_suffix
    path = i['run_script_input']['path']
    sut_path = os.path.join(path, "suts", sut + ".json")
    if os.path.exists(sut_path) and env.get('CM_SUT_DESC_CACHE', '') == "yes":
        print(f"Reusing SUT description file {sut}")
        state['CM_SUT_META'] = json.load(open(sut_path))
    else:
        if not os.path.exists(os.path.dirname(sut_path)):
            os.makedirs(os.path.dirname(sut_path))

        print("Generating SUT description file for " + sut)
        hw_path = os.path.join(path, "hardware", hw_name + ".json")
        if not os.path.exists(hw_path):
            default_hw_path = os.path.join(path, "hardware", "default.json")
            print("HW description file for " + hw_name + " not found. Copying from default!!!")
            shutil.copy(default_hw_path, hw_path)

        state['CM_HW_META'] = json.load(open(hw_path))
        state['CM_SUT_META'] = state['CM_HW_META']
        state['CM_SUT_META']['framework'] = backend_desc
        os_name = env.get('CM_HOST_OS_FLAVOR', '').capitalize()
        os_version = env.get('CM_HOST_OS_VERSION', '')
        if os_name and os_version:
            os_name_string = os_name + " " + os_version
        else:
            os_name_string = ''
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

        if state['CM_SUT_META'].get('system_name','') == '':
            system_name = env.get('CM_MLPERF_SYSTEM_NAME')
            if not system_name:
                system_name = env.get('CM_HW_NAME')
                if system_name:
                    if auto_detected_hw_name:
                        system_name+=" (auto detected)"
                else:
                    system_name = " (generic)"
            state['CM_SUT_META']['system_name'] = system_name

        # Add GPU info
        if 'cm_cuda_device_prop' in state:
            state['CM_SUT_META']['accelerator_frequency'] = state['cm_cuda_device_prop']['Max clock rate']
            state['CM_SUT_META']['accelerator_memory_capacity'] = str(int(state['cm_cuda_device_prop']['Global memory'])/(1024*1024.0*1024)) + " GB"
            state['CM_SUT_META']['accelerator_model_name'] = state['cm_cuda_device_prop']['GPU Name']
            state['CM_SUT_META']['accelerators_per_node'] = "1"

        if state['CM_SUT_META'].get('host_processor_core_count', '') == '':
            physical_cores_per_node = env.get('CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET')
            state['CM_SUT_META']['host_processor_core_count'] = physical_cores_per_node

        if state['CM_SUT_META'].get('host_processor_model_name', '') == '':
            state['CM_SUT_META']['host_processor_model_name'] = env.get('CM_HOST_CPU_MODEL_NAME', 'undefined')
        if state['CM_SUT_META'].get('host_processors_per_node', '') == '':
            state['CM_SUT_META']['host_processors_per_node'] = env.get('CM_HOST_CPU_SOCKETS', '')

        if state['CM_SUT_META'].get('host_processor_caches', '') == '':
            state['CM_SUT_META']['host_processor_caches'] = "L1d cache: " + env.get('CM_HOST_CPU_L1D_CACHE_SIZE', ' ') + \
                    ", L1i cache: " + env.get('CM_HOST_CPU_L1I_CACHE_SIZE', ' ') + ", L2 cache: " + \
                    env.get('CM_HOST_CPU_L2_CACHE_SIZE', ' ') + \
                    ", L3 cache: " + env.get('CM_HOST_CPU_L3_CACHE_SIZE', ' ')

        if state['CM_SUT_META'].get('host_processor_frequency', '') == '':
            state['CM_SUT_META']['host_processor_frequency'] = env.get('CM_HOST_CPU_MAX_MHZ') if env.get('CM_HOST_CPU_MAX_MHZ', '') != '' else 'undefined'
        if state['CM_SUT_META'].get('host_memory_capacity', '') == '':
            state['CM_SUT_META']['host_memory_capacity'] = env.get('CM_HOST_MEMORY_CAPACITY') if env.get('CM_HOST_MEMORY_CAPACITY', '') != '' else 'undefined'
        if state['CM_SUT_META'].get('host_storage_capacity', '') == '':
            state['CM_SUT_META']['host_storage_capacity'] = env.get('CM_HOST_DISK_CAPACITY') if env.get('CM_HOST_DISK_CAPACITY', '') != '' else 'undefined'
        if 'CM_SUT_SW_NOTES' in env:
            sw_notes = env['CM_SUT_SW_NOTES']
        else:
            sw_notes = ''
        state['CM_SUT_META']['sw_notes'] = sw_notes

        state['CM_SUT_META'] = dict(sorted(state['CM_SUT_META'].items()))

        sut_file = open(sut_path, "w")
        json.dump(state['CM_SUT_META'], sut_file, indent = 4)
        sut_file.close()

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
