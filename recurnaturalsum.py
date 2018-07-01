n=int(input("Enter Number of terms:"))
def naturalsum(n):
    if(n==1):
        return 1
    else:
         return n+naturalsum(n-1)
print("Natural sumi is=",naturalsum(n))        
