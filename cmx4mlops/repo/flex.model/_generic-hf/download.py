# Adapted by Agustin Mautone, Daniel Altunay and Grigori Fursin from 
# https://github.com/mlcommons/training_results_v4.0/blob/main/Oracle/benchmarks/llama2_70b_lora/implementations/BM.GPU.H100.8/scripts/download_dataset.py

import argparse
from huggingface_hub import snapshot_download

parser = argparse.ArgumentParser(description="Download model using Hugging Face Hub")

parser.add_argument(
    "--data_dir",
    type=str,
    required=True,
    help="Local directory to download the model to",
)

parser.add_argument(
    "--repo",
    type=str,
    required=False,
    help="HF repo to download the model from",
)

args = parser.parse_args()

if args.repo == None or args.repo == '':
    print ('')
    print ('Obtaining a list of all HF models - may take some time ...')
    from huggingface_hub import list_models
    all_models = [model.id for model in list_models()]

    print ('')
    print ('Total number of HF models: {}'.format(len(all_models)))
    print ('')
    print ('Please, specify one!')

    exit(1)

print ('')
print (f'Downloading from HF repo {args.repo} ...')
print ('')

snapshot_download(
    args.repo,
    local_dir=args.data_dir,
    local_dir_use_symlinks=False,
    repo_type="model",
)
