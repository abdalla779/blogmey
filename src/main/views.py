from django.shortcuts import render
from .models import Blog
from .models import Info

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    info = Info.objects.first()
    return render(request,'blog.html',{'blogs':blogs,'info':info})

def contact(request):
    info = Info.objects.first()
    return render(request,'contact.html',{'info':info})


def about(request):
    info = Info.objects.first()
    return render(request,'about.html',{'info':info})
