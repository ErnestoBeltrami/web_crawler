from crawler import url_queue


urls = [
    "https://en.wikipedia.org/wiki/World_War_II",
    "https://www.bbc.com/news"
]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/117.0 Safari/537.36"
}


print('hello')

url_queue = url_queue.UrlQueue(5,urls)
url_queue.start(headers)

target_word = input()
print('searching...')
url_queue.print_urls(target_word)

