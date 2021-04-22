from django.urls import path
from .views import home

app_name = "wallpaper"
urlpatterns = [
    path('',home , name="home")
]
