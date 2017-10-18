from __future__ import unicode_literals

from django.db import models
from MyCMDB.project_dir import  PROJECT_DIR
# Create your models here.

class installModels(models.Model):
    tarFile=models.FileField(upload_to="./ansible/")
    class Meta():
        db_table="installModels"
