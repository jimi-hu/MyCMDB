#coding:utf-8
'''
Created on 2017年6月25日

@author: hujie
'''
import os 

from MyCMDB.project_dir import PROJECT_DIR 
def file_content_all(path):
    if os.path.exists(path):
        try:
            f=open(path)
        except Exception,e:
            return e
        data = f.read()
        return data        
    
