from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views as auth_views

from accounts import views

app_name = 'accounts'

urlpatterns = [
     path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), 
     path('logout/', views.logout_view, name='logout'),
     path('signup/', views.signup, name='signup'),
]
