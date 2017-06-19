#coding:utf-8
'''
Created on 2017年6月17日

@author: hujie
'''
from django import forms
from install.models import installModels

class installModelsForm(forms.ModelForm):
    class Meta():
        model=installModels
        fields="__all__"
