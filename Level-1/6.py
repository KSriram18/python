n=int(input())
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
if s==n:
    print("{} is a perfect number".format(s))
else:
    print("No")