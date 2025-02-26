from django.urls import path
from . import views 

urlpatterns = [
   path('', views.chai, name='all_chai') 
]