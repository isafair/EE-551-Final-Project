from django.http import HttpResponse
from django.shortcuts import render
from recipes import views as recipe_views
from exercises import views as exercise_views
from recipes.views import recipe_list
from exercises.views import exercise_list
from django.views.generic import TemplateView
from recipes.models import Recipe
from exercises.models import Exercise


def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')
    
 
 
 
