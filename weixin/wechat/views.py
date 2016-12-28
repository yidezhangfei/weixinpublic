from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def response(request):
    return HttpResponse("hello world")
