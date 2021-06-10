from django import forms
from django.contrib.auth.models import User
import re
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email')
    
    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        

        if p1 and p2 :
            if p1 != p2 :
                raise forms.ValidationError('passwords must match')

            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
        # compiling regex
        pat = re.compile(reg)
        mat = re.search(pat, p2)
        if not mat :
            raise forms.ValidationError("invalid password")
        return p2






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
        