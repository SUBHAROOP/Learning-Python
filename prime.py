c=0
i=2
a=int(input('Enter the number:'))
while i < a:
      if (a % i == 0):
           c=c+1
           break;
      else:
           i=i+1
if(c==0):
    print('{} is prime number'.format(a))
else:
     print('{} is composite number'.format(a))
