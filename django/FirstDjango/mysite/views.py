from django.http import HttpResponse
from django.http import JsonResponse
# django.http is django moudle to handle the request and response from the browser
import json

def Home(request):
    return HttpResponse("Hello, This is Home Page")

def About(request):
    return HttpResponse("Heelo, This is About page")

def Profile(request):
    data = {
        "email":"pankaj@gmail.com",
        "password":"1234"
    }
    return JsonResponse(data)

