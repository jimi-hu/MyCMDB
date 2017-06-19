from django.shortcuts import render, render_to_response
from install.models import installModels
from install.form import installModelsForm

# Create your views here.

def index(request):
    return render_to_response("install.html")

def upload(request):
    if request.method == "POST":
        playbook=request.FILES.get('playbook')
        playbook.name="hujie.py"
        file=installModels()
        file.tarFile=playbook 
        file.save()
    return render_to_response("install.html")

        
        