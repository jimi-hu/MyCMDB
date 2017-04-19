#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hosts(models.Model):
    ip=models.GenericIPAddressField(unique=True)
    #hostname=models.CharField(max_length=32)
    #cpu=models.CharField(max_length=32)
    #mem=models.CharField(max_length=32)
    #state=models.CharField(max_length=32)
    port=models.SmallIntegerField()
    username=models.CharField(max_length=32)
    passwd=models.CharField(max_length=32)
    class Meta():
        db_table="hosts"
    def __unicode__(self):
        return "ip:%s"%(self.ip)
