from django.contrib import admin
from .models import Property, Customer, Order

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price')
    search_fields = ('title', 'location')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('property', 'customer', 'order_date')
    list_filter = ('order_date',)
    search_fields = ('property__title', 'customer__name')

admin.site.register(Property, PropertyAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
