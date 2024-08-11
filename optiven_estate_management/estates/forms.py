# estates/forms.py

from django import forms
from .models import Property, Order

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'location', 'price', 'description', 'image']  # Correct field names
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['property', 'customer']  # Correct field names and use the existing fields
        widgets = {
            'property': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),  # Assuming you want to select an existing customer
        }
