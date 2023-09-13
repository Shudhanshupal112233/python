# class rectangle:
#     l=0
#     b=0

# r1=rectangle()
# r1.l=12
# r1.b=4
# area=r1.l*r1.b
# print(area)


# class method_demo:
#     def display(self):
#         print("welcome")

# d1=method_demo()
# d1.display()       
   
# import math
# class circle:
#     def cal_area(self,radius):
#         print("area of circle:",math.pi*radius**2)

# c1=circle()
# c1.cal_area(5)     


# class pac:
#      x=5 #instance variable 
#      def dis(self,x):
#          x=30
#          print("local variable value:",x)  
#          print("instance variable value:",self.x)   
         
         
# c1=pac()
# c1.dis(67)      

# class self_method:
#     def m1(self):
#         print("in method a")
#     def m2(self):
#         print("in method 2")
#         self.m1()
     
# mm=self_method()
# mm.m2()        

class person:
    name="harry"
    occ="software engineer"
    def info(self):
        print(self.name,"is a", self.occ)
a=person()
a.info()   
b=person()
b.name="sudhanshu pal"
b.occ="scientist"
b.info()     
                     