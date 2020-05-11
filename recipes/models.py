from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    intro = models.TextField(max_length=300, blank=True)
    ingredients = models.TextField(max_length=300, blank = True)
    directions = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
        
    def snippet(self):
        return self.intro[:50]
