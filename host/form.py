from django import forms
from host.models import Hosts

class HostsForm(forms.ModelForm):
    class Meta():
        model=Hosts
        #fields=["ip","port","username","passwd"]
        fields="__all__"