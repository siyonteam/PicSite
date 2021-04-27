from django.urls import path
from .views import home , picture_detail

app_name = "pictures"
urlpatterns = [
    path('',home , name="home"),
    path('pictures/categories/<slug:category_slug>/',home , name="category"),
    path('pictures/<int:pk>/<slug:slug>/',picture_detail , name="picture_detail"),
    
]
