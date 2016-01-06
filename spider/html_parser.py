'''
Created on Jan 1, 2016

@author: zpq
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm"))
        new_urls = set()
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_datas(self, page_url, soup):
        res_datas = {}
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>PHP</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_datas['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_datas['summary'] = summary_node.get_text()
        
        res_datas['url'] = page_url
        return res_datas
        
    
    def parse(self, page_url, html_source_content):
        if page_url is None or html_source_content is None:
            return
        
        soup = BeautifulSoup(html_source_content, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_datas = self._get_new_datas(page_url, soup)
        return new_urls, new_datas

    def parse_single_page(self, page_url, html_content):
        if html_content is None or page_url is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding = 'utf-8')
        res_datas = {}
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>PHP</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_datas['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_datas['summary'] = summary_node.get_text()
        
        res_datas['url'] = page_url
        return res_datas
        
    
    



