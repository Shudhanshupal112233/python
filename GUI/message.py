from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
def fun():
    print("hello sudha")

# mymenu=Menu(root)
# mymenu.add_command(label="File",command=fun)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)
def help():
    print("i will help u")
    tmsg.showinfo("help","sudha will hepl u")
    
def rate():
    print("rate us")
    value= tmsg.askquestion("was ur experience good","was ur experience good")
    if value=="yes":
        msg="rate on play store"
        
    else:
       msg="someting is wrong"
    tmsg.showinfo("experince",msg)

urmenu= Menu(root)
m1=Menu(urmenu)
m1.add_command(label="save",command=fun)
m1.add_command(label="print",command=fun)
m1.add_separator()
m1.add_command(labe="open file",command=fun)
m1.add_command(label="Exit",command=quit)
root.config(menu=urmenu)

urmenu.add_cascade(label="File",menu=m1)

m21= Menu(urmenu)
m21=Menu(urmenu)
m21.add_command(label="search")
m21.add_command(label="run")
m21.add_command(labe="select")
m21.add_command(label="Exit",command=quit)
root.config(menu=urmenu)

urmenu.add_cascade(label="Run",menu=m21)

m3= Menu(urmenu)
m3=Menu(urmenu)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)

root.config(menu=urmenu)

urmenu.add_cascade(label="Help",menu=m3)





root.mainloop()