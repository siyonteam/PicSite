from django.core import paginator
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib.auth.models import User
from .models import Picture


def home(request):
    all_pics = Picture.objects.all()
    paginator = Paginator(all_pics , 1)
    page = request.GET.get("page")

    pics = paginator.get_page(page) 

    context = {
        'pics':pics,
    }
    return render(request,'pictures/home.html',context)


def picture_detail(request , pk , slug):
    pic = get_object_or_404(Picture , pk = pk ,slug =slug)
    user = pic.user

    conetxt = {
        "pic": pic,
        "user": user
    }

    return render(request , 'pictures/picture_detail.html',conetxt)


