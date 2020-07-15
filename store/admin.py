from django.contrib import admin
from .models import Customer, Product, Order, Order_Item, ShippingAddress
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(ShippingAddress)