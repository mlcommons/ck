from huggingface_hub import hf_hub_download
import os

model_stub= os.environ.get('CM_MODEL_ZOO_STUB', '')
model_filename= os.environ.get('CM_MODEL_ZOO_FILENAME', 'model.onnx')

print("Downloading model: "+model_stub)

downloaded_model_path = hf_hub_download(repo_id=model_stub,
                                        filename=model_filename,
                                        cache_dir=os.getcwd(),
                                        force_filename=model_filename)

with open('tmp-run-env.out', 'w') as f:
    f.write(f"CM_ML_MODEL_FILE_WITH_PATH={os.path.join(os.getcwd(),model_filename)}")

