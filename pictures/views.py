from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Picture , Category
from .forms import AddPictureForm


def home(request , category_slug=None):
    all_pics = Picture.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category , slug=category_slug)
        all_pics = all_pics.filter(category = category)

    paginator = Paginator(all_pics , 19)
    page = request.GET.get("page")

    try :
        pics = paginator.page(page)
    except PageNotAnInteger:
        pics = paginator.page(1)
    except EmptyPage:
        if request.is_ajax() : 
            return HttpResponse('')
        pics = paginator.page(paginator.num_pages)
  
    context = {
        'pics':pics,
    }

    if request.is_ajax() :
        return render(request , 'pictures/include/list_ajax.html' , context)

    return render(request,'pictures/home.html',context)


def picture_detail(request , pk):
    pic = get_object_or_404(Picture , pk = pk)
    user = pic.user
    similar_pics = pic.tags.similar_objects()[:10]

    conetxt = {
        "pic": pic,
        "user": user,
        "similar_pics" : similar_pics,
    }

    return render(request , 'pictures/picture_detail.html',conetxt)


@login_required
def add_picture(request):
    if request.method == "POST":
        user = request.user
        form = AddPictureForm(data=request.POST , files=request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = user
            pic.slug = slugify(pic.title)
            pic.save()
            return redirect("pictures:home")


    else:
        form = AddPictureForm()
    return render(request , 'pictures/form.html',{"form":form})


@login_required
def edit_picture(request, pk):
    pic = get_object_or_404(Picture , pk=pk)
    if pic.user== request.user :
        if request.method == "POST":
            form = AddPictureForm(data=request.POST , files=request.FILES , instance=pic)
            if form.is_valid():
                pic = form.save(commit=False)
                pic.slug = slugify(pic.title)
                pic.save()
                return redirect("pictures:picture_detail",pk)


        else:
            form = AddPictureForm(instance=pic)
        return render(request , 'pictures/form.html',{"form":form})

    else:
        raise Http404("access denied")