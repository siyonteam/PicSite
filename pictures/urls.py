from django.urls import path
from .views import home , picture_detail , add_picture , edit_picture , like , catalog

app_name = "pictures"
urlpatterns = [
    path('',home , name="home"),
    path('pictures/like/' , like , name="like"),
    path('pictures/categories/<slug:category_slug>/',home , name="category_detail"),
    path('pictures/<int:pk>/',picture_detail , name="picture_detail"),
    path('pictures/<int:pk>/edit/',edit_picture , name='edit_picture'),
    path('pictures/add/',add_picture , name="add_picture"),
    path('pictures/categories/' ,catalog , name='categories')
]
