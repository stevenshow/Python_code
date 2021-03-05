import os

with open('/home/steven/Documents/Python_code/CS3270/Project_D/employees.csv', 'r') as f:
    data = [i for i in f.readlines()]
print(data[0])