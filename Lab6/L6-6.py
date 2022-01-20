sumEvan = 0
sumOdd = 0
while True:
    x = int(input())
    if x != 0:
        if x%2 == 0:
            sumEvan += x
        else:
            sumOdd += x
    else:
        break
print("Sum evan",sumEvan)
print("Sum odd",sumOdd)