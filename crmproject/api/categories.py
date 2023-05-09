from typing import List
from crmproject.models import *
from ninja import Router
from crmproject.schema import *

categories_router = Router(tags=["category endpoints"])


@categories_router.get("/cat", response=List[CategoryOut])
def cat(request):
    categories = Category.objects.all()
    return categories

@categories_router.get("getcatbyid", response=CategoryOut)
def cat(request, id:int):
    return Category.objects.get(id = id)