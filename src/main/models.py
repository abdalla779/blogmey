from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    created_dt = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title

class Info(models.Model):
    location = models.CharField(max_length=50)
    number = models.CharField(max_length=25)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return self.location
