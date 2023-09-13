from tkinter import *

root = Tk()
def getval():
    print("the username is ",userval.get())
    print("the username is ",passval.get())

root.title("my gui")

user = Label(root,text="username")
password = Label(root,text="password")
user.grid()
password.grid(row=1)

userval =StringVar()
passval= StringVar()

userentry= Entry(root,textvariable=userval)
passentry= Entry(root,textvariable=passval)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)


sub= Button(root,text="submit",bg="red",command=getval)
sub.grid(row=2,column=1)

root.mainloop()