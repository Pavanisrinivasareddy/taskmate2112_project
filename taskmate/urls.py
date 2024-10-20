

from django.contrib import admin # type: ignore
from django.urls import path ,include # type: ignore
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todolist_views.index,name='index'),
    
    path('todolist/',include('todolist_app.urls')),
    path('account/',include('user_app.urls')),
     path('contact',todolist_views.contact,name='Contact'),
    path('about',todolist_views.about,name='About'),
    
]
