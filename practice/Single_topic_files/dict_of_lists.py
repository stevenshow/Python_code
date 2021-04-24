def dict_lists():
    graph = {}
    urls = ['page1', 'page2', 'page3', 'page4']
    for x in range(4):
        graph[urls[x]] = [x + 1]
    print(graph)
    for y in range(4):
        graph[urls[y]].append(y+1)
    print(graph)

def compare_lists():
    list1 = [1,2,3,4,5]
    list2 = [1,2,3,4,5]
    list3 = [1,2,3,4,5,6]
    list4 = ['page3', 'page1', 'page5', 'page4']
    list5 = ['page1', 'page3', 'page5']
    set_diff = list(set(list4).symmetric_difference(set(list5)))
    #list_diff = list(set_diff)
    print(set_diff)
    #while (len(set_diff)):

def dict_add():
    x = 'Test'
    y1= 123
    y2 = 456
    my_dict = {}
    my_dict[x] = [y1,y2]
    print(my_dict)

dict_add()
#compare_lists()
# dict_lists()