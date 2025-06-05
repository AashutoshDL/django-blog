from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now) #placing () after the now function would execute the function here which we dont want to do as we need different timings
    author=models.ForeignKey(User, on_delete=models.CASCADE) #tells django that deleting the user deletes their blogs

    def __str__(self):
        return self.title