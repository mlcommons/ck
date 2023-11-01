#ifndef GPU_DEVICE_H_
#define GPU_DEVICE_H_

#include <iostream>

#include "cuda.h"
#include "cuda_runtime.h"

#include "device.h"

#define CHECK_CUDA_SUCCESS(x) if ((x) != cudaSuccess) std::cerr << "encountered CUDA error" << std::endl;

class GPUDevice : public Device {
    size_t NumConcurrency() const override {
        return NumMemory();
    }
    size_t NumMemory() const override {
        int num_devices;
        CHECK_CUDA_SUCCESS(cudaGetDeviceCount(&num_devices));
        return num_devices;
    }
    size_t GetMemoryIndex(size_t concurrency_index) const override {
        return concurrency_index;
    }
    void *Alloc(size_t memory_index, size_t size) override {
        void *data;
        CHECK_CUDA_SUCCESS(cudaSetDevice(memory_index));
        CHECK_CUDA_SUCCESS(cudaMalloc(&data, size));
        return data;
    }
    void Free(size_t memory_index, void *data) override {
        CHECK_CUDA_SUCCESS(cudaSetDevice(memory_index));
        CHECK_CUDA_SUCCESS(cudaFree(data));
    }
    void Read(size_t memory_index, std::vector<uint8_t> &to, const void *from, size_t size) override {
        to.resize(size);
        CHECK_CUDA_SUCCESS(cudaSetDevice(memory_index));
        CHECK_CUDA_SUCCESS(cudaMemcpy(to.data(), from, size, cudaMemcpyDeviceToHost));
    }
    void Write(size_t memory_index, void *to, const std::vector<uint8_t> &from) override {
        CHECK_CUDA_SUCCESS(cudaSetDevice(memory_index));
        CHECK_CUDA_SUCCESS(cudaMemcpy(to, from.data(), from.size(), cudaMemcpyHostToDevice));
    }
    void Copy(size_t memory_index, void *to, const void *from, size_t size) override {
        CHECK_CUDA_SUCCESS(cudaSetDevice(memory_index));
        CHECK_CUDA_SUCCESS(cudaMemcpy(to, from, size, cudaMemcpyDeviceToDevice));
    }
    void SetConcurrencyIndex(size_t concurrency_index) override {
        CHECK_CUDA_SUCCESS(cudaSetDevice(concurrency_index));
    }
};

#endif // GPU_DEVICE_H_
