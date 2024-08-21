from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Order,Customer
from .forms import OrderForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages
from django.urls import reverse
from django.http import Http404

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')  # Assuming password1 is the first password field in your form
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('property_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'estates/property_list.html', {'properties': properties})

def property_detail(request, pk):
    selected_property = get_object_or_404(Property, pk=pk)
    return render(request, 'estates/property_detail.html', {'property': selected_property})

@login_required
def order_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    customer = get_object_or_404(Customer, user=request.user) 
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.property = property
            order.customer = customer
            # order.user = request.user  # Assign the logged-in user
            order.save()
            return redirect('property_list')
    else:
        form = OrderForm()
    return render(request, 'estates/order_form.html', {'form': form, 'property': property})

def dashboard(request):
    user = request.user
    orders = Order.objects.filter(customer=user)  # Filter orders by the logged-in user
    return render(request, 'estates/dashboard.html', {'orders': orders})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return render(request, 'estates/logout.html')
