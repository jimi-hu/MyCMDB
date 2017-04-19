from django.shortcuts import render, render_to_response
from models import *
from form import HostsForm
# Create your views here.
def add_host(request):
    pass

def host_list(request):
    if request.method == "POST":
        checkform=HostsForm(request.POST)
        if checkform.is_valid():
            checkform.save()
        else:
            error=checkform.errors
            return render_to_response("host_list.html",{"error":error})
    hosts=Hosts.objects.all()
    return render_to_response("host_list.html",{"hosts":hosts})