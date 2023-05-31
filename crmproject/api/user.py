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

@user_router.get('register')
def users(request, name: str ,password: str ,email:  str,city: str ,gender: str):
    user = User.objects.create(name = name, password = password, email = email, city=city, gender=gender)
    
    if user:
        return {
            "id": user.id
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

@user_router.get("/login")
def users(request, username: str, password: str):
    name = User.objects.filter(name = username, password = password)

    if name:
        return {"id": name.first().id}
    else:
        return {"message": "user not found"}

@user_router.put("/updatepassword", response=MessageOut)
def change(request, id:int, oldpass:str, newpass:str,confirmpass:str):
    User.objects.filter(id=id)
    if str(User.objects.filter(password=oldpass).exists()) == 'False':
        return {"message":"old password is incorrect"}
    if newpass == oldpass:
        return {"message":"new password is incorrect"}
    if confirmpass != newpass:
        return {"message":"confirm and new must be the same"}
    User.objects.update(password = newpass)
    return {"message": "password changed successfully"}
    