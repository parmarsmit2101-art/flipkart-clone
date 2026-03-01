from django.urls import path
from clothing import views


urlpatterns = [
 path('', views.clothing, name='clothing'),
 path("", views.home, name = "home"),
]