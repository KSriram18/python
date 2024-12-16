def findRecursive(n):
    if n==2:
        return 1
    elif n%2==0:
        return findRecursive(n//2)
    else:
        return 0
n=int(input())
print(findRecursive(n)==1)