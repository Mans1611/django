from django.shortcuts import render
from .models import Post,Person
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.http import HttpResponse 
from .forms  import DemoForms 
from django.http import JsonResponse
from .serializer import Postserializer,PersonSerializer,PersonSerializerbgd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import jwt, datetime
from django.views import View 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

@api_view(['GET','POST'])
def form_view(request):
    
    if request.method == 'GET':
        posts = Post.objects.all()
        serilizear = Postserializer(posts,many = True)
        return JsonResponse(serilizear.data,safe=False)
    if request.method == 'POST':
        serilizear = Postserializer(data=request.data)
        
        if serilizear.is_valid():
            serilizear.save()
            return Response(serilizear.data,status= status.HTTP_201_CREATED)
    
                

    
# @api_view(['GET'])    
# def getPerson(request):
#     if request.method == 'GET':
#         persons = Person.objects.all()
#         serilizar = PersonSerializer(persons,many=True)
#         return Response(data=serilizar.data,status=status.HTTP_200_OK)



class CreatePerson(APIView):
    
    def get(self,request,id):
        person = Person.objects.get(person_id=id)
        serilizer = PersonSerializerbgd(person,many=False)
        response = Response(data=serilizer.data,status=status.HTTP_200_OK)
        response.accepted_render = JSONRenderer()
        return response
    
    
@api_view(['POST'])
def createPerson(request):    
        serilizar = PersonSerializer(data=request.data)
        if serilizar.is_valid():
            serilizar.save()
            return Response(data=serilizar.data,status=status.HTTP_201_CREATED)
        return  Response(data={'err':'an error occured'},status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def signIn(request):
    person = Person.objects.get(name=request.data['name'])
    checkPasswrd = person.check_password(request.data['password'])
    if checkPasswrd:
        return Response(data={'sucess':'password matches'},status=status.HTTP_200_OK)
    payload = {
        'id' : person.pk,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat' : datetime.datetime.utcnow() 
    }
    token = jwt.encode(payload,'secret',algorithm='HS256')
    print(token)
    
    response = Response(data={'fail':'Failling'},status=status.HTTP_401_UNAUTHORIZED)
    response.set_cookie(value=token,key='jwttoken',secure=True)
    
    return response
class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwttoken')
        if token is None:
            return Response(data = { 'msg':'Token is Not Found'})
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
        person = Person.objects.get(pk=payload['id'])
        serilizar = PersonSerializer(person)
        return Response(serilizar.data)
         
@api_view(['GET','PUT','DELETE'])       
def post_details(request,id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        seriliziar = Postserializer(post)
        return JsonResponse(seriliziar.data)
    elif request.method == 'PUT':
        seriliziar = Postserializer(post, data=request.data)
        if seriliziar.is_valid():
            seriliziar.save()
            return Response(seriliziar.data,status=status.HTTP_202_ACCEPTED)
        return Response(seriliziar.data,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response("Deleted sucussfully",status=status.HTTP_200_OK)
    