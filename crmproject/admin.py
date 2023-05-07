from django.contrib import admin

from crmproject.models import *

class AddressDetails(admin.ModelAdmin):
    list_display = [
        "name",
        "phone",
        "user"
    ]  

class UserDetails(admin.ModelAdmin):
    list_display = [
        "name",
        "phone",
        "email"
    ]

class ProductDetails(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "quantity"
    ]
class OrderDetails(admin.ModelAdmin):
    list_display = [
        "address",
        "cost",
        "products",
        "user"
    ]
    
admin.site.register(User,UserDetails)
admin.site.register(Address,AddressDetails)
admin.site.register(Order,OrderDetails)
admin.site.register(Product,ProductDetails)
