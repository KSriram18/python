a=input().lower()
b=input().lower()
a1 = sorted(a)
b1= sorted(b)
if(len(a1) == len(b1)):
    if(a1 == b1):
        print("True")
    else:
        print("False")

else:
    print("False")