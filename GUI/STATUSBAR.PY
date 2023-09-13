from tkinter import *
root=Tk()
def update():
    statusvar.set("busy....")
    sta.update()
    import time
    time.sleep(2)
    statusvar.set("compiled..")
    
statusvar=StringVar()
statusvar.set("ready")
sta = Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sta.pack(side=BOTTOM,fill=X)
Button(root,text="upload",command=update).pack()
root.mainloop()