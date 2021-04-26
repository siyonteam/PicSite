from django.urls import path
from .views import home , picture_detail

app_name = "pictures"
urlpatterns = [
    path('',home , name="home"),
    path('picture/<int:pk>/<slug:slug>/',picture_detail , name="picture_detail")
]
