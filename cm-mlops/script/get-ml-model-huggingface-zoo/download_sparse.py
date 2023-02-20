from setfit import SetFitModel
import os

model_stub= os.environ.get('CM_MODEL_ZOO_STUB', '')
curr_script_path = os.environ.get('CM_TMP_CURRENT_SCRIPT_PATH','')
print(f"Downloading model {model_stub}")
stub = f"{model_stub}"
model = SetFitModel.from_pretrained(stub, cache_dir='.')

model._save_pretrained(stub)

with open('tmp-run-env.out', 'w') as f:
    f.write(f"CM_ML_MODEL_FILE_WITH_PATH={curr_script_path+'/'+stub}")

