import itertools
import array as arr

mydict = {'file1': ['some', 'data'], 'file2': ['more', 'data'], 'file3': ['even', 'more']}

myarray = arr.array('i', [])
for x in range(11):
    myarray.append(x)
end = len(myarray)

for x in itertools.dropwhile(lambda x:x < 3, myarray):
    pass

print(len(mydict['file1']))

for x in mydict.keys():
    print(x)
    for y in range(len(x)-1):
        print(mydict[x][y])