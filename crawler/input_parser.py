from .stopword_list import StopWordList

class InputParser:
    def __init__(self, word_list):
        self.stopword = StopWordList.stopword
        self.parsed_list = []

        current_set = set()

        for w in word_list:
            if w == 'or':
                if current_set:  
                    self.parsed_list.append(current_set)
                current_set = set()  # Ricomincia un nuovo set dopo 'or'
            elif w not in self.stopword:  # Aggiungi solo se non è stopword
                current_set.add(w)

        # aggiungi l’ultimo set se non vuoto
        if current_set:
            self.parsed_list.append(current_set)

    def get_parsed_list(self):
        return self.parsed_list