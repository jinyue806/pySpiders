from Chinaarea.settings import USER_AGENTS as ua_list
import random

# class UserAgentMiddleware(object):
#     """
#         给每一个请求随机切换一个User-Agent
#     """
#     def process_request(self, request, spider):
#         user_agent = random.choice(ua_list)
#         request.headers['User-Agent'] = user_agent

from selenium import webdriver
import time
import scrapy

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        self.driver = webdriver.PhantomJS()
        if request.url != "https://www.aqistudy.cn/historydata/":
            self.driver.get(request.url)
            time.sleep(2)
            html = self.driver.page_source
            self.driver.quit()
            return scrapy.http.HtmlResponse(url=request.url, body=html, encoding="utf-8", request=request)