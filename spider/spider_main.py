#coding = utf8
'''
Created on Jan 1, 2016

@author: zpq
'''
from spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parses = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

#给予一个初始页面和最大抓取数量，抓取所有在页面上出现的链接的页面title与sammary    
#     def crawl(self, root_url):
#         if root_url is None:
#             return
#         self.urls.add_new_url(root_url)
#         count = 1;
#         while self.urls.has_new_url():
#             try:
#                 new_url = self.urls.get_new_url()
#                 print "crawl %d : %s" %(count, new_url)
#                 html_content = self.downloader.download(new_url)
#                 new_urls, new_datas = self.parses.parse(new_url, html_content)
#                 self.urls.add_new_urls(new_urls)
#                 self.outputer.collect_datas(new_datas)
#                 if count == 100:
#                     break
#                 count = count + 1
#             except:
#                 print "crawl failed"
#         self.outputer.output_html()


#抓取给定页面的title与summary和所有子(不含孙)链接的title与summary
    def crawl(self, root_url):
        if root_url is None:
            return
        html_content = self.downloader.download(root_url)
        new_urls, new_datas = self.parses.parse(root_url, html_content)
        self.outputer.collect_datas(new_datas)
        self.urls.add_new_urls(new_urls)
        count = 1;
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "crawl %d : %s" %(count, new_url)
                html_content = self.downloader.download(new_url)
                new_datas = self.parses.parse_single_page(new_url, html_content)
                self.outputer.collect_datas(new_datas)
                count = count + 1
            except Exception,e:
                print e
                print "crawl failed"
        self.outputer.output_html()
            
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/subview/99/5828265.htm";
    spider_obj = SpiderMain()
    spider_obj.crawl(root_url)
    