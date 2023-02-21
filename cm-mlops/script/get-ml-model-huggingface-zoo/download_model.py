from setfit import SetFitModel
import os

model_stub= os.environ.get('CM_MODEL_ZOO_STUB', '')
print(f"Downloading model {model_stub}")
stub = f"{model_stub}"
model = SetFitModel.from_pretrained(stub, cache_dir=os.getcwd())

model._save_pretrained(stub)

with open('tmp-run-env.out', 'w') as f:
    f.write(f"CM_ML_MODEL_FILE_WITH_PATH={os.path.join(os.getcwd(),stub)}")
