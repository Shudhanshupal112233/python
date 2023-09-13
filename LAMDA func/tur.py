# x=lambda a,b,c:a*b*c
# print(x(5,5,5))

l=[2,54,6,43,64,3,21,12,3]

adlts=list(filter(lambda a: a%2==0,l))

for i in adlts:
    print(i)