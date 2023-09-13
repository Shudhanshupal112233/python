import random
user=int(input("0 for snake \n 1 for water \n 2 for gun:"))
comp= random.randint(0,2)
def check(user,comp):
    if user==comp:
        return 0
    if (comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1
    else :
        return 1
    
print("\ncomputer ",comp)
score=check(user,comp)    
if score==0:
    print("no one wins")
elif score ==-1:
    print("you lose")
elif score ==1:
    print("you wins")       
     