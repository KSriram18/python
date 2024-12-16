Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
d={}
for i in Input_list:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print("Frequency count:",d)