# Python program to find the factorial of a number provided by the user.

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)