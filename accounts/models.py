from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    GENDER = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name="profile")
    age = models.PositiveSmallIntegerField(null=True , blank=True)
    gender = models.CharField(max_length=100 , choices=GENDER , null=True , blank=True)
    phone_number = models.BigIntegerField(null=True , blank=True)
    bio = models.TextField(null=True , blank=True)
    avtar = models.ImageField(upload_to='avatars', default='avatars/cover.png' , null=True , blank=True)
