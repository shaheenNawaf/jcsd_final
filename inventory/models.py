from django.db import models

class Supplier(models.Model):    
    name= models.CharField(max_length=255) 
    address= models.CharField(max_length=255) 
    contactNum= models.CharField(max_length=255)
    email = models.CharField(max_length=255) 

    def __str__(self):
        return f"{self.name}"
    
class Inventory(models.Model):
    supplierId = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=255)
    itemType  = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.itemName}"


