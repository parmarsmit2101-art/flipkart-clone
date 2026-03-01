
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clothing/', include('clothing.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('electronics/', include('electronics.urls')),
]

path('', include('electronics.urls')),
