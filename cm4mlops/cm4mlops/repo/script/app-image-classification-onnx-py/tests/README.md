```bash
docker system prune -a -f

cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e

cm docker script "python app image-classification onnx" --docker_cm_repo=ctuning@mlcommons-ck --env.CM_IMAGE=computer_mouse.jpg
cm docker script "python app image-classification onnx" --docker_cm_repo=ctuning@mlcommons-ck --input=computer_mouse.jpg

cmrd "python app image-classification onnx" --docker_cm_repo=ctuning@mlcommons-ck --input=computer_mouse.jpg -j --docker_it

cmrd "python app image-classification onnx" --docker_cm_repo=ctuning@mlcommons-ck --input=computer_mouse.jpg --output=.


```
