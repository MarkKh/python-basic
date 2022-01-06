x = input().split(' ')
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])
x4 = int(x[3])

value = x1 + x2 + x3 + x4 - max(x1, x2, x3, x4) - min(x1, x2, x3, x4)
print(value)