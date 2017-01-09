# -*- coding: utf-8 -*-
import json
import requests
import traceback

import logging

class TulingRobot:
    def __init__(self, tuling_api, tuling_url):
        self.tuling_api_ = tuling_api
        self.tuling_url_ = tuling_url

    def reply(self, unicode_str):
        body = {'key':self.tuling_api_, 'info':unicode_str.encode('utf-8')}
        r = requests.post(self.tuling_url_, data=body)
        r.encode = 'utf-8'
        r_text = r.text
        logging.debug("r_text: %s", r_text)
        if r_text is None or len(r_text) == 0:
            return None
        try:
            js = json.loads(r_text)
            if js['code'] == 100000:
                logging.debug("text: %s", js['text'])
                return js['text']
            elif js['code'] == 200000:
                return js['url']
            else:
                return None
        except Exception:
            traceback.print_exc()
            return None
