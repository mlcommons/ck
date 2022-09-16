#ifndef MODEL_H_
#define MODEL_H_

#include <cstddef>
#include <functional>
#include <string>
#include <vector>

class Model {
public:
    std::string model_path;

    size_t num_inputs;
    std::vector<std::string> input_names;
    std::vector<std::vector<size_t>> input_shapes;
    std::vector<size_t> input_sizes;

    size_t num_outputs;
    std::vector<std::string> output_names;
    std::vector<std::vector<size_t>> output_shapes;
    std::vector<size_t> output_sizes;
    std::function<void(void *response)> postprocess;
};

#endif // MODEL_H_
