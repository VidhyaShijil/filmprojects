from django import  forms
from .models import Addmovie
from .models import Review


class AddmovieForm(forms.ModelForm):
     class Meta:
         model=Addmovie
         fields = ['name','desc','year','img']
         
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['description', 'stars']         