


def dectobin(n):
   l1=[]
   while(n!=0):
     r=n%2
     n=n//2
     l1.append(r)
   l1.reverse()   
   print(l1)  

n=int(input("enter the number:"))  
dectobin(n)