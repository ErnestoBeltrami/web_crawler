import queue
from bs4 import BeautifulSoup
from .indexer import *
import re


class Crawler:
    def __init__(self):
        self.indexer = Indexer()

    def crawl_page(self,url, html_file, set_url, queue_url):
        soup = BeautifulSoup(html_file, 'html.parser')
        web_page_summary = {
            'url': url,
            'title': soup.title.string if soup.title else "",
            'text':  re.findall(r'[a-zA-Z0-9]+', soup.get_text().lower())
        }
        self.indexer.all_pages.append(web_page_summary)
        words_in_page = web_page_summary['text']

        self.indexer.update_indexer(words_in_page,url)
        
        for link in soup.find_all('a'):
            link_url = link.get('href')
            if link_url and link_url.startswith("http") and link_url not in set_url:
                queue_url.put(link_url)
   
