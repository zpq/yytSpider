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

    
    def crawl(self, root_url):
        if root_url is None:
            return
        self.urls.add_new_url(root_url)
        count = 1;
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "crawl %d : %s" %(count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_datas = self.parses.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_datas(new_datas)
                if count == 100:
                    break
                count = count + 1
            except:
                print "crawl failed"
        self.outputer.output_html()
            
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/subview/99/5828265.htm";
    spider_obj = SpiderMain()
    spider_obj.crawl(root_url)
    