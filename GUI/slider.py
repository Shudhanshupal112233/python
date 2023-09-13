from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()

# myslider= Scale(root,from_=0 , to=100)
# myslider.pack()
def getdollars():
    tmsg.showinfo("amount credit",f"you have {myslider2.get()} dollars in ur account")
    
Label(text="want how many dollars?").pack()
myslider2= Scale(root,from_=0 , to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.pack()

Button(text="dollars" ,command=getdollars).pack()


root.mainloop()