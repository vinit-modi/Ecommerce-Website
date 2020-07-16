from django.shortcuts import render
from .models import Customer, Product, Order, Order_Item, ShippingAddress
# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    #! IMPORTANT PART
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False) # TODO: Need to fix this 
        items = order.order_item_set.all()  # TODO: Need to fix this 
    else:
        items = []
    context = {'items':items}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

