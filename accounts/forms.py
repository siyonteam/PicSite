from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.http.response import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
import re

from django.forms import widgets
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(
        attrs={
            'placeholder':'نام کاربری / ایمیل',
            'class':'formInput'
            }
        ))
    password = forms.CharField(label="" ,widget=forms.PasswordInput(
        attrs={
            'placeholder':'رمز عبور',
            'class':'formInput'
            }
        ))

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'placeholder':'پسورد',
            'class':'formInput'
            }
        ))
    password2 = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'placeholder':'تایید پسورد',
            'class':'formInput'
            }
        ))

    class Meta:
        model = User
        fields = ('username','email')
        widgets = {
            'username':forms.TextInput(
                attrs={
                    'placeholder':'نام کاربری',
                    'class':'formInput'
                    }
                ),
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'ایمیل',
                    'class':'formInput'
                    }
                )
        }
        help_texts = {
            "username":""
        }
        labels = {
            'username':"",
            "email":""
        }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("پسورد مطابق نیست")
        return password2
      

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user





class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), label="Old Password")
    password1 = forms.CharField(widget=forms.PasswordInput(), label="New Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm New Password")


    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']

        if p1 and p2 :
            if p1 != p2:
                raise forms.ValidationError("passworf must mach")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username' , 'email','first_name' , 'last_name')

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError('username already taken')
        return username


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        