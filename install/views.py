#coding:utf-8
from django.shortcuts import render, render_to_response
from install.models import *
from install.form import installModelsForm
import os,tarfile,sys
import shutil
from MyCMDB.project_dir import PROJECT_DIR 
from django.http.response import HttpResponse
import json
from common import readfile
from update_job_model import *
reload(sys)
sys.setdefaultencoding('utf8')

def index(request):
    playbook_list=job_models.objects.all()
    #playbook_list=os.listdir(PROJECT_DIR+"/ansible/")
    #playbook_list.path=playbook_list.path.split("/")[-1]
    return render_to_response("install.html",{"playbook_list":playbook_list})

def upload_model(request):
    if request.method == "POST":
        playbook=request.FILES.get('playbook')
        dir_name=playbook.name.split(".")[0]
        path=PROJECT_DIR+"/ansible/"
        server=path+dir_name
        if not os.path.exists(server):
            os.mkdir(server)
        
        file=installModels()
        file.tarFile=playbook
        file.save() 
        if os.path.exists(server):
            shutil.rmtree(server)
        f=tarfile.open(os.path.join(path,playbook.name),"r:gz")
        f.extractall(path)
        f.close()
        os.remove(path+playbook.name)
        updata_job_model_info(server)
    
    return render_to_response("install.html")

def model(request,model_id):
    a=job_models.objects.get(id=model_id)
    file=os.path.join(a.path,"group_vars/all")
    f=open(file)
    var_all_file_contex="".join(f.readlines())
    f.close()
    host_file=os.path.join(a.path,"hosts")
    c=open(host_file)
    host_file_contex="".join(c.readlines())
    return render_to_response("model_job.html",{"var_all_file_contex":var_all_file_contex,"host_file_contex":host_file_contex})

def download(request):
    if request.method == "GET":
        data=readfile.file_content_all(PROJECT_DIR+"/ansible/1/1.py")
        return HttpResponse(data)    
