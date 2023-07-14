from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    inventory = models.IntegerField(null=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
