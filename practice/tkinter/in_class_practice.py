from tkinter import *
import random
import os
import string
# Let's make a GUI that can input a file location and then open that file if it exists, throw an error if not. 
path = os.path.dirname(os.path.abspath(__file__)) + '/'

def change_text():
    t.insert(END, random.randint(10, 100))

def read_file():
    lines= []
    try:
        with open(path + 'text.txt', 'r') as f:
            for ele in f.readlines():
                lines.append(ele)
    except:
        var.set('Could not find file.')
    
    t.config(state=NORMAL)
    t.insert(END, 'Deleting...')
    t.delete('0.0', END)
    t.insert(END, ''.join(lines))

root = Tk()
toolbar = Frame(root)

# Trying to place in center of screen
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
posDown = int(root.winfo_screenmmheight() - windowHeight/2)

b_quit = Button(toolbar, text='Quit', fg='red', command=quit)
var = StringVar()
var.set('Click to get random number')
t = Text(root, height=20, width=50)
b = Button(toolbar, text='Change Number', command=change_text(), padx='5', pady='5')
r = Button(toolbar, text='Read text.txt file', command=read_file(), padx='5', pady='5')
w = Label(root, textvariable=var)


t.pack()
toolbar.pack()
r.pack(side=LEFT)
b.pack(side=LEFT)
w.pack()
b_quit.pack(side=RIGHT)
root.title('Window')
root.geometry("300x300+{}+{}".format(posRight, posDown))
root.mainloop()