def factorial(n):
    if n==1:
        return 1
    else:
        n*factorial(int(n)-1)
        
a=int(input("Enter a number only! \n"))
print(factorial(a))