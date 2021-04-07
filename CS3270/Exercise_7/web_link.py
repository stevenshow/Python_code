import pprint

class HayStack():
    def __init__(self, url, depth):
        super().__init__()
    
    def lookup(self, w):
<<<<<<< HEAD
        pass

    def index(self):
        pass
    
    def graph(self):
=======
>>>>>>> 09d60e255d0062056646e2c40ac0723bf0072cad
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