from tu_fetcher import Html_Fetcher
from tu_parser import Html_Parser
from tu_saver import Html_Saver
import spider
def get_tutorial():
    fetcher_number=3
    fetcher_list=[]
    for i in range(fetcher_number):
        fetcher_list.append(Html_Fetcher())
    parser=Html_Parser()
    saver=Html_Saver()
    html_spider=spider.WebSpider(fetcher_list,parser,saver,None)
    base_url="http://www.liaoxuefeng.com"
    url_list=[url for url in saver.dir]
    #url="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000"
    for url in url_list:
        html_spider.set_start_url(url,("lists",),priority=1)
    html_spider.start_work_and_wait_done(fetcher_num=fetcher_number)
get_tutorial()
