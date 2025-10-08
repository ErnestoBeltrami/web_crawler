class Indexer:
    def __init__(self):
          self.inverted_index = {}
          self.all_pages = []

    def update_indexer(self,words,url):
            for w in words:
              if w not in self.inverted_index:
                self.inverted_index[w] = set()
              self.inverted_index[w].add(url)

    def print_urls(self,target):
            for url in self.inverted_index[target]:
                print(url)