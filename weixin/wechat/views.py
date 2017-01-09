# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
import json
import hashlib

from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
import handle

import logging

TOKEN = "gyn"
APPID = "ws22b0c85f1a73954f"
SECRET = "11efa7ed3b14e9d1fa2905608ef8f015"
SECRET_MODE = False

wechat_conf = WechatConf(token=TOKEN, appid=APPID, appsecret=SECRET, encrypt_mode=SECRET_MODE)
wechat_base = WechatBasic(conf=wechat_conf)

@csrf_exempt
def response(request):
    if request.method == "GET":
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        echostr = request.GET.get('echostr', None)
        nonce = request.GET.get('nonce', None)

        if wechat_base.check_signature(signature, timestamp, nonce):
            return HttpResponse(echostr)
        else:
            return HttpResponse("error")
    else:
        xml_str = smart_str(request.body)
        response_str = handle.handle(wechat_base, xml_str)
    return HttpResponse(response_str)
