def hcf(n1,n2):
    if n1<n2:
        min=n1
    else:
        min=n2
    for i in range(1,min):
        if(n1%i==0 and n2%i==0):
            hcf=i 
    return(hcf)            
        
def lcm(n1,n2):
    h=hcf(n1,n2)
    l=(n1*n2)/h
    print("lcm of ",n1,"and",n2,"is",l)

n1=45
n2=12
lcm(n1,n2)

    