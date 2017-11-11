#coding:utf-8
'''
Created on 2017年6月17日

@author: hujie
'''
from django.conf.urls import url
from install import  views
 
urlpatterns = [
    url(r'^index/',views.index),
    url(r'^upload_molde/',views.upload_model),
    url(r'^download/',views.download),
    url(r'^(?P<model_id>\d*)',views.model),
]


