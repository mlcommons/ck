from huggingface_hub import hf_hub_download
import os

model_stub = os.environ.get('CM_MODEL_ZOO_STUB', '')
model_task = os.environ.get('CM_MODEL_TASK', '')

if model_task == "prune":
    print("Downloading model: " + model_stub)

    for filename in ["pytorch_model.bin", "config.json"]:

        downloaded_model_path = hf_hub_download(repo_id=model_stub,
                                                filename=filename,
                                                cache_dir=os.getcwd())

    with open('tmp-run-env.out', 'w') as f:
        f.write(f"CM_ML_MODEL_FILE_WITH_PATH={os.path.join(os.getcwd(),'')}")

else:
        model_filename = os.environ.get('CM_MODEL_ZOO_FILENAME', '')
        if model_filename == '': 
            model_filename = 'model.onnx'

        model_filenames = model_filename.split(',') if ',' in model_filename else [model_filename]

        # First must be model
        base_model_filename = model_filenames[0]

        for model_filename in model_filenames:

            print("Downloading file {} / {} ...".format(model_stub, model_filename))

            extra_dir = os.path.dirname(model_filename)

            if extra_dir!='' and not os.path.exists(extra_dir):
                os.makedirs(extra_dir)

            hf_hub_download(repo_id=model_stub,
                            filename=model_filename,
                            cache_dir=os.getcwd(),
                            force_filename=model_filename)

        with open('tmp-run-env.out', 'w') as f:
            f.write(f"CM_ML_MODEL_FILE_WITH_PATH={os.path.join(os.getcwd(),base_model_filename)}")
