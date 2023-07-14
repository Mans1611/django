from django.shortcuts import render
from .models import Book,Category
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializer import BooksSerializers,CategorySerializers
from .models import Book
from rest_framework import generics
from rest_framework.decorators import api_view
# Create your views here.

def books(request):
    if(request.method == 'GET'):
        books = Book.objects.all()
        
        
def book(request,pk):
     if(request.method == 'GET'):
        books = Book.objects.get(pk=pk)
        book = model_to_dict(books)
        return JsonResponse(book)
    
    
class BooksListView(generics.ListCreateAPIView):
    ## is to be overriden
    queryset = Book.objects.all()
    serializer_class = BooksSerializers
    
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializers
    
    
class Category (generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
@api_view(['GET','POST'])    
def books(request):
    if request.method=='GET':
        items = Book.objects.all()
        category = request.query_params.get('category')
        price = request.query_params.get('price')
        order = request.query_params.get('order')
        if category:
            items = items.filter(category__name = category)
        if price:
            items = items.filter(price__lte = price)
        if order : 
            items = items.order_by(order)
            
        arr = [1,2,3,4,5]
        print(*arr)
        serlizedItem = BooksSerializers(items,many=True)
        
        return Response(serlizedItem.data,202)
            
        
    if request.method == 'POST':
        serilizedData = BooksSerializers(data=request.data)
        serilizedData.is_valid(raise_exception=True)
        serilizedData.save()
        return Response("Done")