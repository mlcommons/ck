/*

 CK OpenME cTuning plugin

 cTuning plugin is used for fine-grain online application timing and tuning

 OpenME - Event-driven, plugin-based interactive interface to "open up" 
          any software (C/C++/Fortran/Java/PHP) and possibly connect it to cM

 Developer(s): (C) Grigori Fursin
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

#ifndef __XOPENME_H_
#define __XOPENME_H_

#define XOPENME_DEBUG "XOPENME_DEBUG"
#define XOPENME_TIME_FILE "XOPENME_TIME_FILE"
#define XOPENME_FILES "XOPENME_FILES"
#define XOPENME_ENERGY "CK_MONITOR_ENERGY" /* If 1, monitor energy from files */

/*************************************/
#ifdef __cplusplus
extern "C"
{
#endif
/*************************************/

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_clock_start(int timer);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_clock_end(int timer);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_init(int ntimers, int nvars);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_dump_state(void);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_add_var_i(int var, char* desc, int svar);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_add_var_f(int var, char* desc, float svar);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_add_var_d(int var, char* desc, double svar);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_add_var_s(int var, char* desc, void* svar);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_dump_memory(char* name, void* array, long size);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
double xopenme_get_timer(int timer);

extern 
#ifdef WINDOWS
__declspec(dllexport) 
#endif
void xopenme_finish(void);

#ifdef __cplusplus
}
#endif

#endif