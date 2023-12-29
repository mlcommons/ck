import onnx
import os
import sys
import argparse
import yaml

def parse_args(add_help=True):
    parser = argparse.ArgumentParser(description='Print node precision info for the onnx file', add_help=add_help)
    parser.add_argument('--input', default="retinanet.onnx", help='input onnx file')
    parser.add_argument('--output', default="node-precision.yaml", help='output node precision file')
    args = parser.parse_args()

    return args

def main(args):

    onnx_model = onnx.load(args.input)
    list1 = [
        "/backbone/fpn/inner_blocks.0/Conv_output_0",
        "/head/classification_head/Sigmoid_output_0",
        "/head/classification_head/Sigmoid_1_output_0",
        "/head/classification_head/Sigmoid_2_output_0",
        "/head/classification_head/Sigmoid_3_output_0",
        "/head/classification_head/Sigmoid_4_output_0"
    ]
    list2 = [
        "1421",
        "1481",
        "1517",
        "1553",
        "1589",
        "1625",
    ]

    #check which list of node names is valid
    node_names = []
    valid_list = None

    #for n in enumerate_model_node_outputs(onnx_model):
    for n in onnx_model.graph.node:
        node_names.append(n.output[0])

    if set(list1) < set(node_names):
        valid_list = list1
    elif set(list2) < set(node_names):
        valid_list = list2
    else:
        print("Node names are not matching with the expected ones in the input onnx file.")
        sys.exit(1)

    node_precision_info = {}
    node_precision_info['FP16NodeInstanceNames'] = []

    fp16nodes = valid_list
    fp16nodes += [ "boxes_1", "boxes_2", "boxes_3", "boxes_4", "boxes_5", "scores_1", "scores_2", "scores_3", "scores_4", "scores_5"]

    #node_precision_info['FP16NodeInstanceNames'] = "["+", ".join(fp16nodes)+"]"
    node_precision_info['FP16NodeInstanceNames'] = fp16nodes

    yaml_output = yaml.safe_dump(node_precision_info, default_style=None)
    with open(args.output, "w") as f:
        f.write(yaml_output)

    print(f"Node precision info successfully printed out to {args.output}")

    
if __name__ == "__main__":
    args = parse_args()
    main(args)
