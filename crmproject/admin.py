from django.contrib import admin
from django.contrib.auth import get_user_model
from crmproject.models import *
Users = get_user_model()
admin.site.site_header = "CRM PROJECT"
admin.site.site_title = "CRM PROJECT"

class InlineItem(admin.TabularInline):
    model = Item   

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
    inlines = [InlineItem,]
    list_display = [
        "address",
        "cost",
        "user"
    ]


class ItemAdmin(admin.ModelAdmin):

    list_display = [
        "order",
        "product",
        "quantity",
        "price"
    ]


    def price(self, obj):
        return f'{obj.product.price}$'

admin.site.register(User,UserDetails)
admin.site.register(Address,AddressDetails)
admin.site.register(Order,OrderDetails)
admin.site.register(Product,ProductDetails)
admin.site.register(Category)
admin.site.register(Item, ItemAdmin)