from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
var=IntVar()
Label(text="what would you have to like sir?",fg="blue").pack()
raio= Radiobutton(text="Dosa",variable=var,value=1).pack()
raio= Radiobutton(text="dal",variable=var,value=2).pack()
raio= Radiobutton(text="paratha",variable=var,value=3).pack()
raio= Radiobutton(text="tea",variable=var,value=4).pack()

root.mainloop()