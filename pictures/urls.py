from django.urls import path
from .views import home , picture_detail , add_picture , edit_picture

app_name = "pictures"
urlpatterns = [
    path('',home , name="home"),
    path('pictures/categories/<slug:category_slug>/',home , name="category"),
    path('pictures/<int:pk>/',picture_detail , name="picture_detail"),
    path('pictures/<int:pk>/edit/',edit_picture , name='edot_picture'),
    path('pictures/add/',add_picture , name="add_picture"),
    
]
