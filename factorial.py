a=int(input('Enter the number:'))
c=1
if(a>0):
        for i in range (1,a+1):
              c=c*i
        print ('Factorial is ={0}'.format(c))
       
elif(a==0):
     print('Factorial is 1')
else:
     print('Number is negative Factorial is not possible')
