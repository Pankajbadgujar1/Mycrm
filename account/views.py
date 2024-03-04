from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from account.models import models
from .forms import OrderForm, CreateUserForm
from django.forms import inlineformset_factory

from account.models import Customer, Order, Product
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
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

@login_required(login_url='login')
def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


@login_required(login_url='login')
def customer(request, pk):
    customers = Customer.objects.get(id=pk)

    orders = customers.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customers': customers, 'orders': orders, 'myFilter': myFilter}
    return render(request, 'customer.html', context)


@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'), extra=10)
    customers = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset = Order.objects.none(), instance=customers)
    #form = OrderForm(initial={'customer': customers})
    if request.method =='POST':
        #print('REQUEST METHOD',request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customers)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =='POST':
        #print('REQUEST METHOD',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'delete.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            print("not login")
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')



