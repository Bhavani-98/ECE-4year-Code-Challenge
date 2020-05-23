print('Enter correct username and password to continue')
count=1

while count<4:
    username=input('Enter username: ')
    password=input('Enter password: ')
    if password=='e3$WT89x' and username=='Micheal':
        print('Access granted')
        count=5
    else:
        print('Access denied. Try again.')
        count+=1 
if count>3:
 	   print('Account blocked')

