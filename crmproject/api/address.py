from typing import List
from crmproject.models import *
from ninja import Router
from crmproject.schema import *

address_router = Router(tags=["address endpoints"])


@address_router.get('/address',response=List[AddressOut])
def address(request):
    return Address.objects.all()


@address_router.get('/address/{id}', response=AddressOut)
def address(request, id:int):
    return Address.objects.get(id = id)

@address_router.post('/addressin',response=MessageOut)
def address(request, payload: AddressIn):
    Address.objects.create(name = payload.name,
    address1 = payload.address1,
    address2 = payload.address2,
    phone = payload.phone,
    user_id = payload.user_id)
    return {"message": "address created successfully!"}

@address_router.put('/addressupdate',response=MessageOut)
def address(request,id:int,payload: AddressIn):
    Address.objects.filter(id = id).update(
    name = payload.name,
    address1 = payload.address1,
    address2 = payload.address2,
    phone = payload.phone,
    user_id = payload.user_id)
    return {"message":"address updated successfully!"}

@address_router.delete('/addressdel',response=MessageOut)
def address(request,id:int):
    Address.objects.filter(id = id).delete()
    return {"message":"address delete successfully!"}

    
    