from django.core import paginator
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib.auth.models import User
from .models import Picture , Category


def home(request , category_slug=None):
    all_pics = Picture.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category , slug=category_slug)
        all_pics = all_pics.filter(category = category)

    paginator = Paginator(all_pics , 20)
    page = request.GET.get("page")

    pics = paginator.get_page(page) 

    context = {
        'pics':pics,
    }
    return render(request,'pictures/home.html',context)


def picture_detail(request , pk , slug):
    pic = get_object_or_404(Picture , pk = pk ,slug =slug)
    user = pic.user
    similar_pics = pic.tags.similar_objects()[:10]

    conetxt = {
        "pic": pic,
        "user": user,
        "similar_pics" : similar_pics,
    }

    return render(request , 'pictures/picture_detail.html',conetxt)


