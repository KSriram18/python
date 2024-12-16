l=input()
a=[]
lis=[]
for i in range(len(l)):
    if l[i]!='0':
        a.append(l[i])
    else:
        if len(a)!=0:
            lis.append("".join(a))
            a=[]
lis.append("".join(a))
d={}
print(lis)
names=["first_name","last_name","id"]
for i in range(len(names)):
    d[names[i]]=lis[i]
print(d)