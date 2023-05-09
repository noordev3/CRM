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

@order_router.post("/order", response=MessageOut)
def order(request, payload: OrderIn):
    Order.objects.create(address_id = payload.address_id,
    cost = payload.cost,
    user_id = payload.user_id,
    quantity = payload.quantity)
    return {"message": "order created successfully"}