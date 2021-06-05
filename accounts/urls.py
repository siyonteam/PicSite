from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ProfileView , login_user , user_register , user_change_password , edit_profile , user_logout


app_name = "accounts"
urlpatterns = [
    path('login/' , login_user , name="login"),
    path('register/' , user_register , name="register"),
    path('logout/' , user_logout , name="logout"),
    path('password/change/', user_change_password , name="change_password"),
    path('<username>/',ProfileView.as_view(),name ="profile"),
    path('<username>/edit/',edit_profile,name ="edit_profile"),
]