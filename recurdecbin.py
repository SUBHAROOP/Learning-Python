n=int(input("Enter the Decimal Number:"))
def covbin(n):
    if(n==0):
        return 0
    else:
         return (n%2)+(10*covbin(n//2))
print("Binary is=",covbin(n))        
