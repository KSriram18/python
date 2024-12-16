file =open("Level-3//words.txt","r")
data=file.readlines()
data2=[]
for line in data:
    if 'j' in line:
        line2=line.replace('j','i')
    print(line2)
    data2.append(line2)
file.close()
file1=open("Level-3//words.txt","w")
file1.writelines(data2)   

