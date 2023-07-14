

from django.contrib import admin
from django.urls import path,include
from home import views
from post import views

urlpatterns = [
    path('mans/', include('home.urls')),
    path('post/',include('post.urls')),
    path('tasks/',include('tasks.urls')),
    path('books/',include('book.urls')),
    path('__debug__/',include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'app.views.handler404'
