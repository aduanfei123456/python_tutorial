import spider
from bs4 import BeautifulSoup
import requests
class Html_Parser(spider.Parser):
    def __init__(self):
        super(Html_Parser, self).__init__()

    def html_parse(self,priority, url, keys, deep, content):
        html = BeautifulSoup(content, 'lxml')
        content = html.find(id="main").find('div', 'x-content')
        title = content.h4.string
        for tag in content.find_all("p")[-4:-1]:
            tag.clear()
        passage = content.find("div", "x-wiki-content").get_text()

        return 1,[],[{"title":title,"passage":passage},]
