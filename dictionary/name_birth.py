dic1={
    "ani":" 17 june",
    "oja":"12 may",
    "sudha":"5 aug"
}
print("we have birth dates of fooloowing people:")
for x in dic1:
    print(x)

user=input("enter the name:")
if user in dic1:
    print(dic1[user])    