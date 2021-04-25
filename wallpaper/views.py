from django.shortcuts import render
from .models import Wallpaper


def home(request):
    images = Wallpaper.objects.all()
    context = {
        'images':images,
    }
    return render(request,'wallpaper/picture.html',context)
