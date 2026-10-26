from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view1(request):
    a="Welcome to Django section"
    return HttpResponse(a)

def view2(request):
    b="Hello World"
    return HttpResponse(b)