from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(null = True, max_length=100)
    email = models.CharField(null = True, max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(null = True, max_length=100)
    price = models.FloatField()
    mrp = models.FloatField(null = True)
    image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ' '
        return url

    @property
    def percentile(self):
        percentage = 100 - ((self.price/self.mrp)*100)
        return str(percentage)
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True, blank = True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null = True, blank=False)
    transaction_id = models.CharField(null = True, max_length=100)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.order_item_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.order_item_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class Order_Item(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True, blank = True)
    quantity = models.IntegerField(default=0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.Product.price * self.quantity
        return total
    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True, blank = True)
    address = models.CharField(null = True, max_length=100)
    city = models.CharField(null = True, max_length=100)
    state = models.CharField(null = True, max_length=100)
    zipcode = models.CharField(null = True, max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
