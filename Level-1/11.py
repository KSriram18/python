num=int(input())
s=num
while s>=10:
    t=0
    while num>0:
        t+=num%10
        num=num//10
    s=t      
    num=t
print("Final Output:",s) 