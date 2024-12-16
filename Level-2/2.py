n= int(input())
l=[int(input()) for i in range(n)]
d={}
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
m=list(d.keys())
print(m)