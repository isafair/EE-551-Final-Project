from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all().order_by('date')
    return render(request,'recipes/recipe_list.html',{'recipes':recipes})

def recipe_detail(request, slug):
    #return HttpResponse(slug)
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'recipes/recipe_detail.html', {'recipe':recipe})

@login_required(login_url="/accounts/login/")
def recipe_create(request):
    if request.method == 'POST':
        form = forms.CreateRecipe(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('recipes:list')
    else:
        form = forms.CreateRecipe()
    return render(request,'recipes/recipe_create.html',{'form':form})
