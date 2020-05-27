print("*********************************************************************") 
password = "" 
username = "" 
count = 0 
while password!='e3$WT89x' and username!='Micheal' and count < 3: 
    username = input("Enter username: ") 
    password = input("Enter password: ") 
 
    if password=='e3$WT89x' and username=='Micheal': 
     print('You have Logged in Sucsessully') 
     break 
 
    else: 
        print('Invalid username/password\n') 
        count+=1 
  
