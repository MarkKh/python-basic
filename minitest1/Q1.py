num = int(input('Enter num = '))
print('Odd number is')
i = 1
sum = 0

while i <= num:
    if i % 2 == 0:
        sum += i
    else:
        print(i, end=' ')
    i += 1
print('\nSum of Even =', sum)
