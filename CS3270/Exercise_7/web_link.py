import pprint
import re

import requests

'''
[X] Class received URL and optional depth (defaul to 3)
[X] processing starting webpage and find all embedded webpage 
[] Index maps every word (alphanumeric and apostrophes) to a list of URLS of pages that contain that word
[X] Graph maps every URL to a list of web pages it links to directly
[] Lookup(word) takes a word and searches and returns the webpages that contain that word in RANK ORDER, highest to lowest
[X] Do not crawl the webpage twice (keep track of CRAWLED webpages and TO BE CRAWLED webpages)
[X] DO NOT USE Beautiful Soup, Scrapy, or any other web crawler. use urllib.request or requests

Hints:
1. Write the functions and test them before placing them in the classification
2. Regular expressions are key
3. Might be spaces around href, and also href may not be the first field in an <a ...> tag
4. You only have to write about 30 lines of code. Redirect this output to a text file and submit it along with your source code.
5. Crawling happens in the constructor
'''


class HayStack():
    def __init__(self, url, depth=3):
        # Crawling happens in the constructor
        self.url = url
        # Maps every URL encountered to a list of the web pages it links to
        # directly.
        self.graph = {}
        # Maps every word encountered on each crawled page to a list of URLs
        # of all the pages that contain that word.  Only keeps words consisting
        # of runs of alphabetic characters and apostrophes. Convert lowercase.
        # Only consider text that is found outside of HTML tags.
        self.index = {}
        self.crawled = []
        self.to_crawl = []
        self.depth = depth
        self.crawled_depth = 0
        self.crawled.append(self.url)
    
    def grapher(self):
        pass

    def indexer(self):
        pass

    def lookup(self, word):
        '''Takes str(word) as search key and outputs the webpages
        that contain that word in RANK order, highest to lowest.'''
        pass

    def compute_ranks(self, graph):
        d = 0.85
        # probability that surfer will bail
        numloops = 10
        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages
        for _ in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for url in graph:
                    if page in graph[url]:  # this url links to page
                        newrank += d*ranks[url]/len(graph[url])
                newranks[page] = newrank
            ranks = newranks
        self.ranks = ranks


def get_URL(url):
    # Get initial webpage
    start_url = url
    crawled = []
    to_crawl = []
    graph = {}
    index = {}
    url_regex = "<a[^>]* href *= *\"([^\"]*)"
    text_regex = ""
    depth = 4
    crawl_depth = 0
    
    # In the constructor
    try:
        reqs = requests.get(start_url, headers={'user-agent': 'XY'})
        crawled.append(start_url)
        content = reqs.content.decode('utf-8')
        match = re.findall(url_regex, content)
        crawl_depth += 1
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # Get first page URLs to store in to_crawl
    graph[start_url] = []
    for ele in match:
        to_crawl.append(ele)
        graph[start_url].append(ele)
    
    # In the grapher function
    while(crawl_depth <= depth):
        for page in to_crawl:
            if page not in crawled:
                graph[page] = []
                try:
                    reqs = requests.get(page, headers={'user-agent': 'XY'})
                    crawled.append(page)
                    content = reqs.content.decode('utf-8')
                    match = re.findall(url_regex, content)
                    for ele in match:
                        if ele not in to_crawl and ele not in crawled:
                            to_crawl.append(ele)
                        if ele not in graph[page]:
                            graph[page].append(ele)
                    crawl_depth += 1
                    to_crawl.remove(page)
                except requests.exceptions.RequestException as e:
                    raise SystemExit(e)
            else:
                to_crawl.remove(page)
    print('graph')
    pprint.pprint(graph)


get_URL('http://freshsources.com/page1.html')


# if __name__ == '__main__':
#     engine = HayStack('http://freshsources.com/page1.html', 4)
#     for w in ['pages', 'links', 'you', 'have', 'I']:
#         print(w)
#         pprint.pprint(engine.lookup(w))
#         print()
#         print('index:')
#         pprint.pprint(engine.index)
#         print()
#         print('graph:')
#         pprint.pprint(engine.graph)
#         print()
#         print('ranks:')
#         pprint.pprint(engine.ranks)
