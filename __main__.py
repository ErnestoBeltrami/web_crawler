from crawler import url_queue
from crawler.input_parser import InputParser

urls = [
    "https://en.wikipedia.org/wiki/World_War_II",
    "https://www.bbc.com/news"
    ]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/117.0 Safari/537.36"
}


print('hello')

depth = int(input("Number of pages: "))

url_queue = url_queue.UrlQueue(depth,urls)
url_queue.start(headers)

input_list = input().lower().split()
input_parser = InputParser(input_list)
print('searching...')
url_queue.get_indexer().print_urls(input_parser.get_parsed_list())



