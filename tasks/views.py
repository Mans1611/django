from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serilizar import TasksSerializer,TasksSerializerName
from .models import Tasks
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
@api_view(['GET'])          # decorator for function based view.
def getTasks (request):
    tasks = Tasks.objects.all()
    serilizar = TasksSerializerName(tasks,many=True)
    return Response(data= serilizar.data,status=status.HTTP_200_OK)


class CreateTask(APIView):
    def post(self,request):
        serializer = TasksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)