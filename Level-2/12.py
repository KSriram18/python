userName=input("Enter a username")
originalPassword="Password@123"
password=input("Enter a password")
count=1
while (originalPassword!=password) and count<3:
    password=input("Enter a password")
    count+=1
if originalPassword==password:
    print('Access granted')
else:
    print("3 attempts completed")