from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'qty', 'price', 'category',]
    
@admin.register(Customer)
class  CustomerAdmin(admin.ModelAdmin):
    list_display=['id', 'first_name','middle_name', 'last_name', 'shipping_address','user',]
    

class CartItemInline(admin.TabularInline):
    model = CartItem
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines =(
        CartItemInline,
    )
    
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=(
        OrderItemInline,
    )
    
    