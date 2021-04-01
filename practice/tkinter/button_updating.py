from tkinter import *

current = 0

def up(t):
    global current
    t.config(state=NORMAL)
    t.delete('1.0', END)
    current +=1
    t.insert(END, current)


def down(t):
    global current
    t.config(state=NORMAL)
    t.delete('1.0', END)
    current -=1
    t.insert(END, current)


def gui_test():
    root = Tk()
    toolbar = Frame(root)

    # Trying to place in center of screen
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    posRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    posDown = int(root.winfo_screenmmheight() - windowHeight/2)

    t = Text(root, height=20, width=50)
    b = Button(toolbar, text='Up', command= lambda: up(t), padx='5', pady='5')
    r = Button(toolbar, text='Down', command=lambda: down(t), padx='5', pady='5')

    t.pack()
    toolbar.pack()
    r.pack(side=LEFT)
    b.pack(side=LEFT)
    root.title('Window')
    root.geometry("400x400+{}+{}".format(posRight, posDown))
    root.mainloop()

def test():
    gui_test()

test()