from __future__ import unicode_literals

from django.db import models
from MyCMDB.project_dir import  PROJECT_DIR
import datetime
# Create your models here.

class installModels(models.Model):
    tarFile=models.FileField(upload_to="./ansible/")
    class Meta():
        db_table="installModels"

class job_models(models.Model):
    path=models.CharField(max_length=100)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    creater=models.CharField(max_length=100)
    class Meta():
        db_table="model_list_info"
