/*
 Copyright (C) 2000-2013 by Grigori G.Fursin
 http://cTuning.org/lab/people/gfursin
*/

#include <stdio.h>
#include <stdlib.h>

#define Q 16

#ifdef OPENME
#include <openme.h>
#endif
#ifdef XOPENME
#include <xopenme.h>
#endif

void matmul(float* A, float* B, float* C, int N);

int main(int argc, char* argv[])
{
  FILE* fgg=NULL;
  int N=0;
  float QQ[Q];
  int i=0;
  int j=0;
  int k=0;

  float* A;
  float* B;
  float* C;

  long ct_repeat=0;
  long ct_repeat_max=1;
  int ct_return=0;

  char* fn;

#ifdef OPENME
  openme_init(NULL,NULL,NULL,0);
  openme_callback("PROGRAM_START", NULL);
#endif
#ifdef XOPENME
  xopenme_init(2,0);
#endif

  fn=argv[1];

  if ((getenv("CT_REPEAT_MAIN")!=NULL) && (getenv("CT_MATRIX_DIMENSION")!=NULL))
  {
    ct_repeat_max=atol(getenv("CT_REPEAT_MAIN"));
    N=atol(getenv("CT_MATRIX_DIMENSION"));
  } 
  else
  {
    if (argc<3)
    {
       printf("Usage:\n");
       printf("  matmul <data file> <matrix dimension> <repetitions>\n");
       return 1;
    }

    N=atoi(argv[2]);
    ct_repeat_max=atol(argv[3]);
  }

  printf("matrix dimension: %u\n", N);

  if ((fgg=fopen(fn,"rt"))==NULL)
  {
    fprintf(stderr,"\nError: Can't find data!\n");
    return 1;
  }

  for (i=0; i<Q; i++)
  {
    fscanf(fgg, "%f", &QQ[i]);
  }

  fclose(fgg);

  A=malloc(N*N*sizeof(float));
  B=malloc(N*N*sizeof(float));
  C=malloc(N*N*sizeof(float));

  k=0;
  for (i=0; i<N; i++)
  {
    for (j=0; j<N; j++)
    {
      A[j+i*N]=QQ[k++]*rand()/RAND_MAX;
      if (k>=Q) k=0;
      B[j+i*N]=QQ[k++]*rand()/RAND_MAX;
      if (k>=Q) k=0;
      C[j+i*N]=QQ[k++]*rand()/RAND_MAX;
      if (k>=Q) k=0;
    }
  }

#ifdef OPENME
  openme_callback("KERNEL_START", NULL);
#endif
#ifdef XOPENME
  xopenme_clock_start(0);
#endif
  for (ct_repeat=0; ct_repeat<ct_repeat_max; ct_repeat++)
    matmul(A,B,C,N);
#ifdef XOPENME
  xopenme_clock_end(0);
#endif
#ifdef OPENME
  openme_callback("KERNEL_END", NULL);
#endif

  //Print array to avoid dead code elimination
  for (i=0; i<N; i++)
  {
    printf("%u) %f %f %f\n", i, A[i*N+i], B[i*N+i], C[i*N+i]);
  }

  free(C);
  free(B);
  free(A);

#ifdef XOPENME
  xopenme_dump_state();
  xopenme_finish();
#endif
#ifdef OPENME
  openme_callback("PROGRAM_END", NULL);
#endif

  return 0;
}

void matmul(float* A, float* B, float* C, int N)
{
  int i,j,k;

  for (i=0; i<N; i++)
  {
/* Grigori remarked this line to enable cross-function data reuse just for testing
    A[i*N+j]=0; */
    for (j=0; j<N; j++)
    {
      for (k=0; k<N; k++)
      {
        A[i*N+j]=A[i*N+j]+B[i*N+k]*C[k*N+j];
      }
    }
  }
}
