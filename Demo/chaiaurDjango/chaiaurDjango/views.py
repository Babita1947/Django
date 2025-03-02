from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    # DB OPERATIONS
    # CALCULATION



    return render(request, 'about.html')
    # return HttpResponse("<h1> WELCOME TO ABOUT PAGE </h1>")

def contact(request):
    return HttpResponse("<h1> WELCOME TO CONTACT PAGE </h1>")

def findPercentage(reqeust):
    price=50
    perc=5

    ans=price*perc/100
    return JsonResponse({
        "price":price,
        "perc":perc,
        "ans":ans
    })
def printFunc(request):
    return HttpResponse("<h1>Print Function</h1>")