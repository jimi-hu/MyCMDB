from django.shortcuts import render_to_response, redirect
from models import Hosts
from form import HostsForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from common import inventory
from MyCMDB.project_dir import  PROJECT_DIR
import json

# Create your views here.
def del_host(request):
    if request.method == "POST":
        del_ip=request.POST.get("delhost")
        Hosts.objects.filter(ip=del_ip).delete()
    return redirect("/hosts/hostlist/")


def host_list(request,current_page):
    if request.method == "POST":
        checkform=HostsForm(request.POST)
        checkform["passwd"].value()
        if checkform.is_valid():
            passwd=checkform["passwd"].value()
            username=checkform["username"].value()
            port=checkform["port"].value()
            ip=checkform["ip"].value()
            hosts=[{"ip":ip,"username":username,"passwd":passwd,"port":port}]
            inventorys=inventory.inventory(hosts,module_name="script",module_args=PROJECT_DIR+"/scripts/sys_info.sh")
            inventorys.analysis()
            result=inventorys.run()
            checkform.save()
            try:
                rc=result["contacted"][ip]["rc"]
            except Exception,e:
                rc=1
                
            if (rc==0):
                res=json.loads(result["contacted"][ip]["stdout"])
                mem=res["mem"]
                cpu=res["cpu"]
                hostname=res["hostname"]
                Hosts.objects.filter(ip=ip).update(state="ok",mem=mem,cpu=cpu,hostname=hostname)
            else:
                Hosts.objects.filter(ip=ip).update(state="ERROR")
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

