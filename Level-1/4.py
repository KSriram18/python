start=int(input("Enter the starting number"))
stop=int(input("Enter the stoping number"))
odd=[i for i in range(start,stop+1) if i%2!=0]
sum=0
for i in odd:
    sum+=i
print("Sum of odd numbers: ",sum)