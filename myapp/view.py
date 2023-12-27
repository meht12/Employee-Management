from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    if request.method=='POST':
       check=request.POST['check']
       print(check)
    return render(request,"home.html",{})

def about(request):
    return render(request,"about.html",{})

def login(request):
    return render(request,"login.html",{})
def signup(request):
    return render(request,"signup.html",{})