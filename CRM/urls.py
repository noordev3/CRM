from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from crmproject.api.user import *
from crmproject.api.address import *
from crmproject.api.categories import *
from crmproject.api.product import *
from crmproject.api.order import *

api = NinjaAPI(title="CRM Project")

api.add_router("/users",user_router)
api.add_router("/addresses",address_router)
api.add_router("/cat",categories_router)
api.add_router("/prod",products_router)
api.add_router("order",order_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
