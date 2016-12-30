from django.http import HttpResponse

from wechat_sdk import WechatBasic
from wechat_sdk.messages import *

class WeChat:
    def __init__(self, wechat_basic):
        self.wechat_ = wechat_basic
        self.message = self.wechat_.message

    def parse_data(self, data):
        self.wechat_.parse_data(data)

    def auto_reply(self, text):
        self.wechat_.response_text(text, escape=False)

def handle(wechat_basic, post_data):
    wechat_obj = WeChat(wechat_basic)
    wechat_obj.parse_data(post_data)
    if isinstance(wechat_obj.message, TextMessage):
        content = wechat_obj.message.content
        if wechat_obj != None:
            wechat_obj.auto_reply(content)
    return
