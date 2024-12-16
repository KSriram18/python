l=list(map(int,input().split(",")))
k= int(input())
a=l[k+1:]+l[:k+1]
print("arr after rotation =",a)