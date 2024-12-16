file = open("Level-3\\doc.txt", "r") 
data=file.read()
words=data.split()
s=[]
for i in words:
    if len(i)%2==0:
        s.append(i)
print(" ".join(s))

