import pprint
'''
[X] Class received URL and optional depth (defaul to 3)
[] processing starting webpage and find all embedded webpage 
[] Index() maps every word (alphanumeric and apostrophes) to a list of URLS of pages that contain that word
[] Graph() maps every URL to a list of web pages it links to directly
[] Lookup() takes a word and searches and returns the webpages that contain that word in RANK ORDER, highest to lowest
[] Do not crawl the webpage twice
[] DO NOT USE Beautiful Soup, Scrapy, or any other web crawler. use urllib.request or requests
'''


class HayStack():
    def __init__(self, url, depth=3):
        super().__init__()
    
    def lookup(self, word):
        pass

    def index(self):
        pass
    
    def graph(self):
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
                    if page in graph[url]: # this url links to page
                        newrank += d*ranks[url]/len(graph[url])
                newranks[page] = newrank
            ranks = newranks
        self.ranks = ranks


if __name__ == '__main__':
    engine = HayStack('http://freshsources.com/page1.html',4)
    for w in ['pages','links','you','have','I']:
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
        pprint.pprint(engine.ranks)