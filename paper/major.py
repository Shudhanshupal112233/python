# from tkinter import *
# from random import choice
# root=Tk()


# # f1= Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
# # f1.pack()
# # l=Label(f1,text="submit").pack()
# # def color():
# #     pass
# def color():
#     f1.config(bg="red")
    
# f1= Frame(root,bg="red",borderwidth=6)
# f1.pack()
# Button(text="submit",command=color).pack()
# root.mainloop()


# l=[]
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         l.append(i)
# print(l)

# class student:
#     def __init__(self,name,roll) :
#          self.name=name
#          self.roll=roll
#     def setage(self,age):
#         self.age=age
#     def setmarks(self,e,h):
#         self.eng=e
#         self.hindi=h
#     def display(self):
#         print(f" rollno. is{self.roll}\nname:{self.name}\n age: {self.age}\n english marks:{self.eng}")   
        
# s1=student("ani",1)
# s1.setage(20)
# s1.setmarks(34,45)
# s1.display()

# string=input("Enter string:")
# count1=0
# count2=0
# for i in string:
#       if(i.isdigit()):
#             count1=count1+1
#       count2=count2+1
# print("The number of digits is:")
# print(count1)
# print("The number of characters is:")
# print(count2)


# st= input("enter string")
# c1=0
# c2=0
# for i in st:
#     if(i.isdigit()):
#         c1=c1+1
#     c2=c2+1
# print("number:",c1)
# print("alphabet",c2)       


# class Person:
#   def __init__(myobject, name, age):
#     myobject.name = name
#     myobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()
# class person:
#     def __init__(self,f,l):
#         self.fnaam=f
#         self.lnam=l
#     def view1(self):
#         print(self.fnaam,self.lnam)
# class student(person):
#     def __init__(self, f, l):
#         person.__init__(self,f,l)
#         self.year=2
#     def view(self):
#         print(f"name is {self.fnaam} and last name is {self.lnam} is learing python since {self.year}")
        
        
# s=student("ani","mishra")
# s.view()
# s.view1()


# class sem1:
#     def __init__(self,cgpa1) :
#         self.cgpa1=cgpa1
#     def view1(self):
#          print("sem1 cgpa :",self.cgpa1)
# class sem2:
#       def __init__(self,cgpa2) :
#         self.cgpa2=cgpa2
#       def view2(self):
#          print("sem2 cgpa :",self.cgpa2)  
# class year(sem1,sem2):
#     def __init__(self,cgpA1,cgpa2):
#         self.cgpa1=cgpA1
#         self.cgpa2=cgpa2
#     def score(self):
#         self.sgpa= (self.cgpa1+self.cgpa2)/2
#         print("total sgpa of 1st year is :",self.sgpa)    
        
# y=year(7.6,8.45)
# y.score()    
# y.view1()  
                
        
# print(len("banana"))

# pre='hdbshbdbd'
# # npre= pre.find("b")
# if pre.i
# su="ack"
# for i in pre:
#     print(i+su)

            


