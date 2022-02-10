try:
    x = int(input('Enter your number : '))
    y = 10/x
except ArithmeticError:
    print('found the errors in arithmetic.')
else:
    print('not find the errors in arithmetic.')
    print(y)