from django.shortcuts import render, redirect
from .models import Exercise
from django.http import HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/exercise_list.html', {'exercises':exercises})

def exercise_detail(request, slug):
    exercise = Exercise.objects.get(slug=slug)
    return render(request, 'exercises/exercise_detail.html', {'exercise':exercise})

@login_required(login_url="/accounts/login/")
def exercise_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = forms.CreateExercise(request.POST, request.FILES)
        # create a form instance and populate it with data from the request:
        if form.is_valid():
            #process data and return to exercise list
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('exercises:list')
    else:
        form = forms.CreateExercise()
        return render(request,'exercises/exercise_create.html',{'form':form})
