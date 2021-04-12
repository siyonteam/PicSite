from django.db import models
from django.contrib.auth.models import User



class Friend(models.Model):

    sender = models.ForeignKey(User , related_name="following" , on_delete=models.CASCADE)
    reciver = models.ForeignKey(User , related_name="followers" , on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
