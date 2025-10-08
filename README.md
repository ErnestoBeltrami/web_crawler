🚀 Features

✅ Crawl web pages recursively using a queue
✅ Extract text and links with BeautifulSoup
✅ Build an inverted index (word → pages containing that word)
✅ Simple search engine with ranking by frequency
✅ Configurable max crawl depth and headers
✅ Modular structure with three main classes:

UrlQueue → manages URLs and crawling loop
Crawler → parses HTML and extracts content
Indexer → builds and queries the inverted index

🧩 Project Structure
web_crawler/
│
├── crawler/
│   ├── url_queue.py     # orchestrates crawling
│   ├── crawl.py         # HTML parsing and link 
│   ├── indexer.         # inverted index logic
├── main.py              # entry point
├── requirements.txt
└── README.md


🧮 How It Works
UrlQueue manages the queue of URLs to visit and limits crawl depth.
Crawler fetches and parses each page using requests and BeautifulSoup.
Indexer stores text in an inverted index for fast lookups.
The user can query words or phrases to see which pages contain them.