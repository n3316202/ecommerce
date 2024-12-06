from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls'),name='home'),
    path("home/", include('home.urls')),
    path("boards/", include('boards.urls')),
    path('account/', include('accounts.urls')),
]
