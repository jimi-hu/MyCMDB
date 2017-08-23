from django.shortcuts import render, render_to_response
from install.models import installModels
from install.form import installModelsForm
import os
import shutil
from MyCMDB.project_dir import PROJECT_DIR 
from django.http.response import HttpResponse
import json
from common import readfile

def index(request):
    playbook_list=os.listdir(PROJECT_DIR+"/ansible/")
    
    return render_to_response("install.html",{"playbook_list":playbook_list})

def upload(request):
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
        if os.path.exists(server+"/"+playbook.name):
            os.remove(server+"/"+playbook.name)
        shutil.move(path+playbook.name, server)    
    return render_to_response("install.html")

def download(request):
    if request.method == "GET":
        data=readfile.file_content_all(PROJECT_DIR+"/ansible/1/1.py")
        return HttpResponse(data)    
        
        
        
        
                
        