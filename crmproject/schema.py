from typing import List
from ninja import Schema


class UserOut(Schema):
    id:     int
    name:   str
    email:  str
    phone:  str
    
class MessageOut(Schema):
    message: str
    
class UserIn(Schema):
    name:     str
    password: str
    email:    str
    phone:    str

class UserAddress(Schema):
    name : str
    
class UserAddressIn(Schema):
    id : int
    
class AddressOut(Schema):
    id : int
    name : str
    address1 : str
    address2 : str
    phone : str
    user : UserAddress
    
class AddressIn(Schema):
    name : str
    address1 : str
    address2 : str
    phone : str
    user_id : int
    
class OrderOut(Schema):
    id : int
    address : AddressOut
    cost : int
    user : UserAddress
    quantity : int
    products : List[int]