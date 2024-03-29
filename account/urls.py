
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('product/', views.product, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('dashboard/', views.dashboard),

    path('order_form/', views.createOrder, name="createOrder"),
    path('update_order/<str:pk>', views.updateOrder, name="updateOrder"),
    path('delete/<str:pk>', views.deleteOrder, name="deleteOrder"),

]

