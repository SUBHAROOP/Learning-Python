a=float(input('Enter triangle first side:'))
b=float(input('Enter triangle second side:'))
c=float(input('Enter triangle third side:'))
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))**0.5
print('Area of triangle is=%0.2f'%d)
