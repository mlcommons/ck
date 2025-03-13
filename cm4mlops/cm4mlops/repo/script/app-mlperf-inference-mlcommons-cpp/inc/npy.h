/*
 * Adapted from NVIDIA code. Original copyright notice:
 *
 * Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef NPY_H_
#define NPY_H_

#include <algorithm>
#include <fstream>
#include <iterator>
#include <numeric>
#include <regex>
#include <vector>
#include <cstring>

// patch glog
#include <iostream>
#define CHECK(x) if (x) {} else std::cerr

namespace npy {
  class NpyFile {
  private:
    std::string m_Path;
    std::ifstream m_FStream;
    size_t m_HeaderSize;
    std::string m_Header;
    size_t m_TensorSize;
    size_t m_ElementSize;
    std::vector<size_t> m_TensorDims;
    std::vector<char> m_Cache;
  public:
    NpyFile(const std::string& path, bool cache = false) : m_Path(path), m_FStream(m_Path) {
      // magic and fixed header
      char b[256];
      m_FStream.read(b, 10);
      CHECK(m_FStream) << "Unable to parse: " << m_Path;

      // check magic
      CHECK(static_cast<unsigned char>(b[0]) == 0x93 && b[1] == 'N' && b[2] == 'U' && b[3] == 'M' && b[4] == 'P' && b[5] == 'Y') << "Bad magic: " << m_Path;

      // get header
      auto major = *reinterpret_cast<uint8_t *>(b + 6);
      //auto minor = *reinterpret_cast<uint8_t *>(b + 7);
      CHECK(major == 1) << "Only npy version 1 is supported: " << m_Path;
      m_HeaderSize = *reinterpret_cast<uint16_t *>(b + 8);
      m_Header.resize(m_HeaderSize);
      // const cast for c++14
      m_FStream.read(const_cast<char *>(m_Header.data()), m_HeaderSize);

      // get file size
      auto cur = m_FStream.tellg();
      m_FStream.seekg(0, std::ios::end);
      auto size = m_FStream.tellg();
      m_TensorSize = size - cur;

      // cache result
      if (cache) {
        m_FStream.seekg(10 + m_HeaderSize, std::ios::beg);
        m_Cache.resize(m_TensorSize);
        m_FStream.read(m_Cache.data(), m_TensorSize);
        CHECK(m_FStream) << "Unable to parse: " << m_Path;
        CHECK(m_FStream.peek() == EOF) << "Did not consume full file: " << m_Path;
      }

      // parse header
      std::regex re(R"re(\{'descr': '[<|][fi]([\d])', 'fortran_order': False, 'shape': \(([\d, ]*)\), \} +\n)re");
      std::smatch matches;
      CHECK(std::regex_match(m_Header, matches, re)) << "Cannot parse numpy header: " << m_Path;
      CHECK(matches.size() == 3) << "Cannot parse numpy header: " << m_Path;
      m_ElementSize = std::stoi(matches[1]);
      std::vector<std::string> dims = splitString(matches[2], ", ");
      m_TensorDims.resize(dims.size());
      std::transform(dims.begin(), dims.end(), m_TensorDims.begin(), [](const std::string& s){ return std::stoi(s); });

      // check header sanity
      size_t tensorSize = std::accumulate(m_TensorDims.begin(), m_TensorDims.end(), m_ElementSize, std::multiplies<size_t>());
      CHECK(tensorSize == m_TensorSize) << "Header description does not match file size: " << m_Path;

    }
    ~NpyFile() {
      m_FStream.close();
    };
    std::vector<size_t> getDims() {
      return m_TensorDims;
    }
    size_t getTensorSize() {
      return m_TensorSize;
    }
    // load the entire tensor
    void loadAll(std::vector<char>& dst) {
      m_FStream.seekg(10 + m_HeaderSize, std::ios::beg);
      dst.resize(m_TensorSize);
      m_FStream.read(dst.data(), m_TensorSize);
      CHECK(m_FStream) << "Unable to parse: " << m_Path;
      CHECK(m_FStream.peek() == EOF) << "Did not consume full file: " << m_Path;
    }
    // cache the entire tensor
    void cacheAll() {
      loadAll(m_Cache);
    }
    // load only selected indices from the Tensor, assuming that the first dim is batch dim.
    void loadSamples(std::vector<char>& dst, const std::vector<size_t>& indices) {
      if (m_Cache.empty()) {
        cacheAll();
      }
      size_t sampleSize = std::accumulate(m_TensorDims.begin() + 1, m_TensorDims.end(), m_ElementSize, std::multiplies<size_t>());
      dst.resize(sampleSize * indices.size());
      for (size_t i = 0; i < indices.size(); i++) {
        std::memcpy(dst.data() + i * sampleSize, m_Cache.data() + indices[i] * sampleSize, sampleSize);
      }
    }
    // helper function to split a string based on a delimiting character
    std::vector<std::string> splitString(const std::string& input, const std::string& delimiter)
    {
      std::vector<std::string> result;
      size_t start = 0;
      size_t next = 0;
      while(next != std::string::npos)
      {
        next = input.find(delimiter, start);
        result.emplace_back(input, start, next - start);
        start = next + 1;
      }
      return result;
    }
  };
}

#endif // NPY_H_
