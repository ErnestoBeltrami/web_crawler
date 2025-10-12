from .stopword_list import StopWordList
class Indexer:
    
    def __init__(self):
          self.stopword = StopWordList.stopword
          self.inverted_index = {}
          self.all_pages = []

    def update_indexer(self,words,url):
            for w in words:
              if w in self.stopword:
                   continue
              if w not in self.inverted_index:
                self.inverted_index[w] = set()
              self.inverted_index[w].add(url)

    def get_printable_url_set(self, target_list):
      printable_url_set = set()
      
     
      
      # Per ogni set nella lista (ogni set è un gruppo AND)
      for and_group in target_list:
          
          
          # Inizia con tutti gli URL per il primo termine
          current_set = None
          
          for word in and_group:
              
              if word not in self.inverted_index:
                  
                  current_set = set()
                  break
              else:
                  
                  if current_set is None:
                      current_set = set(self.inverted_index[word])
                  else:
                      current_set = current_set & set(self.inverted_index[word])
  
          # Unisci i risultati di questo gruppo AND all'insieme totale (OR)
          if current_set:
              printable_url_set = printable_url_set | current_set
      
      
      return printable_url_set
    
    def print_urls(self,target_list):
            
            printable_url_set = self.get_printable_url_set(target_list)
            if printable_url_set:
                 for url in printable_url_set:
                      print(url)
            else:
                 print('Research was unsuccessfull')
        
"""lista di set, in ogni set ci sono n parole, stampo link solo se tutte le parole sono 
presenti nel indexer
set di url che trovo
"""