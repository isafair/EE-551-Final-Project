from django.shortcuts import render, redirect
from recipes.models import Recipe
from exercises.models import Exercise
from django.http import HttpResponse



# Create your views here.


def home_list(request):
    recipes = Recipe.objects.all().order_by('date')
    exercises = Exercise.objects.all().order_by('date')
    return render(request, 'home/home_list.html', {'recipes':recipes, 'exercises':exercises})
    
