from django import  forms
from .models import Filmproject

class FilmprojectForm(forms.ModelForm):
     class Meta:
         model=Filmproject
         fields = ['name','desc','year','img']