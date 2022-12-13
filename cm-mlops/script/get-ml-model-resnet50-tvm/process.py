import os
import tvm
# Import model to TVM
from tvm import relay
max_batchsize = os.environ.get('CM_ML_MODEL_MAX_BATCH_SIZE')
input_shapes = os.environ.get('CM_ML_MODEL_INPUT_SHAPES','').strip()
if input_shapes == '':
    print ('')
    raise Exception("Error: CM_ML_MODEL_INPUT_SHAPES environment variable is not defined!")

input_shapes = input_shapes.replace('BATCH_SIZE', str(max_batchsize))
model_path = os.environ.get('CM_ML_MODEL_FILE_WITH_PATH')

print ('TVM model: '+model_path)
# Check if load precompiled model
compiled_model = os.path.join(os.getcwd(), 'model-tvm.so')
if model_path.endswith('.so') or model_path.endswith('.dylib'):
    compiled_model = model_path

    if not os.path.isfile(compiled_model):
        print ('')
        raise Exception("Error: Model file {} not found!".format(compiled_model))


build_conf = {}
params = {}

if model_path.endswith('.pt'):
   import torch
   from tvm.relay.build_module import bind_params_by_name

   shape_list = eval('[' + input_shapes + ']')

   print ('TVM shape list: '+str(shape_list))

   x=os.environ.get('CM_MLPERF_TVM_TORCH_QUANTIZED_ENGINE','')
   if x!='':
       torch.backends.quantized.engine = x
   pytorch_model = torch.jit.load(model_path)
   pytorch_model.eval()

   mod, params = relay.frontend.from_pytorch(pytorch_model, shape_list)

   mod["main"] = bind_params_by_name(mod["main"], params)

   # Some optimizations
   mod = relay.transform.FoldConstant()(mod)

   if os.environ.get('CM_MLPERF_TVM_USE_DNNL','').strip().lower() == 'yes':
      from tvm.relay.op.contrib.dnnl import partition_for_dnnl
      from tvm.driver.tvmc.common import convert_graph_layout

      #  move to NHWC layout, prerequisite for DNNL partitioning
      mod = convert_graph_layout(mod, "NHWC")
      mod = relay.transform.FoldConstant()(mod)

      mod = partition_for_dnnl(mod)

elif model_path.endswith('.onnx'):
   import onnx

   shape_dict = eval('{' + input_shapes + '}')

   print ('TVM shape dict: '+str(shape_dict))

   onnx_model = onnx.load(model_path)

   mod, params = relay.frontend.from_onnx(onnx_model, shape_dict, freeze_params=True)

   # Some optimizations
   mod = relay.transform.DynamicToStatic()(mod)
   #mod = relay.transform.FoldExplicitPadding()(mod)

   if os.environ.get('CM_MLPERF_TVM_TRANSFORM_LAYOUT','').strip().lower() == 'yes':
      kernel_layout='NHWC'

      desired_layouts = {
              'qnn.conv2d': [kernel_layout, 'default'],
              'nn.conv2d': [kernel_layout, 'default'],
              'nn.conv2d_transpose': [kernel_layout, 'default'],
              'nn.depthwise_conv2d': [kernel_layout, 'default'],
              'nn.conv3d': [kernel_layout, 'default'],
              'nn.conv3d_transpose': [kernel_layout, 'default'],
              }

      seq = tvm.transform.Sequential([relay.transform.RemoveUnusedFunctions(),
          relay.transform.FoldConstant(),
          relay.transform.ConvertLayout(desired_layouts),
          ])

      with tvm.transform.PassContext(opt_level=3):
          mod = seq(mod)

elif model_path.endswith('.tflite'):
   # Grigori used https://tvm.apache.org/docs/tutorials/frontend/deploy_prequantized_tflite.html

   import tflite

   shape_dict = eval('{' + input_shapes + '}')

   print ('TVM shape dict: '+str(shape_dict))

   tflite_model_buf = open(model_path, "rb").read()
   tflite_model = tflite.Model.GetRootAsModel(tflite_model_buf, 0)

   mod, params = relay.frontend.from_tflite(tflite_model, shape_dict)

else:
   print ('')
   raise Exception("Error: model extension is not supported in TVM backend ({})!".format(model_path))

          # Build model
# TBD! Apply autotuning history!
opt_lvl = int(os.environ.get('CM_MLPERF_TVM_OPT_LEVEL', 3))

target = os.environ.get('CM_MLPERF_TVM_TARGET', 'llvm')

target_host=None

# New target API
tvm_target = tvm.target.Target(target, host=target_host)

# Check if apply history
tvm_history_json_file = os.environ.get('CM_MLPERF_TVM_APPLY_HISTORY','').strip()
if tvm_history_json_file!='':
    if not os.path.isfile(tvm_history_json_file):
        print ('')
        raise Exception("Error: TVM history file {} not found!".format(tvm_history_json_file))

    build_conf['relay.backend.use_auto_scheduler']=True

    with auto_scheduler.ApplyHistoryBest(tvm_history_json_file):
       with tvm.transform.PassContext(opt_level=opt_lvl, config=build_conf):
           lib=relay.build(mod, target=tvm_target, params=params)
else:
    with tvm.transform.PassContext(opt_level=opt_lvl, config=build_conf):
        lib=relay.build(mod, target=tvm_target, params=params)

lib.export_library(compiled_model)

print ('TVM compiled model: '+compiled_model)
