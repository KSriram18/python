Physics=int(input("Enter Physics Marks\n"))
Chemistry=int(input("Enter Chemistry Marks\n"))
Biology=int(input("Enter Biology Marks\n"))
Mathematics=int(input("Enter Mathematics Marks\n"))
Computer=int(input("Enter Computer Marks\n"))
s= Physics+Chemistry+Biology+Mathematics+Computer
perc=(s*100)/500
if perc>=90:
    grad="A"
elif perc>=80:
    grad="B"
elif perc>=70:
    grad="C"
elif perc>=60:
    grad="D"
elif perc>=40:
    grad="E"
else:
    grad="F"
print(grad)