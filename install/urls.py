#coding:utf-8
'''
Created on 2017年6月17日

@author: hujie
'''
from django.conf.urls import url
from install import  views
 
urlpatterns = [
    url(r'^index/',views.index),
    url(r'^upload/',views.upload),
    url(r'^download/',views.download),
]


