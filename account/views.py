from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from account.models import models

from account.models import Customer, Order, Product


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customer = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_customer': total_customer, 'pending': pending,
               'delivered': delivered, 'total_orders': total_orders}
    return render(request, 'dashboard.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


def customer(request, pk):
    customers = Customer.objects.get(id=pk)

    orders = customers.order_set.all()

    context = {'customers':customers, 'orders':orders}
    return render(request, 'customer.html', context)
