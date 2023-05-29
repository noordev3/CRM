from typing import List
from crmproject.models import *
from ninja import Router
from crmproject.schema import *

order_router = Router(tags=["order endpoints"])

@order_router.get("/order", response=List[OrderOut])
def order(request):
    return Order.objects.all()

@order_router.get("orderbyid", response=OrderOut)
def order(request, id:int):
    return Order.objects.get(id = id)

@order_router.get("/orderCheck", response=MessageOut)
def order(request, user_id: int, cost: float, quantity: int):
    user = User.objects.get(id = user_id)
    address, _ = Address.objects.get_or_create(name=user.city, user=user)
    print(address, user)
    print("order", Order.objects.create(address = address, cost = cost, user = user, quantity = quantity))
    return {"message": "order created successfully"}