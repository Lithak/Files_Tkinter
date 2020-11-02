from tkinter import *

root = Tk()
root.title('My Weekend Activities')
root.geometry('600x600')
root.configure(background="#DF4A44")


def open_txt():
    text_file = open("/home/user/Desktop/Friday.txt", 'r+')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def append():
    text_file = open('/home/user/Desktop/Friday.txt', 'w')
    text_file.write(my_text.get(1.0, END))


def clear():
    my_text.delete(0, END)


# Button Exit when pressed terminates the window.
def exit_program():
    root.destroy()


my_text = Text(root, width=40, height=10, font=("Helvetica", 14))
my_text.pack(pady=40)

toolbar = Frame(root, background="#DF4A44")
b = Button(toolbar, text="Create file", width=9, command=open_txt)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="Append data", width=9, command=append)
b.pack(side=LEFT, padx=2, pady=2)

clear_button = Button(toolbar, text="Clear", bg="grey", font="Bold", command=clear)
clear_button.pack(side=LEFT, padx=2, pady=2)

exit_btn = Button(toolbar, text="Exit", font="Bold", bg='red', command=exit_program)
exit_btn.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

mainloop()
