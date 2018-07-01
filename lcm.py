a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
def Lcmcompute(a,b):
    if (a > b):
       s=a
    else:
        s=b
    for i in range(1,s+1):
        if ((a%i==0)and(b%i==0)):
             gcd=i
             lcm=(a*b)//gcd
    return lcm
print("The Lcm of" ,a,"and" ,b,"Lcm is=",Lcmcompute(a,b))


