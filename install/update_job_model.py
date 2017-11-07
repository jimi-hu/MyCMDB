from install.models import job_models
import time

def updata_job_model_info(model_path):
    TIME=time.strftime("%Y-%m-%d %X", time.localtime())
    if job_models.objects.filter(path=model_path):
        job_models.objects.filter(path=model_path).update(path=model_path,update_time=TIME)
    else:
        job_new=job_models()
        job_new.path=model_path
       #job_new.create_time=TIME
       #job_new.update_time=TIME
        job_new.save()
    
