def multiplication():
    try:
        num=int(input('Enter the number'))
    except ValueError:
        print('Please enter a number only!')
        print('Using default value 2, printing table')
        num=2
    finally:
        for i in range(1,11):
            print(num*i)


multiplication()