#ifndef WINDOWS
 #include <unistd.h>
#endif

#include <stdio.h>
#include <cuda.h>

int main(int argc, char *argv[])
{
  int ndev=0;
  int id=0;
  cudaError_t error;
  cudaDeviceProp features;

  int rtver=0;
  int dver=0;

  /* Get number of devices */
  error = cudaGetDeviceCount(&ndev);
  if (error != cudaSuccess) {
    printf("Error: problem obtaining number of CUDA devices: %d\n", error);
    return 1;
  }

  /* Iterating over devices */
  for (id=0; id<ndev; id++)
  {
     cudaSetDevice(id);

     printf("GPU Device ID: %d\n", id);

     cudaGetDeviceProperties(&features, id);
     if (error != cudaSuccess) {
       printf("Error: problem obtaining features of CUDA devices: %d\n", error);
       return 1;
     }

     printf("GPU Name: %s\n", features.name);
     printf("GPU compute capability: %d.%d\n", features.major, features.minor);

     error=cudaDriverGetVersion(&dver);
     if (error != cudaSuccess) {
       printf("Error: problem obtaining CUDA driver version: %d\n", error);
       return 1;
     }

     error=cudaRuntimeGetVersion(&rtver);
     if (error != cudaSuccess) {
       printf("Error: problem obtaining CUDA run-time version: %d\n", error);
       return 1;
     }

     printf("CUDA driver version: %d.%d\n", dver/1000, (dver%100)/10);
     printf("CUDA runtime version: %d.%d\n", rtver/1000, (rtver%100)/10);

     printf("Global memory: %llu\n", (unsigned long long) features.totalGlobalMem);
     printf("Max clock rate: %f MHz\n", features.clockRate * 0.001);

     printf("Total amount of shared memory per block: %lu\n", features.sharedMemPerBlock);
     printf("Total number of registers available per block: %d\n", features.regsPerBlock);
     printf("Warp size: %d\n", features.warpSize);
     printf("Maximum number of threads per multiprocessor:  %d\n", features.maxThreadsPerMultiProcessor);
     printf("Maximum number of threads per block: %d\n", features.maxThreadsPerBlock);
     printf("Max dimension size of a thread block X: %d\n", features.maxThreadsDim[0]);
     printf("Max dimension size of a thread block Y: %d\n", features.maxThreadsDim[1]);
     printf("Max dimension size of a thread block Z: %d\n", features.maxThreadsDim[2]);
     printf("Max dimension size of a grid size X: %d\n", features.maxGridSize[0]);
     printf("Max dimension size of a grid size Y: %d\n", features.maxGridSize[1]);
     printf("Max dimension size of a grid size Z: %d\n", features.maxGridSize[2]);
     printf("\n");
  }

  return error;
}
