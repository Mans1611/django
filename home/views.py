from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from .models import Home

    

# Create your views here.

def index(request,id):
   print("passed")
   home = Home(id,"mans's home",id,1200)
   home.save()
   
   return HttpResponse("done")
   
def mans(request):
    return HttpResponse("mans", status_code='400')