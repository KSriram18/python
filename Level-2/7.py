l=list(map(int,input().split(",")))
l=sorted(l)
n=len(l)//2
if len(l)%2==0:
    m=(l[n-1]+l[n])/2
    print("Median:",m)
else:
    print("Median:",l[n])