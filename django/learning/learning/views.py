from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to Home Page")

def about(request):
    return HttpResponse("This is About page")

def contact(request):
    return HttpResponse("Let's connect!")