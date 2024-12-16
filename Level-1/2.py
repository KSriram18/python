string=list(input())
a=0
n=0
for i in string:
    if i.isnumeric():
        n+=1
    else:
        a+=1
print("Alphabets: {} numbers: {}".format(a,n))
