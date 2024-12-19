from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('store.urls')),
    path("home/", include('home.urls')),
    path("boards/", include('boards.urls')),
    path('account/', include('accounts.urls')),
    path("cart/", include('cart.urls')), 
    path("payment/", include('payment.urls')), #dev_41 settings 추가
    path('accounts/', include('allauth.urls')),#dev_46 
    path("api/", include("api.urls")),#dev_48
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
