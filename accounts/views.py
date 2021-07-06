from django.core.paginator import Paginator
from django.forms.widgets import RadioSelect
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404 , render , redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , update_session_auth_hash , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy , reverse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required , ajax_login_required
from friends.models import Friend
from .models import Profile
from .forms import LoginForm , UserRegistrationForm , ChangePasswordForm , UserEditForm , ProfileEditForm





def profile(request , username):
    user = get_object_or_404(User, username=username)
    pics = user.pics.all()
    paginator = Paginator(pics , 8)

    page = request.GET.get('page')
    if page and request.is_ajax() :
        page_obj = paginator.get_page(page)
        return render(request , 'accounts/include/profile_pics.html' , {'pics':page_obj,})
    else:
        profilee =user.profile
        page_obj = paginator.get_page(1)
        context = {
            'user':user,
            'profile':profilee,
            'pics':page_obj,
        }
        if request.user != user :
            if request.user.is_authenticated :
                is_follow = "follow"
                relation = Friend.objects.filter(sender=request.user , reciver=user)
                if relation.exists():
                    is_follow="unfollow"
                context['is_follow']=is_follow
            
            else:

                context['is_follow']="follow"


        return render(request , 'accounts/profile.html' , context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid() and request.is_ajax():
            cd = form.cleaned_data
            user = authenticate(request , username = cd["username"] , password = cd["password"])
            if user is not None :
                login(request , user)
                response = {
                    "status":"1",
                    "message":"با موفقیت وارد شدید",
                    "url":request.build_absolute_uri(reverse('accounts:profile' , kwargs={'username':user.username}))
                }
                #return redirect("accounts:profile" , user.username)
            else:
                response = {
                    "status":"0",
                    "message":"رمز عبور یا نام کابری اشتباه است",
                }
            return JsonResponse(response)
    
    
    form = LoginForm()  
    return render(request , "accounts/logReg.html",{"form":form , 'title':'login'})
        
    
def user_register(request):
    if request.method == "POST" and request.is_ajax():
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save()
            login(request , user , backend='django.contrib.auth.backends.ModelBackend')
            response = {
                "status":"1",
                "message":"با موفقیت وارد شدید",
                "url":request.build_absolute_uri(reverse('accounts:profile' , kwargs={'username':user.username}))
            }

        else :
            response = {
                "status":"0",
                "message":form.errors.as_text(),
            }
        return JsonResponse(response)
        
            
    else :
        form = UserRegistrationForm()

    return render(request , 'accounts/logReg.html' , {"form":form,'title':'register'})

@login_required
def user_logout(request):
    logout(request)
    return redirect("pictures:home")

@login_required
def user_change_password(request):
    if request.method == "POST":
        user = request.user
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if user.check_password(cd["old_password"]):
                user.set_password(cd["password1"])
                user.save()
                update_session_auth_hash(request , user)
                return redirect("accounts:profile" , user.username)

    else:
        form = ChangePasswordForm()

    return render(request , 'accounts/login.html' , {"form":form})


@login_required
def edit_profile(request , username):
    user = get_object_or_404(User , username=username)
    if user == request.user:
        if request.method == "POST":
            form1 = UserEditForm(data=request.POST , files=request.FILES,instance=user)
            form2 = ProfileEditForm(data=request.POST , files=request.FILES,instance=user.profile)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                return redirect('accounts:profile',user.username)
        else:
            form1 = UserEditForm(instance=user)
            form2 = ProfileEditForm(instance=user.profile)

        context = {
            "form1":form1,
            "form2":form2
        }

        return render(request , 'accounts/edit_profile.html',context)


class UserPassReset(auth_views.PasswordResetView):
	template_name = 'accounts/password_reset.html'
	success_url = reverse_lazy('accounts:password_reset_done')
	email_template_name = 'accounts/password_reset_email.html'

class PasswordResetDone(auth_views.PasswordResetDoneView):
	template_name = 'accounts/password_reset_done.html'

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
	template_name = 'accounts/password_reset_confirm.html'
	success_url = reverse_lazy('accounts:password_reset_complete')

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
	template_name = 'accounts/password_reset_complete.html'
    
    
@require_POST
@ajax_required
@ajax_login_required
def follow_user(request):

    sender_id = request.POST.get('sender')
    reciver_id = request.POST.get('reciver')
    
    sender =get_object_or_404(User, id=sender_id)
    
    reciver = get_object_or_404(User , id=reciver_id)

    relation = Friend.objects.filter(sender=sender , reciver=reciver)
    if relation.exists():
        relation[0].delete()
        is_follow = False
        #return JsonResponse({'isFollow':False})
    else :
        relation = Friend(sender=sender , reciver=reciver)
        relation.save()
        is_follow = True
        #return JsonResponse({'isFollow':True})
    followers = reciver.followers.all().count()
    context = {
        "isFollow": is_follow,
        "followers" : followers
    }
    return JsonResponse(context)

def test(request):
    return render(request,'accounts/logReg.html',{})
