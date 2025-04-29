/*

 XOpenME cTuning support run-time library
 (unlike OpenME dynamic plugin framework, this lib is linked directly)

 cTuning plugin is used for fine-grain online application timing and tuning

 OpenME - Event-driven, plugin-based interactive interface to "open up" 
          any software (C/C++/Fortran/Java/PHP) and possibly connect it to cM

 Developer(s): (C) 2015, Grigori Fursin 
 http://cTuning.org/lab/people/gfursin

 This library is free software; you can redistribute it and/or
 modify it under the terms of the GNU Lesser General Public
 License as published by the Free Software Foundation; either
 version 2.1 of the License, or (at your option) any later version.

 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public
 License along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

*/

#include "xopenme.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef __MINGW32__
# include <sys/time.h>
#else
# ifdef WINDOWS
#  include <time.h>
# else
#  include <sys/time.h>
# endif
#endif

static char* ck_time_file="tmp-ck-timer.json";

#ifdef WINDOWS
# define MYTIMER1 clock_t
 static MYTIMER1 *start;
#else 
# define MYTIMER1 double
# define MYTIMER2 struct timeval
 static MYTIMER1 *start;
 static MYTIMER2 *before, after;
#endif

static int nntimers=0;
static double *secs;

static int nnvars=0;
static char **vars;

static int nnfiles=0; /* Reading from file such as energy or frequency */
static char **files;
static double *fvars1;
static double *fvars2;

static char *env;

static char buf[128]; /* tmp buffer */

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_init(int ntimers, int nvars)
{
  int timer;
  int var;
  int k=0;
  int k1=0;
  int kl=0;
  int nf=0;

  if ((env = getenv(XOPENME_TIME_FILE)) != NULL)
    ck_time_file=env;

  if ( ((env = getenv(XOPENME_DEBUG)) != NULL) && (atoi(env)==1) )
    printf("XOPENME event: start program\n");

  nntimers=ntimers;
  nnvars=nvars;

  /* init timers */
  if (ntimers>0)
  {
     secs=malloc((ntimers+1)*sizeof(double));
     start=malloc((ntimers+1)*sizeof(MYTIMER1));
#ifdef MYTIMER2     
     before=malloc(ntimers*sizeof(MYTIMER2));
#endif

     for (timer=0; timer<nntimers; timer++)
     {
       secs[timer] = 0.0;
       start[timer] = 0.0;
     }
  }

  /* init vars */
  if (nvars>0)
  {
    vars=malloc((nvars+1)*sizeof(char*)); 

    for (var=0; var<nvars; var++)
    {

      vars[var]=(char*) malloc(512*sizeof(char)); // temporal and ugly - should check the length ...
      vars[var][0]=0;
    }
  }

  /* init files */
  env = getenv(XOPENME_FILES);
  if (env!=NULL)
  {
    kl=strlen(env);
    if (kl>0)
    {
      nnfiles++;
      for (k=0; k<strlen(env); k++)
      {
        if (env[k]==';') nnfiles++;
      }
    }
  }

  files=malloc((nnfiles+1)*sizeof(char*)); 
  fvars1=malloc((nnfiles+1)*sizeof(double)); 
  fvars2=malloc((nnfiles+1)*sizeof(double)); 

  if (nnfiles>0)
  {
     k=0;
     k1=0;
     nf=0;

     while (k1<kl)
     {
       k1++;
       if (k1>=kl || env[k1]==';' )
       {
         files[nf]=(char*) malloc((k1-k+1)*sizeof(char));

         strncpy(files[nf],&env[k],k1-k);
         files[nf][k1-k]=0;

         fvars1[nf]=0.0;
         fvars2[nf]=0.0;

         nf++;
         k=k1+1;
       }
     }
   }
}

void read_files(double *fvars)
{
  int nf=0;
  FILE *f=NULL;

  /* Read files */
  if (nnfiles>0)
  {
    for (nf=0; nf<nnfiles; nf++)
    {
      f=fopen(files[nf], "r");
      if (f!=NULL)
      {
        if (fgets(buf, 32, f)!=NULL)
           fvars[nf]=atof(buf);
        else
           fvars[nf]=0,0;
        fclose(f);
      }
    }
  }
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_clock_start(int timer)
{
#ifdef WINDOWS
  start[timer] = clock();
#else
  #ifdef __INTEL_COMPILERX
    start[timer] = (double)_rdtsc();
  #else
    gettimeofday(&before[timer], NULL);
  #endif
#endif
  if ( ((env = getenv(XOPENME_DEBUG)) != NULL) && (atoi(env)==1) )
    printf("XOpenME event: start clock\n");

  read_files(fvars1);
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_clock_end(int timer)
{
#ifdef WINDOWS
  secs[timer] = ((double)(clock() - start[timer])) / CLOCKS_PER_SEC;
#else
  #ifdef __INTEL_COMPILERX
  secs[timer] = ((double)((double)_rdtsc() - start[timer])) / (double) getCPUFreq();
  #else
  gettimeofday(&after, NULL);
  secs[timer] = (after.tv_sec - before[timer].tv_sec) + (after.tv_usec - before[timer].tv_usec)/1000000.0;
  #endif
#endif
  if ( ((env = getenv(XOPENME_DEBUG)) != NULL) && (atoi(env)==1) )
    printf("XOpenME event: stop clock: %f\n", secs[timer]);

  read_files(fvars2);
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_add_var_i(int var, char* desc, int svar)
{
  sprintf(vars[var], desc, svar);
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_add_var_f(int var, char* desc, float svar)
{
  sprintf(vars[var], desc, svar);
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_add_var_d(int var, char* desc, double svar)
{
  sprintf(vars[var], desc, svar);
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_add_var_s(int var, char* desc, void* svar)
{
  sprintf(vars[var], desc, svar);
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_dump_memory(char* name, void* array, long size)
{
  FILE *fx=fopen(name , "wb" );
  fwrite(array, size, 1, fx);
  fclose(fx);
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_dump_state(void)
{
  FILE* f;
  int timer;
  int var;
  int energy=0; // set from CK_MONITOR_ENERGY

  env = getenv(XOPENME_ENERGY);
  if (env!= NULL)
     energy=atoi(env);

  if ( ((env = getenv(XOPENME_DEBUG)) != NULL) && (atoi(env)==1) )
    printf("XOPENME event: dumping state\n");

  f=fopen(ck_time_file, "w");
  if (f==NULL)
  {
    printf("Error: can't open timer file %s for writing\n", ck_time_file);
    exit(1);
  }

  fprintf(f,"{\n");

  if (nntimers>0) 
  {
     fprintf(f," \"execution_time\":%.6lf", secs[0]);
     for (timer=0; timer<nntimers; timer++) 
     {
       fprintf(f,",\n \"execution_time_kernel_%u\":%.6lf", timer, secs[timer]);
     }
  }

  if (nnvars>0)
  {
    fprintf(f,",\n \"run_time_state\":{\n");

    for (var=0; var<nnvars; var++) 
    {
      if ((vars[var][0]!=0))
      {
         if (var!=0) fprintf(f, ",\n");
         fprintf(f,"  %s", vars[var]);
      }
    }

    for (var=0; var<nnfiles; var++) 
    {
      if (nnvars>0 || var!=0) fprintf(f, ",\n");
      fprintf(f,"    \"file_%u_start\":%f", var, fvars1[var]);
      fprintf(f,",\n    \"file_%u_stop\":%f", var, fvars2[var]);

      if (energy==1 && nntimers>0)
         fprintf(f,",\n    \"file_%u_energy\":%f", var, ((fvars2[var]+fvars1[var])/2)*secs[0]);
    }

    fprintf(f,"\n }");
  }

  fprintf(f,"\n}\n");

  fclose(f);
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
double xopenme_get_timer(int timer)
{
  return secs[timer];
}

/*****************************************************************/
extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_finish(void)
{
  int timer;
  int var;

  if (nnvars>0)
  {
    for (var=0; var<nnvars; var++) 
    {
      free(vars[var]);
    }
    free(vars);
  }

  if (nntimers>0)
  {
    free(secs);
    free(start);
#ifdef MYTIMER2
    free(before);
#endif
  }

  if (nnfiles>0)
  {
    for (var=0; var<nnfiles; var++)
    {
      free(files[var]);
    }

    free(fvars1);
    free(fvars2);
  }
}
