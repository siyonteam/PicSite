from django.contrib import admin
from .models import Friend , Like

@admin.register(Friend)
class FrinedAdmin(admin.ModelAdmin):
    list_display = ('sender' , 'reciver' , 'created')
    list_filter = ('sender' , 'reciver' , 'created')



@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user' , 'pic' , 'created')
    list_filter = ('user' , 'pic' , 'created')