from django.db import models

class User(models.Model):
    name = models.CharField('name',max_length=255,blank=False,null=False)
    email = models.EmailField('email',null=False,blank=False)
    password = models.CharField('password',max_length=36,null=False,blank=False)
    phone = models.CharField('phone',max_length=32,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Address(models.Model):
    name = models.CharField('name',max_length=255,blank=False,null=False)
    address1 = models.CharField('address1',max_length=255,blank=False,null=False)
    address2 = models.CharField('address2',max_length=255,null=False,blank=False)
    phone = models.CharField('phone',max_length=32,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField('name',max_length=255,blank=False,null=False)
    price = models.FloatField('price',null=False,blank=False)
    quantity = models.IntegerField('quantity',null=True,blank=True)
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    cost = models.FloatField('cost',null=False,blank=False)
    # product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    quantity = models.IntegerField("quantity", null=True, blank=True, default=0)
    products = models.JSONField("products",default=[])
    
    def __str__(self):
        return str(self.user)
    