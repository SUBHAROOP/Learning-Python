a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
def hcfcompute(a,b):
    if (a > b):
       s=a
    else:
        s=b
    for i in range(1,s+1):
        if ((a%i==0)and(b%i==0)):
             gcd=i
    return gcd
print("The Hcf of" ,a,"and" ,b,"Hcf is=",hcfcompute(a,b))


