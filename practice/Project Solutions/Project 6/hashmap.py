'''
Project: Project 7 Hashing & Caching (instructor Solution)
Author: George Rudolph
Course: CS 2420-000 Fall 2020
Date: 10 Nov 2020

Hash Map solution is modified from code orginally written by Dana Doggett in 2019.
The Project it solves is a completely different application.
This solution assumes the keys are tuples, and so if the application changes
that part of the solutin needs to change.
'''

class HashMap():
    ''' This implements a dictionary structure using linear-probing '''
    INITIAL_SIZE = 7
    def __init__(self):
        ''' initializes an empty HashMap '''
        self.buckets = [None] * HashMap.INITIAL_SIZE
        self._size = 0

    def do_hash(self, key):
        ''' generates a hash value from a key. Key must be a tuple '''
        if not isinstance(key, tuple):
            raise KeyError("Key must be a tuple")
        r, c = key
        return r*(r+1)//2 + c

    def get(self, key):
        ''' returns the value associated with key. If key is not found, default is returned '''
        index = self.do_hash(key) % len(self.buckets)
        #print('start:', index)

        original_index = index
        while True:
            if self.buckets[index] == None:
                index = (index + 1) % len(self.buckets)
                if index == original_index:
                    raise KeyError(f"Key{key} not found.")
                continue
            if self.buckets[index][0] != key:
                index = (index + 1) % len(self.buckets)
                if index == original_index:
                    raise KeyError(f"Key{key} not found.")
                continue
            if self.buckets[index][0] == key:
                found = True
                return self.buckets[index][1]
            if original_index == index:
                raise KeyError(f"Key{key} not found.")


    def set(self, key, value):
        ''' associates value with key.
        If HashMap gets too full, this will rehash the existing map.
        '''
        index = self.do_hash(key) % len(self.buckets)
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                break
            index = (index + 1) % len(self.buckets)
        self.buckets[index] = (key, value)
        self._size += 1
        load_factor = self._size / len(self.buckets)
        if load_factor >= 0.80:
            self.rehash()

    def clear(self):
        ''' clears the HashMap '''
        self.buckets = [None] * HashMap.INITIAL_SIZE
        self._size = 0

    def remove(self, key):
        ''' Remove a key,value pair from the HashMap.
        If the key does not exist, nothing happens.
        '''
        index = self.do_hash(key) % len(self.buckets)
        if self.buckets[index] is None:
            return

        if self.buckets[index][0] != key:
            original_index = index
            while self.buckets[index][0] != key:
                index = (index + 1) % len(self.buckets)
                if self.buckets[index] is None:
                    return
                if index == original_index:
                    return
        self.buckets[index] = None

    def capacity(self):
        ''' returns the capacity of the Hashmap '''
        return len(self.buckets)

    def size(self):
        ''' returns the number of key-value pairs currently in the HashMap '''
        return self._size

    def keys(self):
        ''' returns a list of keys in the Hashmap '''
        return [item[0] for item in self.buckets if item is not None]

    def rehash(self):
        ''' rehashes the current data into a new list of buckets.

        The policy is new k = 2k - 1.
        The number of buckets being odd increases the likelihood that any
        key value k with be relatively prime.
        '''
        old_buckets = self.buckets
        self.buckets = [None] * (len(self.buckets) * 2 - 1)
        self._size = 0

        for i in range(len(old_buckets)):
            if old_buckets[i] is not None:
                self.set(old_buckets[i][0], old_buckets[i][1])

    def __str__(self):
        s = ""
        for i,b in enumerate(self.buckets):
            s += f'{i} -> {b}\n'
        return s

def main():
    ''' A minor bit of test code. Does not replace official pytest code.'''
    import pytest
    hm = HashMap()
    with pytest.raises(KeyError):
        hm.get((0,0))

    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    print(hm)
    print("Remove (3,3)")
    hm.remove((3,3))
    print(hm)
    print(hm.get((7,7)))
if __name__ == "__main__":
    main()
