class upper:
    def upp(self,n):
        self.num=n
        self.i= 1
        while self.i<=self.num:
            print(" "* (self.num-self.i),end="")
            print("* "*self.i)
            self.i=self.i+1
class low(upper):
    def lo(self):
        self.num=4
        self.i=self.num-1
        while self.i >= 1:
            print(" "*(self.num-self.i),end="")
            print("* " * self.i)
            self.i=self.i-1
            
    

c1=upper()
c1.upp(4)   
c2=low()
c2.lo()   