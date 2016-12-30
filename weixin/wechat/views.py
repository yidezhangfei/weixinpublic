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
#        token = TOKEN
#        tmp_list = [token, timestamp, nonce]
#        tmp_list.sort()
#        tmp_str = "%s%s%s" % tuple(tmp_list)
#        tmp_str = hashlib.sha1(tmp_str).hexdigest()
#        FORMAT = '%(asctime)-15s %(signature)s%(tmp_str)s'
#        logging.basicConfig(format=FORMAT)
#        d = {'signature': signature, 'tmp_str':tmp_str}
#        logger = logging.getLogger('server')
#        logger.debug("request:", extra=d)

        if wechat_base.check_signature(signature, timestamp, nonce):
            return HttpResponse(echostr)
        else:
            return HttpResponse("error")
    else:
#        logger = logging.getLogger('server')
#        xml_str = smart_str(request.body)
#        logger.debug("xml_str:%s", xml_str)
#        request_xml = etree.fromstring(xml_str)
#        logger.debug("request_xml:%s", request_xml)
#        content = request_xml.find("Content").text
#        response_str = content
#        logger.debug("response_str:%s", response_str)
        xml_str = smart_str(request.body)
        handle.handle(wechat_base, xml_str)
    return
