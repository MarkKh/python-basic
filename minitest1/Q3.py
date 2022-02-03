count = int(input('Enter count = '))
a = []
i = 0

while i < count:
    x = int(input())
    a.append(x)
    i += 1
sum = sum(a)
avg = sum/len(a)

print('Sum is =', sum)
print('Mean is = %.2f' % avg)
