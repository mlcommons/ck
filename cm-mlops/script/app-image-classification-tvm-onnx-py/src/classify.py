"""
Developers:
 - grigori@octoml.ai
"""

import time
import os
import argparse
import json

from PIL import Image
import cv2

import numpy as np

import onnxruntime as rt



# Image conversion from MLPerf(tm) vision
def center_crop(img, out_height, out_width):
    height, width, _ = img.shape
    left = int((width - out_width) / 2)
    right = int((width + out_width) / 2)
    top = int((height - out_height) / 2)
    bottom = int((height + out_height) / 2)
    img = img[top:bottom, left:right]
    return img


def resize_with_aspectratio(img, out_height, out_width, scale=87.5, inter_pol=cv2.INTER_LINEAR):
    height, width, _ = img.shape
    new_height = int(100. * out_height / scale)
    new_width = int(100. * out_width / scale)
    if height > width:
        w = new_width
        h = int(new_height * height / width)
    else:
        h = new_height
        w = int(new_width * width / height)
    img = cv2.resize(img, (w, h), interpolation=inter_pol)
    return img


# returns list of pairs (prob, class_index)
def get_top5(all_probs):
  probs_with_classes = []

  for class_index in range(len(all_probs)):
    prob = all_probs[class_index]
    probs_with_classes.append((prob, class_index))

  sorted_probs = sorted(probs_with_classes, key = lambda pair: pair[0], reverse=True)
  return sorted_probs[0:5]

def run_case(dtype, image, target):
    # Check image
    import os
    import json
    import sys

    STAT_REPEAT=os.environ.get('STAT_REPEAT','')
    if STAT_REPEAT=='' or STAT_REPEAT==None:
       STAT_REPEAT=10
    STAT_REPEAT=int(STAT_REPEAT)

    # FGG: set model files via CM env
    CATEG_FILE = 'synset.txt'
    synset = eval(open(os.path.join(CATEG_FILE)).read())

    files=[]
    val={}

    # FGG: set timers
    import time
    timers={}

    img_orig = cv2.imread(image)

    img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)

    output_height, output_width, _ = 224, 224, 3
    img = resize_with_aspectratio(img, output_height, output_width, inter_pol=cv2.INTER_AREA)
    img = center_crop(img, output_height, output_width)
    img = np.asarray(img, dtype='float32')

    # normalize image
    means = np.array([123.68, 116.78, 103.94], dtype=np.float32)
    img -= means

    # transpose if needed
    img = img.transpose([2, 0, 1])

    import matplotlib.pyplot as plt
    img1 = img.transpose([1, 2, 0])
    arr_ = np.squeeze(img1) # you can give axis attribute if you wanna squeeze in specific dimension
    plt.imshow(arr_)
#    plt.show()
    plt.savefig('pre-processed-image.png')
    # Load model
    model_path=os.environ.get('CM_ML_MODEL_FILE_WITH_PATH','')
    if model_path=='':
        print ('Error: environment variable CM_ML_MODEL_FILE_WITH_PATH is not defined')
        exit(1)

    opt = rt.SessionOptions()

    if len(rt.get_all_providers()) > 1 and os.environ.get("USE_CUDA", "yes").lower() not in [ "0", "false", "off", "no" ]:
        #Currently considering only CUDAExecutionProvider
        sess = rt.InferenceSession(model_path, opt, providers=['CUDAExecutionProvider'])
    else:
        sess = rt.InferenceSession(model_path, opt, providers=["CPUExecutionProvider"])

    inputs = [meta.name for meta in sess.get_inputs()]
    outputs = [meta.name for meta in sess.get_outputs()]

    print (inputs)
    print (outputs)




    if os.environ.get('USE_TVM','')=='yes':
        import tvm
        from tvm import relay
        import onnx

        del sess

        # Load model via ONNX to be used with TVM
        print ('')
        print ('ONNX: load model ...')
        print ('')

        onnx_model = onnx.load(model_path)

        # Init TVM
        # TBD: add tvm platform selector
        if os.environ.get('USE_CUDA','')=='yes':
           # TVM package must be built with CUDA enabled
           ctx = tvm.cuda(0)
        else:
           ctx = tvm.cpu(0)
        tvm_ctx = ctx

        build_conf = {'relay.backend.use_auto_scheduler': False}
        opt_lvl = int(os.environ.get('TVM_OPT_LEVEL', 3))
        host = os.environ.get('CM_HOST_PLATFORM_FLAVOR')
        if host == 'x86_64' and 'AMD' in os.environ.get('CM_HOST_CPU_VENDOR_ID',''):
            target = os.environ.get('TVM_TARGET', 'llvm -mcpu=znver2')
        else:
            target = os.environ.get('TVM_TARGET', 'llvm')

        target_host=None
        params={}

        # New target API
        tvm_target = tvm.target.Target(target, host=target_host)

        input_shape = (1, 3, 224, 224)
        shape_dict = {inputs[0]: input_shape}

        print ('')
        print ('TVM: import model ...')
        print ('')
        # Extra param: opset=12
        mod, params = relay.frontend.from_onnx(onnx_model, shape_dict, freeze_params=True)

        print ('')
        print ('TVM: transform to static ...')
        print ('')
        mod = relay.transform.DynamicToStatic()(mod)

        print ('')
        print ('TVM: apply extra optimizations ...')
        print ('')
        # Padding optimization
        # Adds extra optimizations
        mod = relay.transform.FoldExplicitPadding()(mod)


        print ('')
        print ('TVM: build model ...')
        print ('')

        executor=os.environ.get('MLPERF_TVM_EXECUTOR','graph')

        if executor == "graph" or executor == "debug":
            from tvm.contrib import graph_executor

            # Without history
            with tvm.transform.PassContext(opt_level=opt_lvl, config=build_conf):
                graph_module = relay.build(mod,
                                           target=tvm_target,
                                           params=params)
            lib = graph_module

            print ('')
            print ('TVM: init graph engine ...')
            print ('')

            sess = graph_executor.GraphModule(lib['default'](ctx))


        elif executor == "vm":
            from tvm.runtime.vm import VirtualMachine

            # Without history
            with tvm.transform.PassContext(opt_level=opt_lvl, config=build_conf):
                vm_exec = relay.vm.compile(mod, target=tvm_target, params=params)

            r_exec = vm_exec

            print ('')
            print ('TVM: init VM ...')
            print ('')

            sess = VirtualMachine(r_exec, ctx)


        # For now only graph
        sess.set_input(inputs[0], tvm.nd.array([img]))

        # Run TVM inference
        sess.run()

        # Process TVM outputs
        output = []

        for i in range(sess.get_num_outputs()):
            # Take only the output of batch size for dynamic batches
            if len(output)<(i+1):
                output.append([])
            output[i].append(sess.get_output(i).asnumpy()[0])



    else:
       inp={inputs[0]:np.array([img], dtype=np.float32)}
       output=sess.run(outputs, inp)




    top1 = np.argmax(output[1])-1 #.asnumpy())

    top5=[]
    atop5 = get_top5(output[1][0]) #.asnumpy())

    print ('')
    print('Prediction Top1:', top1, synset[top1])

    print ('')
    print('Prediction Top5:')
    for p in atop5:
        out=p[1]-1
        name=synset[out]
        print (' * {} {}'.format(out, name))

    ck_results={
      'prediction':synset[top1]
    }

    with open('tmp-ck-timer.json', 'w') as ck_results_file:
       json.dump(ck_results, ck_results_file, indent=2, sort_keys=True)

    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help="Path to JPEG image.", default=None, required=True)
    parser.add_argument('--target', type=str, help="Target", default=None)
    args = parser.parse_args()

    if args.image.strip().lower()=='':
        print ('Please specify path to an image using CM_IMAGE environment variable!')
        exit(1)

    # set parameter
    batch_size = 1
    num_classes = 1000
    image_shape = (3, 224, 224)

    # load model
    data_shape = (batch_size,) + image_shape
    out_shape = (batch_size, num_classes)

    dtype='float32'
    if os.environ.get('CM_TVM_DTYPE','')!='':
       dtype=os.environ['CM_TVM_DTYPE']

    run_case(dtype, args.image, args.target)
