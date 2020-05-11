from django import forms
from . import models

# Create your views here.
class CreateExercise(forms.ModelForm):
    class Meta:
        model = models.Exercise
        fields = ['title','slug','intro','body','thumb']

