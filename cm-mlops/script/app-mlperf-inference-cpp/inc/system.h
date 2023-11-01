#ifndef SYSTEM_H_
#define SYSTEM_H_

#include <deque>
#include <memory>
#include <mutex>
#include <thread>
#include <vector>
#include <condition_variable>

#include "system_under_test.h"

#include "backend.h"

/**
 * A System class represents the policy by which requests from LoadGen are handled.
 *
 * StreamSUT immediately takes any LoadGen requests to device concurrency 0
 * (this is for single-stream).
 *
 * QueueSUT maintains a queue of LoadGen requests and dequeues requests to
 * any available device concurrency.
 */
class System : public mlperf::SystemUnderTest {
public:
    System(const std::string &name, std::shared_ptr<Backend> &backend)
        : name(name), backend(backend) {}
    const std::string &Name() override { return name; }

protected:
    std::shared_ptr<Backend> backend;

private:
    std::string name;
};

class StreamSUT : public System {
public:
    StreamSUT(std::shared_ptr<Backend> &backend) : System("StreamSUT", backend) {}
    
    void IssueQuery(const std::vector<mlperf::QuerySample> &samples) override {
        size_t max_batch_size = backend->MaxBatchSize();
        size_t size = samples.size();

        // for CUDA, set the device to use for this thread
        backend->SetDeviceConcurrencyIndex(0);

        for (auto batch_begin = samples.begin(); batch_begin < samples.end(); batch_begin += max_batch_size) {
            auto batch_end = std::min(batch_begin + max_batch_size, samples.end());
            const std::vector<mlperf::QuerySample> batch_queries(batch_begin, batch_end);
            backend->IssueBatch(0, batch_queries);
        }
    }

    void FlushQueries() override {}
};

class QueueSUT : public System {
public:
    QueueSUT(std::shared_ptr<Backend> &backend)
            : System("QueueSUT", backend) {
        // launch threads
        size_t num_threads = backend->NumConcurrency();
        for (size_t i = 0; i < num_threads; i++)
            threads.emplace_back(&QueueSUT::ThreadStart, this, i);
    }

    ~QueueSUT() override {
        {
            std::lock_guard<std::mutex> lock(queries_mutex);
            done = true;
        }
        has_queries.notify_all();

        for (std::thread &thread : threads)
            thread.join();
    }

    void IssueQuery(const std::vector<mlperf::QuerySample> &samples) override {
        // enqueue queries
        {
            std::lock_guard<std::mutex> lock(queries_mutex);
            queries.insert(queries.end(), samples.begin(), samples.end());
        }
        has_queries.notify_one();
    }

    void FlushQueries() override {}

private:
    void ThreadStart(size_t concurrency_index) {
        size_t max_batch_size = backend->MaxBatchSize();
        std::vector<mlperf::QuerySample> batch_queries;
        batch_queries.reserve(max_batch_size);
        size_t size;

        // for CUDA, set the device to use for this thread
        backend->SetDeviceConcurrencyIndex(concurrency_index);

        while (true) {
            // dequeue queries
            {
                std::unique_lock<std::mutex> lock(queries_mutex);
                has_queries.wait(lock, [&]() { return !queries.empty() || done; });

                if (done)
                    break;

                // load a batch of queries to batch_queries
                size = std::min(max_batch_size, queries.size());
                auto begin = queries.begin();
                auto end = begin + size;
                batch_queries.assign(begin, end);
                queries.erase(begin, end);
            }
            has_queries.notify_one();

            // compute response from batch_queries
            // and log to LoadGen
            backend->IssueBatch(concurrency_index, batch_queries);
        }
    }

    // queue of incoming queries
    std::deque<mlperf::QuerySample> queries;
    std::mutex queries_mutex;
    std::condition_variable has_queries;

    // worker threads to process queries
    std::vector<std::thread> threads;

    bool done{false};
};

#endif // SYSTEM_H_
