 
f= lambda x: x if x<=1 else f(x-1)+f(x-2)

for i in range(0,11):
    print(f(i))