from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import hashlib

def response(request):
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('tiemstamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    return HttpResponse(echostr)
