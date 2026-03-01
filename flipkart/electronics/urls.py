from django.urls import path
from . import views

urlpatterns = [
    path('', views.electronics, name='electronics'),
    path('', views.electronics_home, name='electronics_home'),
    path('add/', views.add_product, name='add_product'),
    path('electronics/', views.electronics),
    path('clothing/', views.clothing),
]

