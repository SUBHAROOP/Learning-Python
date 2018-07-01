a=int(input('Enter the first number:'))
b=int(input('Enter the Second number:'))
c=int(input('Enter the Third number:'))
if ( a > b and a > c):
    print ("{} is greatest number".format(a))
elif ( a < b and b > c):
    print ("{} is greatest number".format(b))

else:
     print ("{} is greatest number".format(c))
