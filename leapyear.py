a=int(input('Enter the Year:'))
if (a % 4 ==0):
    if (a % 100 == 0):
         if ( a % 400 == 0):
             print('{0}Leap year'.format(a))
         else:
              print('{0} is not Leap year'.format(a))
    else:
        print('{0} is  Leap year'.format(a))
else:
     print('{0} is not Leap year'.format(a))
         
