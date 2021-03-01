import string
import matplotlib.pyplot as plt

def read_file(txt_file, txt_out): #Processes text file and counts the occurences of letters a-z and A-Z
    counter = 0
    user_input = input('Enter 1 for processing with a-z and A-Z.  Enter 2 for genome letters (a,g,c,t): ')
    if int(user_input) == 1:
        alphabet = string.ascii_letters
    else:
        alphabet = ['a','g','c','t']
    
    for letter in alphabet:
        for line in txt_file:
            for char in line:        
                if char == letter:    
                    counter += 1
                else:
                    continue
        print("There were |" + str(counter) + "| occurences of '" + str(letter) + "' in this file")
        output_file(txt_out, counter, letter)
        counter = 0

def output_file(txt_out, counter, letter): #writes the data found while reading and processing file
    txt_out.write(str(letter)+ ' ' + str(counter))
    txt_out.write('\n')
    

def letter_Occurences(min_max): #Finds the minimum letter and maximum letter occurences in the file
    x, y = [],[]
    for el in min_max:
        row = el.split()
        x.append(row[0])
        y.append(row[1])
    myDict = {x[i]: y[i] for i in range(len(x))}
    key_max = max(myDict.keys(), key = lambda k: int(myDict[k]))
    key_min = min(myDict.keys(), key = lambda k: int(myDict[k]))
    print("The letter with the most occurences was '" + key_max + "' with |" + myDict[key_max] + "| occurence(s).")
    print("The letter with the least occurences was '" + key_min + "' with |" + myDict[key_min] + "| occurence(s).")


def open_files(inputfile, outputfile, minmaxfile): #Takes in 2 files (input, outputfile) minmaxfile is outputfile in read format
    txt = open(inputfile, 'r')
    txt_file = txt.read()
    txt_out = open(outputfile, 'a+')
    min_max = open(minmaxfile, 'r')
    want_read = input('Enter 1 if this is the first time opening and processing this file, else enter ANY KEY: ')
    
    if int(want_read) == 1: #prevents multiple entries of the same data in the same file
        read_file(txt_file, txt_out)
        txt_file.close()
    else:
        pass
        
    letter_Occurences(min_max)
    txt_out.close()
    print("Your occurences file is stored in | " + minmaxfile + " |")


#Takes in 2 files (input, outputfile) minmaxfile is outputfile in read format
#open_files('C:\\Users\\Steven\\Desktop\\Python\\large\\world192.txt',
#        'C:\\Users\\Steven\\Desktop\\Python\\large\\world192_occurences.txt',
#        'C:\\Users\\Steven\\Desktop\\Python\\large\\world192_occurences.txt')




# txt_file = open('C:\\Users\\Steven\\Desktop\\Python\\large\\world192.txt', "r")
# txt_file_readable = txt_file.read()
# txt_out = open('C:\\Users\\Steven\\Desktop\\Python\\large\\world192_occurences.txt', 'a+')
# read_file()
# txt_file.close()
# txt_out.close()
# min_max = open('C:\\Users\\Steven\\Desktop\\Python\\large\\world192_occurences.txt', 'r')
# letter_Occurences()
# min_max.close()


#Create function that opens and passes files to correct functions, then closes them
#Create function that counts most used words in file

def list_comp():
    my_list = [x.strip(' ') for x in input('enter a comma separated list: ').split(',')]
    [print(x) for x in my_list if x.lower().startswith('h')]