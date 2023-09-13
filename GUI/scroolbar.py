from tkinter import *
root=Tk()
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
# list_box = Listbox(root)
# for i in range(344):
#     list_box.insert(END,f" item{i+1}")
# list_box.pack() 
text = Text(root,yscrollcommand = scroll.set)
text.pack()
scroll.config(command=text.yview)   

root.mainloop()


# from tkinter import *
# root = Tk()
# root.geometry("455x233")
# root.title("Scrollbar tutorial")
# # For connecting scrollbar to a widget
# # 1. widget(yscrollcommand = scrollbar.set)
# # 2 scrollbar.config(command=widget.yview)
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)

# # listbox = Listbox(root, yscrollcommand = scrollbar.set)
# # for i in range(344):
# #     listbox.insert(END, f"Item {i}")

# # listbox.pack(fill="both",padx=22 )
# text = Text(root, yscrollcommand = scrollbar.set)
# text.pack(fill=BOTH)
# # scrollbar.config(command=listbox.yview)
# scrollbar.config(command=text.yview)

# root.mainloop()