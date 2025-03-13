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


#include "QAicInfApi.h"

#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <dlfcn.h>
#include <dirent.h>
#include <iostream>
#include <fstream>
#include <google/protobuf/util/json_util.h>
namespace qaic_api {

const uint32_t setSizeDefault = 10;
const uint32_t numActivationsDefault = 1;
const uint32_t numInferencesDefault = 40;
const uint32_t numThreadsPerQueueDefault = 4;
const uint32_t qidDefault = 0;


class ActivationSet {

 public:
  ActivationSet(
      QData ioDescQData,
      QAicContext* context,
      QAicProgram* program, QAicQueue* queue, QID dev, uint32_t numBuffers,
      QAicExecObjProperties_t& execObjProperties_t,
      uint32_t activationId,
      QAicEventCallback callback = nullptr);
  virtual ~ActivationSet();

  // protected:
  // Program is expected to be activated before calling init
  QStatus init(uint32_t setSize = setSizeDefault);
  QBuffer* getDmaBuffers(uint32_t execOjbIndex);
  QStatus reset();
  QStatus setData(std::vector<std::vector<QBuffer>>& buffers);
  QStatus setDataSingle(int set_idx, std::vector<QBuffer>& buffers);
  QStatus run(uint32_t numInferences, void* payload);
  QStatus deinit();
  void setOutBufIndex(uint32_t outBufIndex) { outBufIndex_ = outBufIndex;}
  std::string filename;
  uint32_t getNumBuffers() { return numBuffers_; }
private:
  std::vector<QAicEvent *> eventExecSet_;
  std::vector<QAicExecObj *> execObjSet_;
  std::vector<QBuffer *> qbuffersSet_;
  uint32_t setSize_;
  QAicEvent *activationEvent_;
  QAicContext *context_;
  QAicProgram *program_;
  QAicQueue *queue_;
  QID dev_;
  uint32_t numBuffers_;
  QBuffer *userBuffers_;
  QAicExecObjProperties_t execObjProperties_;
  uint32_t activationId_;
  QAicEventCallback callback_;
  QData ioDescQData_;
  uint32_t outBufIndex_;
};

//--------------------------------------------------------------------
// ActivationSet class Implementation
//--------------------------------------------------------------------

ActivationSet::ActivationSet(
    QData ioDescQData,
    QAicContext *context,
    QAicProgram *program, QAicQueue *queue, QID dev, uint32_t numBuffers,
    QAicExecObjProperties_t &execObjProperties,
    uint32_t activationId,
    QAicEventCallback callback)
    : context_(context), program_(program), queue_(queue),
      dev_(dev), numBuffers_(numBuffers), userBuffers_(nullptr),
      execObjProperties_(execObjProperties),
      activationId_(activationId), callback_(callback), ioDescQData_(ioDescQData) {}

ActivationSet::~ActivationSet() {}

QStatus ActivationSet::deinit() {
  QStatus status = QS_SUCCESS;

  for (auto &e : execObjSet_) {

    status = qaicReleaseExecObj(e);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to release Exec obj" << std::endl;
      return status;
    }
  }
  for (auto &ev : eventExecSet_) {
    status = qaicReleaseEvent(ev);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to release Event obj" << std::endl;
      return status;
    }
  }
  return status;
}

QBuffer* ActivationSet::getDmaBuffers(uint32_t execObjIndex) {
  return qbuffersSet_[execObjIndex];
}

QStatus ActivationSet::init(uint32_t setSize) {
  QStatus status = QS_SUCCESS;

  setSize_ = setSize;

  qbuffersSet_.resize(setSize_);

  if (!strcmp(std::getenv("QAIC_BYPASS_PPP"),"enable")) {
     // std::cout << "Zero Copy enabled\n";
    execObjProperties_ |= QAIC_EXECOBJ_PROPERTIES_ZERO_COPY_BUFFERS;
  }

  for (uint32_t i = 0; i < setSize_; i++) {
    QAicExecObj *execObj = nullptr;
    qbuffersSet_[i] = nullptr;
    // nullptr is passed as the ioDesc indicating we will use the default
    // ioDescriptor.
    status = qaicCreateExecObj(
        context_, &execObj, &execObjProperties_, program_,
        (ioDescQData_.data)?(&ioDescQData_):nullptr,
        nullptr, nullptr);
    if ((status != QS_SUCCESS) || (execObj == nullptr)) {
      std::cerr << "Failed to create Exec obj" << std::endl;
      return status;
    }
    execObjSet_.push_back(execObj);
    if (!strcmp(std::getenv("QAIC_BYPASS_PPP"),"enable")) {
      const QAicApiFunctionTable *aicApi_ = qaicGetFunctionTable(); 
      status = aicApi_ -> qaicExecObjGetIoBuffers( execObj, &numBuffers_, &qbuffersSet_[i]);
      if ((status != QS_SUCCESS)) {
        std::cerr << "Failed to get IO buffers" << std::endl;
        return status;
      }
    }

    QAicEvent *event = nullptr;
    status = qaicCreateEvent(context_, &event,
                                      QAIC_EVENT_DEVICE_COMPLETE);
    if ((status != QS_SUCCESS) || (event == nullptr)) {
      std::cerr << "Failed to create Event" << std::endl;
      return status;
    }
    eventExecSet_.push_back(event);
  }
  return QS_SUCCESS;
}

QStatus ActivationSet::setData(std::vector<std::vector<QBuffer>> &buffers) {
  QStatus status = QS_SUCCESS;
  int i = 0;
  if (!strcmp(std::getenv("QAIC_BYPASS_PPP"),"enable")) {
    // no setdata is required when using dma buf path

    std::cerr << "no setdata is required when using dma buf path" << std::endl;
    return status;
  }
  for (auto &e : execObjSet_) {
    status = qaicExecObjSetData(e, buffers[i].size(),  buffers[i].data());
    if (status != QS_SUCCESS) {
      return status;
    }
    ++i;
  }
  //userBuffers_ = userBuffers;
  return status;
}

QStatus ActivationSet::setDataSingle(int set_idx, std::vector<QBuffer> &buffers) {
  QStatus status = QS_SUCCESS;

  status = qaicExecObjSetData(execObjSet_[set_idx], buffers.size(),  buffers.data());
  if (status != QS_SUCCESS) {
    std::cout << "tried to set " << set_idx << " " << buffers.data() << " " << buffers.size() << std::endl;
    return status;
  }

  return status;
}


QStatus ActivationSet::run(uint32_t index, void* payload) {
  QStatus status;

  //std::cout << "clearing event for " << index << " " << payload << std::endl;
  status = qaicEventClear(eventExecSet_.at(index));
  if (status != QS_SUCCESS) {
    return status;
  }

  qaicEventRemoveCallback(eventExecSet_.at(index), callback_);

  status = qaicEventAddCallback(eventExecSet_.at(index), callback_, payload);
  if (status != QS_SUCCESS) {
    return status;
  }

  //std::cout << "Enqueuing work " << index << " " << payload << std::endl;
  status = qaicEnqueueExecObj(queue_, execObjSet_.at(index),
                                       eventExecSet_.at(index));
  if (status != QS_SUCCESS) {
    return status;
  }

  //std::cout << "Creating callback " << index << " " << payload << std::endl;
  return QS_SUCCESS;
}



//------------------------------------------------------------------
// QAIC Runner Example Class Implementation
//------------------------------------------------------------------
QAicInfApi::QAicInfApi()
    :
      context_(nullptr),
      constants_(nullptr), contextProperties_(QAIC_CONTEXT_DEFAULT),
      execObjProperties_(QAIC_EXECOBJ_PROPERTIES_DEFAULT),
      queueProperties_{QAIC_QUEUE_PROPERTIES_ENABLE_MULTI_THREADED_QUEUES,
                       numThreadsPerQueueDefault},
      dev_(0),
      numActivations_(numActivationsDefault),
      numInferences_(numInferencesDefault),
      numThreadsPerQueue_(numThreadsPerQueueDefault), setSize_(setSizeDefault),
      activated_(false), entryPoint_("default") {
}

QAicInfApi::~QAicInfApi() {
  QStatus status;

  for (uint32_t i = 0; i < programs_.size(); i++) {
    status = qaicReleaseProgram(programs_[i]);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to release program" << std::endl;
    }
  }

  for (uint32_t i = 0; i < queues_.size(); i++) {
    status = qaicReleaseQueue(queues_[i]);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to release queue" << std::endl;
    }
    queues_[i] = nullptr;
  }

  if (constants_ != nullptr) {
    status = qaicReleaseConstants(constants_);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to release constants" << std::endl;
    }
  }

  shActivationSets_.clear();

  if (context_ != nullptr) {
    status = qaicReleaseContext(context_);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to release context" << std::endl;
    }
    context_ = nullptr;
  }

  inferenceBufferVector_.clear();
}

void QAicInfApi::setSkipStage(std::string qaic_skip_stage) {
 if (!qaic_skip_stage.empty()) {
  entryPoint_ = qaic_skip_stage;
 }
}

QStatus QAicInfApi::loadFileType(
    const std::string &filePath, size_t &sizeLoaded, uint8_t *&dataPtr,
    std::vector<std::unique_ptr<uint8_t[]>> &vector) {
  uint64_t fileSize;
  std::ifstream infile;
  infile.open(filePath, std::ios::binary | std::ios::in);
  if (!infile.is_open()) {
    std::cerr << "Failed to open file: " << filePath << std::endl;
    return QS_ERROR;
  }

  infile.seekg(0, infile.end);
  fileSize = infile.tellg();
  infile.seekg(0, infile.beg);
  std::unique_ptr<uint8_t[]> uniqueBuffer =
      std::unique_ptr<uint8_t[]>(new (std::nothrow) uint8_t[fileSize]);
  if (uniqueBuffer == nullptr) {
    std::cerr << "Failed to allocate buffer for file " << filePath
              << " of size " << fileSize << std::endl;
    return QS_ERROR;
  }
  infile.read((char *)uniqueBuffer.get(), fileSize);
  if (!infile) {
    std::cerr << "Failed to read all data from file " << filePath << std::endl;
    return QS_ERROR;
  }
  dataPtr = uniqueBuffer.get();
  vector.emplace_back(std::move(uniqueBuffer));
  sizeLoaded = fileSize;
  return QS_SUCCESS;
}


QStatus QAicInfApi::init(QID qid, QAicEventCallback callback) {
  QStatus status = QS_SUCCESS;

  callback_ = callback;
  //std::cout << "callback - " << (void*)callback_ << std::endl;

  dev_ = qid;

  // validate if device is available
  QDevInfo devInfo;
  status = qaicGetDeviceInfo(dev_, &devInfo);
  if (status == QS_SUCCESS) {
    if (devInfo.devStatus != QDS_READY) {
      std::cerr << "Device:" << dev_ << " not in ready state" << std::endl;
      exit(1);
    }
  } else {
    std::cerr << "Invalid device:" << std::to_string(dev_) << std::endl;
    exit(1);
  }

  // Check Library Compatibility
  {
    uint16_t major;
    uint16_t minor;
    const char *patch;
    const char *variant;
    status = qaicGetAicVersion(&major, &minor, &patch, &variant);

    if (status != QS_SUCCESS) {
      std::cerr << "Unable to retrieve AicVersion" << std::endl;
      exit(1);
    }
    if ((major != LRT_LIB_MAJOR_VERSION) || (minor < LRT_LIB_MINOR_VERSION)) {
      std::cerr << "AicApi Header is not compatible with Library, lib:" << major
                << "." << minor << " header:" << LRT_LIB_MAJOR_VERSION << "."
                << LRT_LIB_MINOR_VERSION << std::endl;
      exit(1);
    }
  }

  status = qaicCreateContext(&context_, &contextProperties_, 1, &dev_,
                                      logCallback, errorHandler, nullptr);
  if ((context_ == nullptr) || (status != QS_SUCCESS)) {
    std::cerr << "Failed to Create Context" << std::endl;
    return status;
  }

  for (uint32_t i = 0; i < modelBasePaths_.size() ; i++) {

    QBuffer programQpcBuf_;
    QAicProgramProperties_t programProperties_;
    std::vector<std::unique_ptr<uint8_t[]>> programBufferVector_;
    QAicQpcObj *qpcObj_;

    std::string filePath = modelBasePaths_[i] + "/programqpc.bin";


    // Load file
    status = loadFileType(filePath, programQpcBuf_.size, programQpcBuf_.buf,
                          programBufferVector_);


    //-------------------------------------------------------------------------
    // Create Programs
    // It is valid to pass a null for constants, if null program will
    // disregard constants
    //-------------------------------------------------------------------------
    // Initialize the program properties with default.
    status = qaicProgramPropertiesInitDefault(&programProperties_);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to initialize program properties." << std::endl;
      return status;
    }

    status = qaicOpenQpc(&qpcObj_, programQpcBuf_.buf, programQpcBuf_.size, false);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to open Qpc." << std::endl;
      return status;
    }

    const char *name = "progName";
    QAicProgram *program = nullptr;

    status = qaicCreateProgram(
        context_, &program, &programProperties_, dev_, name, qpcObj_);

    if ((program == nullptr) || (status != QS_SUCCESS)) {
      std::cerr << "Failed to create program" << std::endl;
      return status;
    }
    programs_.push_back(program);
  }


  //-------------------------------------------------------------------------
  // Load Programs  QAicInfApi(uint32_t dummy);

  // User may choose to explicitly load program, or let the driver load
  // the program when it is needed.
  // For this reason the following code is commented out, to demonstrate
  // automatic loading and activation
  //-------------------------------------------------------------------------
  for (uint32_t i = 0; i < modelBasePaths_.size(); i++) {
    QStatus status;
    status = qaicLoadProgram(programs_[i]);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to load program" << std::endl;
      return status;
    }
  }
  //-------------------------------------------------------------------------
  // Activate Programs
  // User may choose to explicitly activate program, or let the driver
  // activate the program when it is needed.
  // For this reason the following code is commented out, to demonstrate
  // automatic loading and activation
  //-------------------------------------------------------------------------
  for (uint32_t i = 0; i < modelBasePaths_.size(); i++) {
    QStatus status;
    status = qaicRunActivationCmd(programs_[i],
                                           QAIC_PROGRAM_CMD_ACTIVATE_FULL);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to enqueue Activation command" << std::endl;
      return status;
    }
  }

  //-------------------------------------------------------------------------
  // Create Queues for Execution
  //-------------------------------------------------------------------------
  for (uint32_t i = 0; i < modelBasePaths_.size(); i++) {

    QAicQueue *queue = nullptr;
    status =
        qaicCreateQueue(context_, &queue, &queueProperties_, dev_);
    if ((queue == nullptr) || (status != QS_SUCCESS)) {
      std::cerr << "Failed to create queue" << std::endl;
      return status;
    }
    queues_.push_back(queue);
  }

  for (uint32_t i = 0; i < modelBasePaths_.size(); i++) {

    QData ioDescQData;
    ioDescQData.data = nullptr;
    ioDescQData.size = 0;
    aicapi::IoDesc ioDescProto;
    status = qaicProgramGetIoDescriptor(programs_[i], &ioDescQData);
    if (ioDescQData.data == nullptr) {
      std::cerr << "Failed to get iodesc" << std::endl;
      return QS_ERROR;
    }
    ioDescProto.ParseFromArray(ioDescQData.data, ioDescQData.size);
    if (!entryPoint_.empty() && entryPoint_.compare("default") != 0)  {
      for (auto &io_set : ioDescProto.io_sets()) {
        if (io_set.name().compare(entryPoint_) == 0) {
          ioDescProto.clear_selected_set();
          ioDescProto.mutable_selected_set()->CopyFrom(io_set);
          break;
        }
      }
      if(ioDescProto.selected_set().name().compare(entryPoint_) != 0) {
        std::cerr << "Failed to match name in iodesc" << std::endl;
        return QS_ERROR;
      }

      try {
        customizedIoDescProtoBuffer_.resize(ioDescProto.ByteSizeLong());
      } catch (const std::bad_alloc &e) {
        std::cerr << "vector resize failed for protocol Buffer -"<< e.what()<<std::endl;
        return QS_ERROR;
      }
      if (!ioDescProto.SerializeToArray(customizedIoDescProtoBuffer_.data(),
                                     customizedIoDescProtoBuffer_.size())) {
        std::cerr << "Failed to serialize modified protocol bufffer"<<std::endl;
        return QS_ERROR;
      }
      ioDescQData.data = customizedIoDescProtoBuffer_.data();
      ioDescQData.size = customizedIoDescProtoBuffer_.size();
    } else {
      customizedIoDescProtoBuffer_.clear();
      ioDescQData.data = nullptr;
      ioDescQData.size = 0;
    }
    #if 0
    {
      google::protobuf::util::JsonPrintOptions jsonPrintOption;
      jsonPrintOption.add_whitespace = true;
      jsonPrintOption.always_print_primitive_fields = true;
      jsonPrintOption.always_print_enums_as_ints = false;
      jsonPrintOption.preserve_proto_field_names = true;

      std::string jsonPrint;
      google::protobuf::util::MessageToJsonString(ioDescProto, &jsonPrint,
                                                  jsonPrintOption);
      std::cout << "Network Descriptor:\n{" << jsonPrint << std::endl;
      jsonPrint.clear();
    }
    #endif
    uint32_t numBuffers = ioDescProto.selected_set().bindings().size();
    if (!strcmp(std::getenv("QAIC_BYPASS_PPP"),"enable")) {
      numBuffers = ioDescProto.dma_buf_size();
      ioDescQData.data = nullptr;
    }
    std::shared_ptr<ActivationSet> shActivation =
        std::make_shared<ActivationSet>(ioDescQData,
            context_, programs_[i], queues_[i], dev_,
                                        numBuffers,
            execObjProperties_, i, callback_);
    if (shActivation != nullptr) {
      shActivation->init(setSize_);
      shActivationSets_.emplace_back(shActivation);
    }

    // Create IO buffers
    status = createBuffers(i, ioDescProto, shActivation);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to create IO buffers." << std::endl;
      return status;
    }
  }

  if (!(!strcmp(std::getenv("QAIC_BYPASS_PPP"),"enable"))) {
    setData();
  }

  return QS_SUCCESS;
}

QStatus QAicInfApi::createBuffers(int idx, aicapi::IoDesc& ioDescProto, std::shared_ptr<ActivationSet> shActivation) {

  inferenceBuffersList_.resize(inferenceBuffersList_.size() + 1);

  inferenceBuffersList_[idx].resize(setSize_);
  if (!strcmp(std::getenv("QAIC_BYPASS_PPP"),"enable")) {
    for (uint32_t y = 0; y < setSize_; y++) {
      
      QBuffer* dmaBuffVect = shActivation->getDmaBuffers(y);

      for (uint32_t i = 0; i < shActivation->getNumBuffers(); i++) {
        inferenceBuffersList_[idx][y].push_back(dmaBuffVect[i]);
      }
    }
    return QS_SUCCESS;
  }

  for (uint32_t y = 0; y < setSize_; y++) {

    for (uint32_t i = 0; i < ioDescProto.selected_set().bindings().size(); i++) {
      if (ioDescProto.selected_set().bindings(i).dir() == aicapi::BUFFER_IO_TYPE_OUTPUT) {
        QBuffer buf;
        uint32_t outputBufferSize = ioDescProto.selected_set().bindings(i).size();
        std::unique_ptr<uint8_t[]> uniqueBuffer = std::unique_ptr<uint8_t[]>(
            // over allocate to allow for buffer alignment
            new(std::nothrow) uint8_t[outputBufferSize + 32]);
        if (uniqueBuffer == nullptr) {
          std::cerr << "Failed to allocate buffer for output, size "
              << outputBufferSize << std::endl;
          return QS_ERROR;
        }
        buf.buf = uniqueBuffer.get();

        //align the buffer to 32 byte boundary
        uint64_t mask = 31;
        mask = ~mask;
        buf.buf = (uint8_t*)((uint64_t)(buf.buf + 32) & mask);

        buf.size = outputBufferSize;
        inferenceBufferVector_.push_back(std::move(uniqueBuffer));
        inferenceBuffersList_[idx][y].push_back(std::move(buf));
      } else if (ioDescProto.selected_set().bindings(i).dir() == aicapi::BUFFER_IO_TYPE_INPUT) {
        QBuffer buf = QBuffer();
        uint32_t inputBufferSize = ioDescProto.selected_set().bindings(i).size();

        std::unique_ptr<uint8_t[]> uniqueBuffer = std::unique_ptr<uint8_t[]>(
            // over allocate to allow for buffer alignment
            new(std::nothrow) uint8_t[inputBufferSize + 32]);
        if (uniqueBuffer == nullptr) {
          std::cerr << "Failed to allocate input buffer" << std::endl;
          return QS_ERROR;
        }
        buf.buf = uniqueBuffer.get();

        //align the buffer to 32 byte boundary
        uint64_t mask = 31;
        mask = ~mask;
        buf.buf = (uint8_t*)((uint64_t)(buf.buf + 32) & mask);

        buf.size = inputBufferSize;
        inferenceBufferVector_.push_back(std::move(uniqueBuffer));
        inferenceBuffersList_[idx][y].push_back(std::move(buf));
      }
    }
  }

  return QS_SUCCESS;
}

QStatus QAicInfApi::setData() {

  //--------------------------------------
  // Set data in buffers
  //--------------------------------------
  int x = 0;
  for (auto &a : shActivationSets_) {
    if (a != nullptr) {
      a->setData(inferenceBuffersList_[x]);
    }
    ++x;
  }

  return QS_SUCCESS;
}


//----------------------------------------------------------------
// Run Inferences
//----------------------------------------------------------------
QStatus QAicInfApi::run(uint32_t activation,
                        uint32_t execobj,
                        void* payload) {
  QStatus status = QS_SUCCESS;
  //setData();

  shActivationSets_[activation]->run(execobj, payload);

  return status;
}
/*QStatus qaicExecObjGetIoBuffers(const QAicExecObj *execObj,
                                uint32_t *numBuffers, QBuffer **buffers) {
  if ((execObj == nullptr) || (execObj->shExecObj == nullptr) ||
      (numBuffers == nullptr) || (buffers == nullptr)) {
  //  LogErrorG("Invalid null pointer");
    return QS_INVAL;
  }
  return execObj->shExecObj->getIoBuffers(*numBuffers, *buffers);
}*/

QStatus QAicInfApi::deinit() {
  QStatus status;

  for (auto &a : shActivationSets_) {
    if (a != nullptr) {
      status = a->deinit();
      if (status != QS_SUCCESS) {
        return status;
      }
    }
  }

  if (activated_ == false) {
    return QS_SUCCESS;
  }

  for (uint32_t i = 0; i < modelBasePaths_.size(); i++) {
    qaicRunActivationCmd(programs_.at(i),
                                  QAIC_PROGRAM_CMD_DEACTIVATE_FULL);
    }
  for (uint32_t i = 0; i < modelBasePaths_.size(); i++) {
    status = qaicUnloadProgram(programs_[i]);
    if (status != QS_SUCCESS) {
      std::cerr << "Failed to unload program" << std::endl;
      return status;
    }
  }

  return QS_SUCCESS;
}

// Kept to keep backwards compatibility for resnets 50 and 34.
void QAicInfApi::setNumActivations(uint32_t num) {

  for(int i=0 ; i<num-1 ; ++i)
      modelBasePaths_.push_back(modelBasePaths_[0]);
}

void QAicInfApi::setSetSize(uint32_t setSize) { setSize_ = setSize; }

void QAicInfApi::setModelBasePath(std::string modelBasePath) {
  modelBasePaths_.push_back(modelBasePath);
}

void QAicInfApi::setNumThreadsPerQueue(uint32_t num) {
  queueProperties_.numThreadsPerQueue = num;
  numThreadsPerQueue_ = num;
}

QStatus QAicInfApi::setBufferPtr(uint32_t act_idx, uint32_t set_idx, uint32_t buf_idx, void* ptr) {
  inferenceBuffersList_[act_idx][set_idx][buf_idx].buf =  static_cast<uint8_t *>(ptr);

  QStatus status = QS_SUCCESS;

  status = shActivationSets_[act_idx]->setDataSingle(set_idx, inferenceBuffersList_[act_idx][set_idx]);
  if (status != QS_SUCCESS) {
    std::cerr <<   "Failed to set data." << std::endl;
    return status;
  }

  return status;
}



}

