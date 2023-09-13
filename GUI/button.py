from tkinter import *

root = Tk()
def name():
    print("my self")

def hello():
    print(" sudhanshu")    
f1= Frame(root,borderwidth=8,bg="grey")
f1.pack()

b1=Button(f1,text="print now",command=name)
b1.pack()


b2=Button(f1,text="print now",command=hello)
b2.pack()

   
   
root.mainloop()   
