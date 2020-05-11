from django import forms
from . import models

# Create your views here.
class CreateRecipe(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title','slug','intro','ingredients','directions','thumb']
