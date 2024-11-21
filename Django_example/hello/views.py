from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("HELLO!")
#to render entire html page
def index1(request):
     return render(request,"hello/index.html")
def likith(request):
    return HttpResponse("Hello to you")

def greet(request,name):
    return render(request,"hello/greet.html",{
        "name":name.capitalize()
    })