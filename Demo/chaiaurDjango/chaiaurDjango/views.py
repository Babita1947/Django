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

    data = {
        "price":price,
        "perc":perc,
        "ans":ans
    }


    # return JsonResponse({
    #     "price":price,
    #     "perc":perc,
    #     "ans":ans
    # })

    return render(reqeust, 'percent.html', data)
def printFunc(request):
    return HttpResponse("<h1>Print Function</h1>")


# def fetchEmployeeData(reqest):
#     # 1. Fetch all the emplyeees from the databases
#     # 2. Fetched emplyee data ko Pass kar do employee.html (jaha par hame data render karwana hai)

#     return render("")