
naam = input("enter the name:")
accno = int(input("enter the account no.:"))
acctype = input("enter type of account:")
balance = float(input("enter the balance:"))

class bank_acc:
    def __init__(self,naam,accno,acctype,balance):
        self.naam=naam
        self.accno=accno
        self.acctype=acctype
        self.balance=balance
        
    def create_acc(self):
        print("ACCOUNT DETAILS:")
        print("NAME:",self.naam,
              "\n ACCOUNT NO.",self.accno,"\n ACCOUNT TYPE:",self.acctype,"\nBALANCE:",self.balance)
        
        
p1=bank_acc(naam,accno,acctype,balance)
p1.create_acc()
        