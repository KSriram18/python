l=input()
a=[]
b=[]
count =0
for i in range(len(l)):
    if len(a)==0:
        a.append(l[i])
        count+=1
    elif l[i]==a[-1]:
        count+=1
    else:
        b.append(count)
        a.append(l[i])
        count=1
b.append(count)
s=''
for i in range(len(a)):
    s=s+a[i]+str(b[i])
print(s)