n= int(input())
l=[]
m=[]
for i in range(n):
    l.append(int(input()))
for j in range(n):
    m.append(int(input()))
s=[]
for i in l:
    if i in m:
        s.append(i)
print(s)
        