from tkinter import *
root=Tk()
def fun():
    print("hello sudha")

# mymenu=Menu(root)
# mymenu.add_command(label="File",command=fun)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

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


root.mainloop()