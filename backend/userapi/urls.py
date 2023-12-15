from django.urls import path
from userapi import views

urlpatterns = [
    path('register/', views.user_registration_view, name='user-registration'),
    path('login/', views.user_login_view, name='user-login'),
    path('profile/', views.user_profile_view, name='user-profile'),
    path('change-password/', views.user_change_password_view, name='user-change-password'),
    path('logout/', views.user_logout_view, name='user-logout'),
]
