# CM/CK repoducibility demo for IPOL journal

Code and sample images are taken from https://ipolcore.ipol.im/demo/clientApp/demo.html?id=439 

The demo illustrates the method proposed by Daudt et al. (2019) for change detection on satellite images. It takes as input two color images in PNG format. Both images should be satellites images of the same area, and co-registered.
The output image is a change map. For each pixel in the input images, the value of the change map is 1 if a change is detected and 0 otherwise.

Pair of images from the OSCD test set are already provided with the demo. For those images, 
the ground truth is available in the original dataset: https://ieee-dataport.org/open-access/oscd-onera-satellite-change-detection.

# TBD
