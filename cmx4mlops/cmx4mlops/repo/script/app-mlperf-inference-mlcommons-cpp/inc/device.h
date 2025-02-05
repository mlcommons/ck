#ifndef DEVICE_H_
#define DEVICE_H_

#include <cstddef>
#include <thread>
#include <vector>

/**
 * This class represents device and memory that the benchmark is run on.
 *
 * It assumes there are NumMemory() separate memories on the device(s),
 * and NumConcurrency() concurrencies for running the model,
 * each concurrency with access to the memory GetMemoryIndex(concurrency_index).
 *
 * For example, a single CPU can have 1 memory (RAM),
 * any number of concurrencies (may be number of cores), and each concurrency
 * with access to the only memory.
 * 2 GPUs can have 2 memories (one for each GPU), 2 concurrencies (one for each GPU).
 *
 * The Alloc, Free, Read, Write, Copy operations are for the corresponding device memory.
 */
class Device {
public:
    virtual size_t NumConcurrency() const = 0;
    virtual size_t NumMemory() const = 0;
    virtual size_t GetMemoryIndex(size_t concurrency_index) const = 0;
    virtual void *Alloc(size_t memory_index, size_t size) = 0;
    virtual void Free(size_t memory_index, void *data) = 0;
    virtual void Read(size_t memory_index, std::vector<uint8_t> &to, const void *from, size_t size) = 0;
    virtual void Write(size_t memory_index, void *to, const std::vector<uint8_t> &from) = 0;
    virtual void Copy(size_t memory_index, void *to, const void *from, size_t size) = 0;
    // This is specifically for CUDA, which needs to set a device index for each host thread
    virtual void SetConcurrencyIndex(size_t concurrency_index) {}
};

class CPUDevice : public Device {
    size_t NumConcurrency() const override {
        return 2;//std::thread::hardware_concurrency();
    }
    size_t NumMemory() const override {
        return 2;
    }
    size_t GetMemoryIndex(size_t concurrency_index) const override {
        return 0;
    }
    void *Alloc(size_t memory_index, size_t size) override {
        return std::malloc(size);
    }
    void Free(size_t memory_index, void *data) override {
        std::free(data);
    }
    void Read(size_t memory_index, std::vector<uint8_t> &to, const void *from, size_t size) override {
        to.resize(size);
        std::memcpy(to.data(), from, size);
    }
    void Write(size_t memory_index, void *to, const std::vector<uint8_t> &from) override {
        std::memcpy(to, from.data(), from.size());
    }
    void Copy(size_t memory_index, void *to, const void *from, size_t size) override {
        std::memcpy(to, from, size);
    }
};

#endif // DEVICE_H_
