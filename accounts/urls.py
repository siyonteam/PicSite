from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ProfileView , login_user , user_register ,user_change_password , edit_profile , user_logout , UserPassReset , PasswordResetDone , PasswordResetConfirm , PasswordResetComplete


app_name = "accounts"
urlpatterns = [
    path('login/' , login_user , name="login"),
    path('register/' , user_register , name="register"),
    path('logout/' , user_logout , name="logout"),
    path('password/reset/' , UserPassReset.as_view() , name="password_reset"),
    path('password/reset/done/' , PasswordResetDone.as_view() , name = "password_reset_done"),
    path('password/reset/<uidb64>/<token>/' , PasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path('password/reset/complete/' , PasswordResetComplete.as_view() , name="password_reset_complete"),
    path('<username>/',ProfileView.as_view(),name ="profile"),
    path('<username>/edit/',edit_profile,name ="edit_profile"),
]