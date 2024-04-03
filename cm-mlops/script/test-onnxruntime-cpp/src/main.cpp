#include <iostream>

#include <onnxruntime_cxx_api.h>

int main(void) {

  std::cout << "- ORT init 1\n";

  std::string version = Ort::GetVersionString();

  std::cout << version << std::endl;

  std::cout << "- ORT init 2\n";

  Ort::Env env;

  std::cout << "- ORT init 3\n";

  Ort::RunOptions runOptions;

  std::cout << "- ORT init 4\n";

  Ort::Session session(nullptr);

  std::cout << "  SUCCESS!\n";


  return 0;
}
