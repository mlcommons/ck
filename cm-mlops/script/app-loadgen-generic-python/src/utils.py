# Developer: Grigori Fursin

import os
import psutil

def print_host_memory_use(text=''):

    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_info()[0]

    if text == '': text = 'host memory use'
    
    print('{}: {} MB'.format(text, int(memoryUse/1000000)))

    return
