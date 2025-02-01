from hip import hip

# Defining the value for hipDeviceGetAttribute
STRINGLENGTH = 256
hipDeviceAttributeClockRate = 5
hipDeviceAttributeMaxBlockDimX = 26
hipDeviceAttributeMaxBlockDimY = 27
hipDeviceAttributeMaxBlockDimZ = 28
hipDeviceAttributeMaxGridDimX = 29
hipDeviceAttributeMaxGridDimY = 30
hipDeviceAttributeMaxGridDimZ = 31
hipDeviceAttributeMaxThreadsPerBlock = 56
hipDeviceAttributeMaxThreadsPerMultiProcessor = 57
hipDeviceAttributeMaxRegistersPerBlock = 71
hipDeviceAttributeMaxSharedMemoryPerBlock = 74
hipDeviceAttributeWarpSize = 87


def get_gpu_info():
    num_gpus = hip.hipGetDeviceCount()[1]
    all_gpu_info = []

    for i in range(num_gpus):
        gpu_info = {
            "GPU Device ID": hip.hipDeviceGetPCIBusId(STRINGLENGTH, i)[1],
            "GPU Name": i,
            "GPU compute capability": f"{hip.hipDeviceComputeCapability(i)[1]}.{hip.hipDeviceComputeCapability(i)[2]}",
            "ROCM driver version": f"{hip.hipDriverGetVersion()[1]}",
            "ROCM runtime version": hip.hipRuntimeGetVersion()[1],
            "Global memory (GiB)": hip.hipDeviceTotalMem(i)[1] / 1_073_741_824,
            "Max clock rate": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeClockRate), i)[1] / 1000} MHz",
            "Total amount of shared memory per block (Bytes)": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxSharedMemoryPerBlock), i)[1]}",
            "Total number of registers available per block (Bytes)": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxRegistersPerBlock), i)[1]}",
            "Warp size": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeWarpSize), i)[1]}",
            "Maximum number of threads per multiprocessor": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxThreadsPerMultiProcessor), i)[1]}",
            "Maximum number of threads per block": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxThreadsPerBlock), i)[1]}",
            "Max dimension size of a thread block X": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxBlockDimX), i)[1]}",
            "Max dimension size of a thread block Y": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxBlockDimY), i)[1]}",
            "Max dimension size of a thread block Z": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxBlockDimZ), i)[1]}",
            "Max dimension size of a grid size X": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxGridDimX), i)[1]}",
            "Max dimension size of a grid size Y": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxGridDimY), i)[1]}",
            "Max dimension size of a grid size Z": f"{hip.hipDeviceGetAttribute(hip.hipDeviceAttribute_t(hipDeviceAttributeMaxGridDimZ), i)[1]}",
        }
        all_gpu_info.append(gpu_info)

    return all_gpu_info


if __name__ == "__main__":
    gpu_info_list = get_gpu_info()
    with open("tmp-run.out", "w") as f:
        for idx, gpu_info in enumerate(gpu_info_list):
            print(f"GPU {idx}:")
            for key, value in gpu_info.items():
                f.write(f"{key}: {value}\n")
