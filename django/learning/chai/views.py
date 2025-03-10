from django.shortcuts import render
from .models import CharVarity
# Create your views here.
def chai(request):
    chais = CharVarity.objects.all()
    return render(request , 'chai/all_chai.html' , {'chais' : chais})