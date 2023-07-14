from django.urls import path
from . import views
 
 
 
urlpatterns = [
    path('gettasks/',views.getTasks),
    path('posttask/',views.CreateTask.as_view()),
]