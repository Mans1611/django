from django.urls import path
from . import views
 
urlpatterns = [
    path('form/',views.form_view,name='form_view'), 
    path('form/<int:id>',views.post_details),
    path('persons/<int:id>',views.CreatePerson.as_view()),   
    path('createperson/',views.createPerson),   
    path('signin/',views.signIn),   
    path('user/',views.UserView.as_view()),   
]
