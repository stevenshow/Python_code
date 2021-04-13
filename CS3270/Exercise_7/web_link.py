<<<<<<< HEAD

=======
>>>>>>> e3fb4ce6a541feac8d9e79a96268b1118b4aa3e5
'''Accepts a url and a depth.  Proceeds to crawl all the links on the webpags down
to the crawl depth.  Maps all URLs to the webpages they link to directly.  Maps all
alphabetic words with or without apostrophes to the webpages they were found on.
Ranks the webpages.  Allows for lookup of words and displays the webpages where
the word is found in rank order, highest to lowest.
Created by: Steven Schoeinger 04/11/2021'''
import pprint
import re

import requests

# pylint: disable=invalid-name
# pylint: disable=too-many-instance-attributes
# [X] Class received URL and optional depth (defaul to 3)
# [X] processing starting webpage and find all embedded webpage
# [X] Index maps every word (alphanumeric and apostrophes) to a list of URLS of pages that
#     contain that word
# [X] Graph maps every URL to a list of web pages it links to directly
# [X] Lookup(word) takes a word and searches and returns the webpages that contain that word
#     in RANK ORDER, highest to lowest
# [X] Do not crawl the webpage twice (keep track of CRAWLED webpages and TO BE CRAWLED webpages)
# [X] DO NOT USE Beautiful Soup, Scrapy, or any other web crawler. use urllib.request or requests

# Hints:
# 1. Write the functions and test them before placing them in the classification
# 2. Regular expressions are key
# 3. Might be spaces around href, and also href may not be the first field in an <a ...> tag
# 4. You only have to write about 30 lines of code. Redirect this output to a text file and submit
#     it along with your source code.
# 5. Crawling happens in the constructor


class HayStack():
    '''Crawls webpages and gives back data based on pages linked to and words on each page'''

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
        self.crawl_depth = 0
        self.crawled.append(self.url)
        self.url_regex = '<a[^>]* href *= *\"([^\"]*)'
        self.text_regex = '([a-zA-Z\']+(?![^<>]*>))'
        try:
            reqs = requests.get(self.url, headers={'user-agent': 'XY'})
            self.crawled.append(self.url)
            content = reqs.content.decode('utf-8')
            links = re.findall(self.url_regex, content)
            self.crawl_depth += 1
        except requests.exceptions.RequestException as e:
            raise SystemExit from e
        # Get first page URLs to store in to_crawl
        self.graph[self.url] = []
        for link in links:
            self.to_crawl.append(link)
            self.graph[self.url].append(link)
        self.grapher()
        self.indexer(self.url, self.index, content)
        self.compute_ranks(self.graph)

    def grapher(self):
        '''Maps every URL toa list of the web pages it links to directly'''
        while self.crawl_depth <= self.depth:
            for page in self.to_crawl:
                if page not in self.crawled:
                    self.graph[page] = []
                    try:
                        reqs = requests.get(page, headers={'user-agent': 'XY'})
                        self.crawled.append(page)
                        content = reqs.content.decode('utf-8')
                        # Call to indexer to get the words indexed
                        self.indexer(page, self.index, content)
                        links = re.findall(self.url_regex, content)
                        for link in links:
                            if link not in self.to_crawl and link not in self.crawled:
                                self.to_crawl.append(link)
                            if link not in self.graph[page]:
                                self.graph[page].append(link)
                        self.crawl_depth += 1
                        self.to_crawl.remove(page)
                    except requests.exceptions.RequestException as e:
                        raise SystemExit from e
                else:
                    self.to_crawl.remove(page)

    def indexer(self, page, index, content):
        '''Gets the all alhpabetic words, including apostrophes, and places
        them in the index with the corresponding url that the word was found on '''
        match = re.findall(self.text_regex, content.lower())
        # Make match a set so that there are no duplicate words
        matches = set(match)
        for word in matches:
            index.setdefault(word, []).append(page)

    def lookup(self, word):
        '''Takes str(word) as search key and returns the webpages
        that contain that word in RANK order, highest to lowest.'''
        sorted_values = sorted(self.ranks, key=self.ranks.get, reverse=True)
        lookup_list = []
        for i in sorted_values:
            if i in self.index[word.lower()]:
                lookup_list.append(i)
        return lookup_list

    def compute_ranks(self, graph):
        '''Computes the ranks of each webpage and places them in a dictionary'''
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


if __name__ == '__main__':
    engine = HayStack('http://freshsources.com/page1.html', 4)
    for w in ['pages', 'links', 'you', 'have', 'I']:
        print(w)
        pprint.pprint(engine.lookup(w))
        print()
    print('index:')
    pprint.pprint(engine.index)
    print()
    print('graph:')
    pprint.pprint(engine.graph)
    print()
    print('ranks:')
<<<<<<< HEAD
    pprint.pprint(engine.ranks)
=======
    pprint.pprint(engine.ranks)
>>>>>>> e3fb4ce6a541feac8d9e79a96268b1118b4aa3e5
