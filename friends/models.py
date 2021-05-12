from django.db import models
from django.contrib.auth.models import User
from pictures.models import Picture



class Friend(models.Model):

    sender = models.ForeignKey(User , related_name="following" , on_delete=models.CASCADE)
    reciver = models.ForeignKey(User , related_name="followers" , on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)



class Like(models.Model):

    user = models.ForeignKey(User , related_name="Likes" , on_delete=models.CASCADE)
    pic = models.ForeignKey(Picture , related_name="likes" , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)