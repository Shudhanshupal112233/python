from tkinter import *
root=Tk()
def harry(events):
    print(f" you click on coordinates :{events.x},{events.y}")
root.title("my gui")
root.geometry("700x345")
b1=Button(root,text="please click me,",fg="blue")
b1.pack()
b1.bind('<Button-1>',harry)
b1.bind('<Double-1>',quit)
root.mainloop()