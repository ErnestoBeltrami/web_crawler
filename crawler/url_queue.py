from .crawl import *
import requests
import time
import queue

class UrlQueue:
 
    def __init__(self,maxpages,urls):
        self.q = queue.Queue()
        self.maxpages = maxpages
        for url in urls:
            self.q.put(url)
        self.visited = set()
        self.crawler = Crawler()


    def start(self,headers):
        while not self.q.empty() and len(self.visited) < self.maxpages:   
            url = self.q.get()
            print("Visiting:", url)

            if url in self.visited:
                continue

            self.visited.add(url)
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if not response.ok:
                    print("errore su:", url)
                    continue
            except requests.RequestException as e:
                print("request failed:", e)
                continue

            time.sleep(1)
            self.crawler.crawl_page(url,response.text,self.visited,self.q)
            

        print('done')
  
    def get_indexer(self):
        return self.crawler.indexer