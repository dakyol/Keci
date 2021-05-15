from django import forms
from django.forms import ModelForm

from keci.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'abstract', 'language', 'current_stage', 'branches', 'authors', 'document']

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    #def __init__(self,*args,**kwargs):
        #self.title = kwargs.pop('aa')
        #super(UploadFileForm,self).__init__(*args,**kwargs)



