a=int(input("Enter lower limit:"))
b=int(input("Enter upper range: "))
for num in range(2,b+1):
    if num>1:
       for i in range(2,num):
           if(num %i==0):
              break
       else:
            print(num)
   
