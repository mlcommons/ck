#include <iostream>

#include <onnxruntime_cxx_api.h>

int main(void) {

  std::cout << "HELLO1\n";

  Ort::Env env;

  std::cout << "HELLO2\n";

  Ort::RunOptions runOptions;

  std::cout << "HELLO3\n";

  Ort::Session session(nullptr);
  
  std::cout << "HELLO4\n";

  return 0;
}