from django import forms
from .models import Property, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Corrected line
        self.helper = FormHelper()
        self.helper.form_method = 'post'  # Fixed attribute name
        self.helper.add_input(Submit('submit', 'Sign Up'))
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
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )

    class Meta:
        model = Order
        fields = ['property', 'phone']  # Including the new fields
        widgets = {
            'property': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True, user=None):
        order = super().save(commit=False)
        if user is not None:
            order.customer = user  
        if commit:
            order.save()
        return order
