num=int(input())
t=0
while num>0:
        t=t*10+num%10
        num=num//10
        
print(t)