n=int(input())
s=input()
l=[]
m=[]
count=0
final=0
for i in range(len(s)):
    if s[i] not in l:
        if count!=n and s[i] not in m:
            l.append(s[i])
            count+=1
        elif len(m)!=0 and s[i] in m:
            m.remove(s[i])
            final+=1
        else:
            m.append(s[i])
    else:
        count-=1
        l.remove(s[i])
print(final)