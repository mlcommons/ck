from huggingface_hub import hf_hub_download
import os

model_stub = os.environ.get('CM_MODEL_ZOO_STUB', '')
model_task = os.environ.get('CM_MODEL_TASK', '')

revision = os.environ.get('CM_HF_REVISION','')

if model_task == "prune":
    print("Downloading model: " + model_stub)

    for filename in ["pytorch_model.bin", "config.json"]:

        downloaded_model_path = hf_hub_download(repo_id=model_stub,
                                                filename=filename,
                                                cache_dir=os.getcwd())

    with open('tmp-run-env.out', 'w') as f:
        f.write(f"CM_ML_MODEL_FILE_WITH_PATH={os.path.join(os.getcwd(),'')}")

else:
        subfolder = os.environ.get('CM_HF_SUBFOLDER', '')
        full_subfolder = os.environ.get('CM_HF_FULL_SUBFOLDER', '')

        model_filename = os.environ.get('CM_MODEL_ZOO_FILENAME', '')
        if model_filename == '':
            model_filename = 'model.onnx'

        model_filenames = model_filename.split(',') if ',' in model_filename else [model_filename]

        # First must be model
        base_model_filename = model_filenames[0]

        files = []
        if full_subfolder!='':

            from huggingface_hub import HfFileSystem
            fs = HfFileSystem()

            # List all files in a directory
            path = model_stub+'/'+full_subfolder

            print ('')
            print ('Listing files in {} ...'.format(path))

            def list_hf_files(path):
                all_files = []
                
                xrevision = None if revision == '' else revision
                files=fs.ls(path, revision=xrevision) #, detail=False)            

                for f in files:
                    fname = f['name']
                    fdir = f['type'] == 'directory'

                    if fdir:
                        all_files += list_hf_files(fname)
                    else:
                        all_files.append(fname)

                return all_files
                        
            
            files=list_hf_files(path)

            print ('')
            print ('Found {} files'.format(len(files)))
            
            for f in files:

                remove = len(model_stub)+1

                if revision!='':
                    remove+=len(revision)+1

                ff = f[remove:]

                if ff not in model_filenames:
                    model_filenames.append(ff)


        print ('')
        for model_filename in model_filenames:

            print("Downloading file {} / {} ...".format(model_stub, model_filename))

            extra_dir = os.path.dirname(model_filename)

            if extra_dir!='' and not os.path.exists(extra_dir):
                os.makedirs(extra_dir)

            
            xrevision = None if revision == '' else revision
            xsubfolder = None if subfolder == '' else subfolder

            hf_hub_download(repo_id=model_stub,
                       subfolder=xsubfolder,
                       filename=model_filename,
                       force_filename=model_filename,
                       revision=xrevision,
                       cache_dir=os.getcwd())
        

        print ('')
        
        with open('tmp-run-env.out', 'w') as f:
            f.write(f"CM_ML_MODEL_FILE_WITH_PATH={os.path.join(os.getcwd(),base_model_filename)}")
