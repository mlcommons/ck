# Examples

CM interface for https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/onnx

```bash
cm run script "install python-venv" --name=sd-test
cm run script "get generic-python-lib _package.optimum[onnxruntime]" --adr.python.name=sd-test
cm run script "activate python-venv" --name=sd-test

cm run script "python app stable-diffusion onnx" --adr.python.name=sd-test --text="crazy programmer"

cm rm cache -f
cm run script "python app stable-diffusion onnx _cuda" --adr.python.name=sd-test --text="crazy programmer"

cm docker script "python app stable-diffusion onnx" --text="crazy programmer" --output=. --docker_cm_repo=ctuning@mlcommons-ck --env.CM_DOCKER_ADD_FLAG_TO_CM_MLOPS_REPO=xyz4

```



# Resources

* https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
* https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/tree/main
* https://huggingface.co/CompVis/stable-diffusion-v1-4/tree/main
* https://huggingface.co/runwayml/stable-diffusion-v1-5
* https://huggingface.co/bes-dev/stable-diffusion-v1-4-onnx
* https://onnxruntime.ai/docs/tutorials/csharp/stable-diffusion-csharp.html
* https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main
* https://huggingface.co/docs/optimum/onnxruntime/usage_guides/models
