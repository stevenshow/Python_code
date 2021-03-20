import sys
import os

path = os.path.dirname(__file__)
file = path + '/yankee.txt'
size = 0
if len(sys.argv) > 1:
    file = sys.argv[1]
    try:
        size = sys.argv[2]
    except:
        size = 20

print(len(sys.argv))
print(sys.argv)
def cmd_line(file='test.txt', size=20):
    print(f'The file is {file}')
    print(f'The size is {size}')

if __name__ == '__main__':
    cmd_line(file, size)
