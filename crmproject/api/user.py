from typing import List
from crmproject.models import *
from ninja import Router
from crmproject.schema import *
user_router = Router(tags=["user endpoints"])

@user_router.get('/users', response=List[UserOut])
def users(request):
    return User.objects.all()

@user_router.get('user/{id}',response=UserOut)
def users(request, id:int):
    return User.objects.get(id = id)

@user_router.post('register',response=MessageOut)
def users(request,payload: UserIn):
    User.objects.create(name = payload.name, password = payload.password, email = payload.email, phone = payload.phone)
    return {
        "message": "user created successfully!"
    }
    
@user_router.put("updateinfo",response=MessageOut)
def users(request,id: int, payload: UserIn):
    User.objects.filter(id = id).update(name = payload.name, password = payload.password, email = payload.email, phone = payload.phone)
    return {
        "message": "user updated successfully!"
    }
    
@user_router.delete("deleteuser",response=MessageOut)
def users(request,id: int):
    User.objects.filter(id = id).delete()
    return {
        "message": "user deleted successfully!"
    }