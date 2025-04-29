#
# Copyright (C) 2016 by Grigori G.Fursin
#

def prepare(N,M,K):
    import math

    A=[[math.sin(float(i+j)) for i in range(M)] for j in range(N)]
    B=[[math.sin(float(i+j+1)) for i in range(K)] for j in range(M)]
    C=[[0.0 for i in range(M)] for j in range(N)]

    return A, B, C

def matmul(A,B,C):
    import numpy

    C = numpy.matmul(A,B)

    return C

##############################################################################
if __name__ == "__main__":
   import os
   import time

   repeat = int(os.environ.get('CMX_KERNEL_REPEAT', '10'))
   N = int(os.environ.get('CMX_MATMUL_DIM_N', '10'))
   M = int(os.environ.get('CMX_MATMUL_DIM_M', '10'))  
   K = int(os.environ.get('CMX_MATMUL_DIM_K', '10'))  

   print (f'Repeat={repeat}')
   print (f'N={N}')
   print (f'M={M}')
   print (f'K={K}')

   t_prepare = 0.0
   t_matmul = 0.0

   # Add openme for performance analysis (min,max,mean,modes)
   # Check loadgen
   
   print ('')
   for i in range(0, repeat):
       t = time.perf_counter()
       A,B,C = prepare(N,N,K)
       t_prepare += time.perf_counter() - t

       t = time.perf_counter()
       C = matmul(A,B,C)
       t_matmul += time.perf_counter() - t

       print (C[0][0])

   t_prepare = t_prepare / repeat
   t_matmul = t_matmul / repeat

   print ('')
   print (f'Time to prepare = {t_prepare}')
   print (f'Time to calculate = {t_matmul}')

   gflops = ((2*M*N*K)/t_matmul) / 1e9
   print (f'GFLOP/s = {gflops}')
