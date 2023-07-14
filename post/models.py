from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.hashers import make_password,check_password
class Person(models.Model):
    person_id = models.AutoField(primary_key=True,validators=[MinValueValidator(4), MaxValueValidator(100)])
    name = models.CharField(max_length=90)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    
    
    def save(self, *args, **kwargs):
        if self.password:  # Only hash the password if it's not empty
            self.password = make_password(self.password)
        super().save(*args, **kwargs) 
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
        
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    class Meta:
        
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title


     