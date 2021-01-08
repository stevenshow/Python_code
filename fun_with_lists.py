import names
import matplotlib.pylab as plt

my_list = ['Steven', 'Kayla', 'Kit Kat', 'Nacho']
human = ['Steven', 'Kayla']
cat = ['Kit Kat', 'Nacho']
#for my_list in cat:
#    pass
    #print(my_list)

#Counts occurences of each name in the random name list and places them in a dictionary
def count_names(name_list):
    name_dict = {}
    for name in name_list:
        if name not in name_dict:
            name_dict[name] = 1
        else:
            name_dict[name] += 1
    return name_dict


def get_name_list():
    name_list = []
    for name in range(10):
        name_list.append(names.get_first_name())
    return name_list



def plot_dict():
    name_dict = count_names(get_name_list())
    lists = sorted(name_dict.items(), key = lambda kv:kv[1], reverse = True)
    x, y = zip(*lists)
    plt.plot(x,y)
    plt.show()

plot_dict()

#print(name_list)

#for my_list in human:
    #print(f'Found {my_list} in list: ', list(my_list)
    
#if human[0] in name_list:
#    print(f'{human[0]} was found in the List: ', name_list)