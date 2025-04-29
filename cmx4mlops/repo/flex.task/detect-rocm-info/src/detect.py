# Reused from legacy CM4MLOps

import pycuda.driver as cuda
import pycuda.autoinit

def get_gpu_info():
    num_gpus = cuda.Device.count()
    all_gpu_info = []

    for i in range(num_gpus):
        device = cuda.Device(i)
        cuda_runtime_version = cuda.get_version()
        cuda_runtime_version_str = f"{cuda_runtime_version[0]}.{cuda_runtime_version[1]}"

        gpu_info = {
            "GPU Device ID": device.pci_bus_id(),
            "GPU Name": device.name(),
            "GPU compute capability": f"{device.compute_capability()[0]}.{device.compute_capability()[1]}",
            "CUDA driver version": f"{cuda.get_driver_version() // 1000}.{(cuda.get_driver_version() % 1000) // 10}",
            "CUDA runtime version": cuda_runtime_version_str,
            "Global memory": device.total_memory(),
            "Max clock rate": f"{device.get_attribute(cuda.device_attribute.CLOCK_RATE)} MHz",
            "Total amount of shared memory per block": device.get_attribute(cuda.device_attribute.MAX_SHARED_MEMORY_PER_BLOCK),
            "Total number of registers available per block": device.get_attribute(cuda.device_attribute.MAX_REGISTERS_PER_BLOCK),
            "Warp size": device.get_attribute(cuda.device_attribute.WARP_SIZE),
            "Maximum number of threads per multiprocessor": device.get_attribute(cuda.device_attribute.MAX_THREADS_PER_MULTIPROCESSOR),
            "Maximum number of threads per block": device.get_attribute(cuda.device_attribute.MAX_THREADS_PER_BLOCK),
            "Max dimension size of a thread block X": device.get_attribute(cuda.device_attribute.MAX_BLOCK_DIM_X),
            "Max dimension size of a thread block Y": device.get_attribute(cuda.device_attribute.MAX_BLOCK_DIM_Y),
            "Max dimension size of a thread block Z": device.get_attribute(cuda.device_attribute.MAX_BLOCK_DIM_Z),
            "Max dimension size of a grid size X": device.get_attribute(cuda.device_attribute.MAX_GRID_DIM_X),
            "Max dimension size of a grid size Y": device.get_attribute(cuda.device_attribute.MAX_GRID_DIM_Y),
            "Max dimension size of a grid size Z": device.get_attribute(cuda.device_attribute.MAX_GRID_DIM_Z),
        }

        all_gpu_info.append(gpu_info)

    return all_gpu_info

if __name__ == "__main__":
    gpu_info_list = get_gpu_info()

    import json
    with open ("tmp-flex-task-output.json", "w") as f:
        json.dump({'gpu_info':gpu_info_list}, f, indent=2, sort_keys=True)

    print (json.dumps(gpu_info_list, indent=2, sort_keys=True))
