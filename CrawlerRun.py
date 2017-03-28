#!/usr/bin/python
# filename: run.py
import re
from crawler import Crawler, CrawlerCache

if __name__ == "__main__": 
    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler(CrawlerCache('crawler.db'))
    root_re = re.compile('^/$').match
    crawler.crawl('http://google.com', no_cache=root_re)
    crawler.crawl('http://', no_cache=root_re)
    crawler.crawl('http://', no_cache=root_re)
    crawler.crawl('http://', no_cache=root_re)
    crawler.crawl('http://', no_cache=root_re)
