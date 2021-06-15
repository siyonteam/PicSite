from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404 , render , redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , update_session_auth_hash , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .models import Profile
from .forms import LoginForm , UserRegistrationForm , ChangePasswordForm , UserEditForm , ProfileEditForm


class ProfileView(DetailView):
    model = User
    context_object_name = "usr" 
    template_name = 'accounts/profile.html'

    def get_object(self):
        return get_object_or_404(User , username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = context["usr"].profile 
        context["pics"] = context["usr"].pics
        return context


def profile(request , username):
    user = get_object_or_404(User, username=username)
    profilee =user.profile
    pics = user.pics.all()
    paginator = Paginator(pics , 8)
    context = {
        'user':user,
        'profile':profilee,
    }
    page = request.GET.get('page')
    if page :
        page_obj = paginator.get_page(page)
        context['pics']=page_obj
        return render(request , 'accounts/include/profile_pics.html' , context)
    else:
        page_obj = paginator.get_page(1)
        context['pics']=page_obj
        return render(request , 'accounts/profile.html' , context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username = cd["username"] , password = cd["password"])
            if user is not None :
                login(request , user)
                return redirect("accounts:profile" , user.username)
            else:
                messages.error(request, 'incorrect username/password')
   
    form = LoginForm()
    return render(request , "accounts/login.html",{"form":form})
        
    
def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save()
            login(request , user , backend='django.contrib.auth.backends.ModelBackend')
            return redirect("accounts:profile" , user.username)
    else :
        form = UserRegistrationForm()

    return render(request , 'accounts/register.html' , {"form":form})

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