from tkinter import *


cal_root= Tk()
cal_root.title(" my gui")

f= Frame(cal_root,bg="grey",borderwidth=8)
f.pack(side="top",fill="x")
title_label=Label(f,text='''READY''',bg="yellow",fg="purple",font="Aerial  55  bold  ",padx= 123)


title_label.pack(side="bottom")


cal_root.mainloop()


