from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from keci.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'abstract', 'language', 'current_stage', 'branches', 'authors', 'document']

LANGUAGE_CHOICES = (
    ('Türkçe','Turkish'),
    ('English','English'),
)
STAGE_CHOICES = (
    ('Bitti','Bitti'),
)
BRANCH_CHOICES = (
    ('Teknik','Teknik'),
    ('Dil','Dil'),
)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    abstract = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    current_stage = forms.ChoiceField(choices=STAGE_CHOICES)
    branches = forms.ChoiceField(choices=BRANCH_CHOICES)
    authors = forms.CharField(widget=forms.Textarea)
    document = forms.FileField()
    #def __init__(self,*args,**kwargs):
        #self.title = kwargs.pop('aa')
        #super(UploadFileForm,self).__init__(*args,**kwargs)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


