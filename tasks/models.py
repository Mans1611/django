from django.db import models

# Create your models here.
from django.contrib.auth.hashers import make_password


class Tasks(models.Model):
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    icons = models.ImageField()
    
    def set_password(self, *args, **kwargs):   
        if self.name:
            self.name = make_password(self.name)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return self.name
    
    
class Teachers(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) :
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=90)
    code = models.CharField(max_length=90)
    teacher_id = models.ManyToManyField(Teachers)
    
    def __str__(self):
        return self.name
    