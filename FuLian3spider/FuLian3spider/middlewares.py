# -*- coding: utf-8 -*-
from FuLian3spider.settings import USER_AGENT as headers
import requests,random,time

class requestsmiddlewares():
    def start_requests(self,request, spider):
        header = random.choice(headers)
        request.headers['User-Agent'] = header

# 开启代理池
class Pool():
    def get_proxy(self):
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            return None

        def get_random_proxy(self):
            '''随机从文件中读取proxy'''
            while 1:
                with open('response.text', 'r') as f:
                    proxies = f.readlines()
                if proxies:
                    break
                else:
                    time.sleep(1)
            proxy = random.choice(proxies).strip()
            return proxy