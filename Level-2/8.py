st=input()
vowels=['a','e','i','o','u']
count=0
for i in st:
    if i in vowels:
        count+=1
print("Number of vowels:",count)