from django.shortcuts import render
from .models import Post 
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.http import HttpResponse 
# Create your views here.
from .forms  import DemoForms 
from django.http import JsonResponse

def form_view(request):
    form = DemoForms()
    context = {'mans':form}
    if request.method == "GET":
        data = {
            'data' : list(['mans','ahmed'])
        }
        return JsonResponse(data)
    if request.method == "POST":
        form = DemoForms(request.POST)
        if form.is_valid():
            print("Passed")
            form.save()
        
    return render(request,'home.html',context)