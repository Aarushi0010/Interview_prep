from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("welcome to Home Page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is About page")

def contact(request):
    return HttpResponse("Let's connect!")