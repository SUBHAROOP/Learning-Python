a=str(input("Enter the string:"))
b=reversed(a)
if (list(a)==list(b)):
          print("{0} is Palindrome".format(a))
else:
     print("{0} is not palindrome".format(a))
