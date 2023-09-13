from tkinter import *
root=Tk()
canvas_h=500
canvas_w=800
root.title("my gui")
root.geometry(f"{canvas_h}x{canvas_w}")
can_wid= Canvas(root,width=canvas_w,height=canvas_h)
can_wid.pack()
can_wid.create_line(0,0,800,200)
can_wid.create_rectangle(124,45,23,123,fill="blue")
can_wid.create_oval(68,180,45,100)
can_wid.create_text(200,200,text="python")
root.mainloop()

