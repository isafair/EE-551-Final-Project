from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Exercise(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    intro = models.CharField(max_length = 200)
    body = models.TextField()
    date = models.DateTimeField(auto_now = True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def snippet(self):
        return self.intro[:50]
