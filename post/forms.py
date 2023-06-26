from django import forms
from django.db import models 
from django.utils import timezone
from .models import Post

choices = (
    (1,"mans"),
    (2,"ahmed"),
    (3,"abdullah"),
    )
class DemoForms(forms.ModelForm):
   class Meta:
       model = Post
       fields = "__all__"
       
       
    