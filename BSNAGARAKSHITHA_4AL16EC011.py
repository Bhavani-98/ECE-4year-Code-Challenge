password="e3$WT89x"
username="Micheal"

for i in range (3,0,-1):
    user = input("enter usr name:")
    pwd = input("enter password:")
    if (pwd == password) & (user==username):
        break
    else:
        print("incorrect")
if i==1:
    print("account locked")
else:
    print("you have successfully loged in")            
