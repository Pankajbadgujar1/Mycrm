
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home),
    path('product/', views.product),
    path('customer/<str:pk>', views.customer),
    path('dashboard/', views.dashboard),
]

