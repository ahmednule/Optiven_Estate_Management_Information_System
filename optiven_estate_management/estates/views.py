from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Order
from .forms import OrderForm  # Corrected import statement

def home(request):
    return render(request, 'estates/index.html')

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'estates/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'estates/property_detail.html', {'property': property})

def order_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.property = property
            order.save()
            return redirect('property_list')  # Consider redirecting to 'property_detail' to show the newly placed order
    else:
        form = OrderForm()
    return render(request, 'estates/order_form.html', {'form': form, 'property': property})

def dashboard(request):
    orders = Order.objects.all()
    return render(request, 'estates/dashboard.html', {'orders': orders})
