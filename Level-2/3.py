l=list(map(int,input().split(",")))
k= int(input())
s=[]
t=0
for i in l:
    p=k-i
    if p<0:
        continue
    else:
        if p in l[t+1:]:
            s.append([i,p])
    t+=1
print("pair count: ",len(s))