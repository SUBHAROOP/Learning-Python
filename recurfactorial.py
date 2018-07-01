n=int(input("Enter the positive Number:"))
def factor(n):
    if(n==1):
        return 1
    else:
         return n*factor(n-1)
print("Factor is=",factor(n))        
