def lcm(n1,n2,n):
    gcd=0
    for i in range(1,n):
        if n1%i==0 and n2%i==0:
            if i>gcd:
                gcd=i
    l=(n1*n2)//gcd
    return l
a=int(input())
b=int(input())

if a>b:
    l=lcm(a,b,b)
    print("LCM of {} and {} are:{}".format(a,b,lcm(a,b,b)))
else:
    l=lcm(a,b,a)
    print("LCM of {} and {} are:{}".format(a,b,lcm(a,b,a)))