sum = 0
while True:
    x = int(input())
    if x != 0:
        if x%3 == 0 or x%5 == 0:
            sum += x #sum = sum + x
    else:
        break
print("Sum is",sum)