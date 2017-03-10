import requests
from bs4 import BeautifulSoup
import os
import re
class fetch_liao:
    def __init__(self):
        self.base_url="http://www.liaoxuefeng.com"
        self.headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        self.filter=re.compile(r"")
    def  get_html(self,url):

        return requests.get(self.base_url+url,headers=self.headers).text
    def parse_content(self,response):
        html=BeautifulSoup(response,'lxml')
        content=html.find(id="main").find('div','x-content')
        title=content.h4.string
        for tag in content.find_all("p")[-4:-1]:
            tag.clear()
        passage=content.find("div","x-wiki-content").get_text()
        print(title)
        return(title+passage)


    def parse_dialog(self,content):
        html=BeautifulSoup(content,'lxml')
        dir=html.find(attrs={'class':'uk-nav','style':"margin-right:-15px;"}).find_all('li')

        for tag in dir[1:]:
            href=tag.a['href']
            print(href)
            pas=self.parse_content(self.get_html(href))


            if tag['style']=="margin-left:1em;":
                first_dir = tag.a.string
                os.makedirs('./Python/'+first_dir)
                with open('./Python/'+first_dir+'/'+first_dir+'.txt','w') as f:
                    f.write(pas)

            elif tag['style']=="margin-left:2em;":
                second_dir=tag.a.string
                with open('./Python/'+first_dir+'/'+second_dir+'.txt','w') as f:
                    f.write(pas)




        #print(dir)
f=fetch_liao()
f.parse_dialog(f.get_html("/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000#0"))




