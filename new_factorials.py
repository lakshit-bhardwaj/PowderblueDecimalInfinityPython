def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

try:    
    a=int(input('Please enter the number for calculating the factorial \n'))
    print(f'The factorial of the number {a} is {factorial(a)}')
except ValueError:
          print('Please input numbers only.')
