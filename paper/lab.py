# l1=[1,2,3]
# l2=[4,5,6]
# l3=l1+l2
# print(l3)

# list=[1,2,3,4,5,6]
# print(list[:4])

# n=int(input("enter the no:"))
# s=n
# rev=0
# while(n>0):
#     r=n%10
#     rev= rev*10+r
#     n=n//10
    
# if(s==rev):
#     print("no is palindrome")
# else:
#     print("not a palindrome")  


# def rev(string):
#   w =string.split()
#   w = list(reversed(w))
#   return " ".join(w)

# string= "hello shudhanshu"
# print(rev(string))


# l=[1,2,3,4]
# l1=sum(l)
# print(l1)

# def search_list(lst, element):
#     count = lst.count(element)
#     index = lst.index(element)
#     return count, index

# lst = [1, 2, 3, 4, 5, 2]
# element = 2
# count, index = search_list(lst, element)
# print(f"Number of occurrences of {element}: {count}")
# print(f"Index of first appearance of {element}: {index}")

# def search_list(lst,ele):
#     count = lst.count(ele)
#     index = lst.index(ele)
#     return count,index

# lst= [1,2,4,6,2,5,2]
# ele=2
# count, index= search_list(lst,ele)
# print(f"Number of occurrences of {ele}: {count}")
# print(f"Index of first appearance of {ele}: {index}") 

# n = int(input('Enter the number of rows: '))

# # printing upper triangle
# i = 1
# while i <= n:
#     print(" " * (n - i), end="")
#     print("* " * i)
#     i += 1

# # printing lower triangle
# i = n - 1
# while i >= 1:
#     print(" " * (n - i), end="")
#     print("* " * i)
#     i -= 1



# class upper:
#     def upp(self,n):
#         self.num=n
#         self.i= 1
#         while self.i<=self.num:
#             print(" "* (self.num-self.i),end="")
#             print("* "*self.i)
#             self.i=self.i+1
# class low(upper):
#     def lo(self):
#         self.num=4
#         self.i=self.num-1
#         while self.i >= 1:
#             print(" "*(self.num-self.i),end="")
#             print("* " * self.i)
#             self.i=self.i-1
            
    

# c1=upper()
# c1.upp(4)   
# c2=low()
# c2.lo()   

# class employee      
        
        
class upper:
    def __init__(self,n):
        self._num=n      
        
a= upper("ani")
print(a._num)