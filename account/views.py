from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from account.models import models
from .forms import OrderForm

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


def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm()
    if request.method =='POST':
        #print('REQUEST METHOD',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'delete.html', context)





