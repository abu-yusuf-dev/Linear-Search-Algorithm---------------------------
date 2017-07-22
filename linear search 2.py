#Author:Yusuf
list=[2,3,5,7,8,10]
print("The list is : ",list)
i=flag=0
a=int(input("Enter the item you want to search : "))

while i<len(list):
    if a==list[i]:

        flag=1
        break
    i=i+1
if flag==1:
    print("Your item is in ",i+1,"th Position")
else:
    print("Sorry! your item isn't exit here.")


