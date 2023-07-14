from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.BooksListView.as_view(),name='book-detail'),
    path('category',views.Category.as_view()),
    path('<int:pk>',views.SingleMenuItemView.as_view()),
    path('bookcreate',views.books,name='create-book')
]
