#coding:utf-8
'''
Created on 2017年6月3日

@author: hujie
'''
import ansible.runner


class hostInfo():
    def __init__(self,port,password,username):
        self.port=port
        self.password=password
        self.username=username
        