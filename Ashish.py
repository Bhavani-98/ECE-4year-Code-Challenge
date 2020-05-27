print('Enter correct username and password to continue')
count=0
while count<3:
    username=input('Enter username:')
    password=input('Enter password:')
    if username=='Micheal'and password=='e3$WT89x':
            print('You have successfully login')
            break
    else:
          print('Invalid username or password\n')
          count+=1
    if count==3:
           print('Account locked ')
