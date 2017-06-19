from __future__ import unicode_literals

from django.db import models

# Create your models here.

class installModels(models.Model):
    tarFile=models.FileField(upload_to="./")
    class Meta():
        db_table="installModels"