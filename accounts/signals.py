from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User


@receiver(post_save , sender=User)
def save_profile(sender , instance , created , **kwargs):
    if created :
        profile = Profile(user = instance)
        profile.save()