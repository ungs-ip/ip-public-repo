from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nasa_image_gallery.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]