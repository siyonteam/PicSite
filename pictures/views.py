from django.core import paginator
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.text import slugify
from friends.models import Like
from common.decorators import ajax_required , ajax_login_required
from .models import Picture , Category
from .forms import AddPictureForm

# home page view 
def home(request , category_slug=None):
    all_pics = Picture.objects.all()
    
    # category view
    if category_slug:
        category = get_object_or_404(Category , slug=category_slug)
        all_pics = all_pics.filter(category = category)

    paginator = Paginator(all_pics , 19)
    page = request.GET.get("page")

    try :
        pics = paginator.page(page)
    # if error is page not found view get the page 1
    except PageNotAnInteger:
        pics = paginator.page(1)

    
    except EmptyPage:
        # if reguest id ajax return empty data 
        if request.is_ajax() : 
            return HttpResponse('')

        # if error is page not found view get the last page
        pics = paginator.page(paginator.num_pages)
  
    context = {
        'pics':pics,
    }
    # if request id ajax append renderd list_ajax.html to the home.html
    if request.is_ajax() :
        return render(request , 'pictures/include/list_ajax.html' , context)

    # render home.html 
    return render(request,'pictures/home.html',context)

@ajax_required
def picture_detail(request , pk):
    try :
        pic = get_object_or_404(Picture , pk = pk)
    except :
        return HttpResponse(" Picture not found ")
    
    user = pic.user
    similar_pics = pic.tags.similar_objects()[:10]
    is_liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(user = request.user , pic = pic)

        if liked.exists():
            is_liked = True
    conetxt = {
        "pic": pic,
        "user": user,
        "similar_pics" : similar_pics,
        'is_liked' : is_liked
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


@require_POST
@ajax_required
@ajax_login_required
def like(request):
    # picid == picture id
    picid = request.POST.get('id')
    pic = get_object_or_404(Picture , id=picid)
    user = request.user
    like =Like.objects.filter(pic=pic , user=user)

    if like.exists():
        like = Like.objects.get(pic=pic , user=user)
        like.delete()
        return JsonResponse({"isLike":False})
    else :
        like = Like(pic=pic , user=user)
        like.save()
        return JsonResponse({"isLike":True})
    
def catalog(request):
    cats = Category.objects.all()
    return render(request , 'pictures/categories.html' , {'cats':cats})