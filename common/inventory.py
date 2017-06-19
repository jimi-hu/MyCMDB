#coding:utf-8
'''
Created on 2017年6月3日

@author: hujie
'''
import time
import random
import ansible.runner
import os

class  inventory():
    def __init__(self,hosts=[],module_name="",module_args=""):
        self.hosts=hosts
        self.item=""
        self.inventory_file=""
        self.module_name=module_name
        self.module_args=module_args
    
    def file_name(self):
        rand=int(time.mktime(time.localtime())+random.randrange(1,100))
        self.inventory_file="inventory"+str(rand)
        return self.inventory_file
                    
    def analysis(self):
        filename=self.file_name()
        f=open(filename,"w")
        for host in self.hosts:
            try:
                ssh_port=host["port"]
                remote_user=host["username"]        
                remote_passwd=host["passwd"]
                ssh_ip=host["ip"]
            except Exception,e:
                print Exception,":",e
            line="%s ansible_ssh_port=%s ansible_ssh_user=%s ansible_ssh_pass=%s\n"%(ssh_ip,ssh_port,remote_user,remote_passwd)
            f.write(line)
        f.close()
    
    def run(self):
        runner=ansible.runner.Runner(host_list=self.inventory_file,module_name=self.module_name,module_args=self.module_args)
        try:
            result=runner.run()
        except Exception,e:
            result=0
        os.remove(self.inventory_file)
        return result
        
        
    