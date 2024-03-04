
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('product/', views.product, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('dashboard/', views.dashboard),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('order_form/<str:pk>/', views.createOrder, name="createOrder"),
    path('update_order/<str:pk>/', views.updateOrder, name="updateOrder"),
    path('delete/<str:pk>', views.deleteOrder, name="deleteOrder"),

]

