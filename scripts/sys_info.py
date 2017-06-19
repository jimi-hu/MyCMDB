#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年6月4日

@author: hujie
'''
import psutil
def sys_info():
    mem=psutil.virtual_memory().total
    mem_total=str(int(mem/2**30))+"G"
    cpu_total=psutil.cpu_count()
    info = {"mem":mem_total,"cpu":cpu_total}
    print info
#    return info

sys_info()
