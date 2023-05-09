from typing import List
from crmproject.models import *
from ninja import Router
from crmproject.schema import *

products_router = Router(tags=["product endpoints"])

@products_router.get("/product",response= List[ProductOut])
def prod(request):
    return Product.objects.all()

@products_router.get("getproductbyid", response=ProductOut)
def prod(request, id:int):
    return Product.objects.get(id = id)