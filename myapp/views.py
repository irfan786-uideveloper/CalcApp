from unittest import result
from django.shortcuts import render

# Create your views here.

def calc(request):

    return render(request,"calc.html")

def add(request):

    val1=int(request.POST['num1'])

    val2=int(request.POST['num2'])

    result=val1+val2

    multiply=val1*val2

    division=val1/val2

    subtraction=val1-val2

    return render(request,"result.html",{'sub':subtraction,'div':division,'multiply':multiply,'result':result})