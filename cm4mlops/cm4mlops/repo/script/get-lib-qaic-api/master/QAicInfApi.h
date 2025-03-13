// Copyright (c) 2021 Qualcomm Innovation Center, Inc.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted (subject to the limitations in the
// disclaimer below) provided that the following conditions are met:
//
//    * Redistributions of source code must retain the above copyright
//      notice, this list of conditions and the following disclaimer.
//
//    * Redistributions in binary form must reproduce the above
//      copyright notice, this list of conditions and the following
//      disclaimer in the documentation and/or other materials provided
//      with the distribution.
//
//    * Neither the name Qualcomm Innovation Center nor the names of its
//      contributors may be used to endorse or promote products derived
//      from this software without specific prior written permission.
//
// NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE
// GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT
// HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
// WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
// MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
// IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
// ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
// GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
// IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
// OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
// IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#ifndef QAIC_DEVICE_H_
#define QAIC_DEVICE_H_

#include "QAicApi.h"
#include "QAicApi.pb.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <getopt.h>
#include <vector>
#include <string.h>
#include <cassert>
#include <chrono>
#include <memory>
#include <thread>
#include <array>
#include <random>
#include <future>
#include <bitset>

namespace qaic_api {

extern const uint32_t setSizeDefault;
extern const uint32_t numActivationsDefault;
extern const uint32_t numInferencesDefault;
extern const uint32_t numThreadsPerQueueDefault;
extern const uint32_t qidDefault;

class ActivationSet;

class QAicInfApi {
public:
  QAicInfApi();

  virtual ~QAicInfApi();
  static void logCallback(QLogLevel logLevel, const char *str) {
    std::cout << str;
  }

  static void errorHandler(QAicContextID id, const char *errInfo,
                           QAicErrorType errType, const void *errData,
                           size_t errDataSize, void *userData) {
    std::cout << "Received Error Handler CB: id " << id << "msg: " << errInfo
              << std::endl;
  }

  void setModelBasePath(std::string modelBasePath);
  void setNumActivations(uint32_t num);
  void setNumThreadsPerQueue(uint32_t num);
  void setSetSize(uint32_t num);
  void setLibPath(std::string &aicLibPath);
  void setSkipStage(std::string qaic_skip_stage);

  // Initialize Driver, Run, De-Init, get Results

  QStatus init(QID qid, QAicEventCallback callback);
  QStatus loadDataset();
  QStatus setData();
  QStatus createBuffers(int idx, aicapi::IoDesc& ioDescProto,  std::shared_ptr<qaic_api::ActivationSet>);

  QStatus run(uint32_t activation, uint32_t execobj, void* payload);

  QStatus deinit();
  uint64_t getInfCompletedCount();
  bool isBatchMode();

  void* getBufferPtr(uint32_t act_idx,uint32_t exec_idx, uint32_t buf_idx) {
    return inferenceBuffersList_[act_idx][exec_idx][buf_idx].buf;
  }

  QStatus setBufferPtr(uint32_t act_idx, uint32_t set_idx, uint32_t buf_idx, void* ptr);

private:
  QStatus loadFileType(const std::string &filePath, size_t &sizeLoaded,
                       uint8_t *&dataPtr,
                       std::vector<std::unique_ptr<uint8_t[]>> &vector);
  QAicContext *context_;
  QAicConstants *constants_;
  std::vector<QAicProgram *> programs_;
  // Properties
  QAicContextProperties_t contextProperties_;
  QAicConstantsProperties_t constantsProperties_;
  QAicExecObjProperties_t execObjProperties_;
  QAicQueueProperties queueProperties_;

  std::vector<std::vector<std::vector<QBuffer>>> inferenceBuffersList_;

  // Per Activation Resources
  std::vector<QAicQueue *> queues_;
  std::vector<QAicEvent *> perQueueFinishEvents_;
  std::vector<std::shared_ptr<ActivationSet>> shActivationSets_;
  QBuffer constDescBuf_;
  QBuffer constBuf_;
  QBuffer networkDescBuf_;
  QBuffer progBuf_;
  QID dev_;
  std::vector<std::string> modelBasePaths_;
  std::vector<std::unique_ptr<uint8_t[]>> inferenceBufferVector_;
  uint32_t numActivations_;
  uint32_t numInferences_;
  uint32_t numThreadsPerQueue_;
  uint32_t setSize_;
  bool activated_;
  std::vector<QBuffer> infDataSet;

  // Callback
  QAicEventCallback callback_;
  std::string entryPoint_;
  std::vector<uint8_t> customizedIoDescProtoBuffer_;
}; // QAicInfApi

} // namespace qaic_device

#endif
