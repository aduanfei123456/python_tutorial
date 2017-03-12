import spider
import logging
import requests
import sys
from spider.utilities import make_random_useragent
class Html_Fetcher(spider.Fetcher):
    def __init__(self):
        super(Html_Fetcher, self).__init__()
        self.base_url = "http://www.liaoxuefeng.com"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    def url_fetch(self,url,keys,fetch_repeat):
            headers = {"User-Agent": make_random_useragent()}
            logging.warning("----------------------")
            logging.warning("fetch%s",url)
            response=requests.get(self.base_url+url,headers=headers)
            #logging.warning(response.text)
            return 1,response.text




