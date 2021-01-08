import names

my_list = ['Steven', 'Kayla', 'Kit Kat', 'Nacho']
human = ['Steven', 'Kayla']
cat = ['Kit Kat', 'Nacho']
for my_list in cat:
    pass
    #print(my_list)
    

name_list = []
for name in range(1000):
    name_list.append(names.get_first_name())
#print(name_list)

#for my_list in human:
    #print(f'Found {my_list} in list: ', list(my_list)
    
if human[0] in name_list:
    print(f'{human[0]} was found in the List: ', name_list)