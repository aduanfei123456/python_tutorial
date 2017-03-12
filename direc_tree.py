from bs4 import BeautifulSoup
import requests
import logging
import os
import re
content = requests.get(
            "http://www.liaoxuefeng.com" + "/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000#0", headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
html = BeautifulSoup(content.text, 'lxml')
def has_style(t):
    return t.has_attr('style')
dir = html.find(attrs={'class':'uk-nav', 'style': "margin-right:-15px;"}).find_all('li',style=True)
list={}
count=0
reg=re.compile('/')
print(dir)
for tag in dir:
    count=count+1
    logging.warning(count)
    if tag['style'] == "margin-left:1em;":
                tag.a.string = reg.sub("",tag.a.string)
                list[tag.a.string]='./Python3/'+tag.a.string
                if not os.path.exists(list[tag.a.string]):
                    os.makedirs(list[tag.a.string])
                tag.a.string=tag.a.string.strip("/")
                list[tag.a.string]=list[tag.a.string]+'/'+tag.a.string+'.txt'
                with open(list[tag.a.string], 'w') as f:
                    pass
    elif tag['style']=="margin-left:2em;":

                first_d=tag.find_previous(style="margin-left:1em;")
                tag.a.string = reg.sub("", tag.a.string)
                list[tag.a.string]='./Python3/'+first_d.a.string+'/'+tag.a.string+'.txt'
                with open(list[tag.a.string], 'w') as f:
                    pass



print(list)