from django import forms
from .models import Picture


class AddPictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ('title','pic','description','category','tags')

