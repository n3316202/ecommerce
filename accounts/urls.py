from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views as auth_views

from accounts import views

app_name = 'accounts'

#dev_40 이름 통일
urlpatterns = [
     #path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), 
     path('login/', views.login_user, name='login'), 
     path('logout/', views.logout_user, name='logout'),
     path('register/', views.register_user, name='signup'),
]
