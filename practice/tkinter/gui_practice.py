import tkinter as tk
import tkinter.messagebox

def testcommand():
    tkinter.messagebox.showinfo('Hello there', 'Thank you for pushing my button!')

def submit():
    name = name_var.get()
    password = pass_var.get()
    
    print('The name is ' + name)
    print('The password is ' + password)

    name_var.set('')
    pass_var.set('')

root = tk.Tk()
# code to add widgets go here
#Button = tkinter.Button(top, activebackground = 'blue', text = 'Hello', command = testcommand)
root.geometry('300x200')

name_var = tk.StringVar()
pass_var = tk.StringVar()
# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre', 10 ,'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
  
# creating a entry for password
passw_entry=tk.Entry(root, textvariable = pass_var, font = ('calibre',10,'normal'), show = '*')
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()