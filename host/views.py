from django.shortcuts import render_to_response, redirect
from models import Hosts
from form import HostsForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def del_host(request):
    if request.method == "POST":
        del_ip=request.POST["delhost"]
        delete=Hosts.objects.filter(ip=del_ip).delete()
    return redirect("/hosts/hostlist/")


def host_list(request,current_page):
    if request.method == "POST":
        checkform=HostsForm(request.POST)
        if checkform.is_valid():
            checkform.save()
        else:
            error=checkform.errors
            return render_to_response("host_list.html",{"error":error})
    hosts=Hosts.objects.all()
    paginator = Paginator(hosts,3)
    
    try:   
        current_data=paginator.page(current_page)
    except PageNotAnInteger:
        current_data = paginator.page(1)
    except EmptyPage:
        current_data = paginator.page(paginator.num_pages)
    
    return render_to_response("host_list.html",{"hosts":current_data})

