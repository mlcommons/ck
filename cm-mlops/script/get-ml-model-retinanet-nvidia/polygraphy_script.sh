# Set these parameters
RAW_ONNX_PATH=$1
FOLDED_ONNX_PATH=$2
BACKEND_ONNX_PATH=$3
NMS_ONNX_PATH=$4

bbox_concat_node="bbox_regression"
classification_concat_node="cls_logits"


# Run once to install the dependencies. For some reason, this messes up Polygraphy's auto-fold loop, so we need to run a
# second time.
POLYGRAPHY_AUTOINSTALL_DEPS=1 polygraphy surgeon sanitize --fold-constants $RAW_ONNX_PATH -o $FOLDED_ONNX_PATH
polygraphy surgeon sanitize --fold-constants $RAW_ONNX_PATH -o $FOLDED_ONNX_PATH

# Extract backend
polygraphy surgeon extract $FOLDED_ONNX_PATH \
    --outputs ${bbox_concat_node}:auto ${classification_concat_node}:auto \
    -o $BACKEND_ONNX_PATH

# Extract NMS head
polygraphy surgeon extract $FOLDED_ONNX_PATH \
    --inputs ${classification_concat_node}:[batch_size,120087,264]:auto ${bbox_concat_node}:[batch_size,120087,4]:auto \
    -o $NMS_ONNX_PATH
