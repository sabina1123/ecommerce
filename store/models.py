from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length= 50)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} ({self.category})"

class Customer(models.Model):
    first_name= models.CharField(max_length=20)
    middle_name= models.CharField(max_length=20, null = True, blank = True)
    last_name= models.CharField(max_length=50)
    shipping_address= models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.customer}"
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    
    def __str__(self):
        return f" Cart no {self.pk}"

    
    
class Order(models.Model):
    
    CASH_CHOICE = 'C'
    KHALTI_CHOICE= 'K'
    ESEWA_CHOICE = 'E'
    
    PAYMENT_MODE_CHOICES=[
        (CASH_CHOICE, 'CASH'),
        (KHALTI_CHOICE, 'KHALTI'),
        (ESEWA_CHOICE, 'ESEWA'),
        ]
    
    PENDING_CHOICE='P'
    CONFIRM_CHOICE='CF'
    REJECTED_CHOICE='R'
    CANCELLED_CHOICE = 'C'
    INDELIVERY_CHOICE='ID'
    DELIVERD_CHOICE='D'
    
    
    STATUS_CHOICES=[
        (PENDING_CHOICE, 'PENDING'),
        (CONFIRM_CHOICE, 'CONFIRM'),
        (REJECTED_CHOICE, 'REJECTED'),
        (CANCELLED_CHOICE, 'CANCELLED'),
        (INDELIVERY_CHOICE, 'INDELIVERY'),
        (DELIVERD_CHOICE, 'DELIVERD'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING_CHOICE)
    payment_mode = models.CharField(max_length=1, choices=PAYMENT_MODE_CHOICES)
    is_paid = models.BooleanField(default=False)
    place = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    def __str__(self):
      return f"Order No {self.pk} ({self.customer})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Order No {self.order.pk} ({self.order.customer})"
        