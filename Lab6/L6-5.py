n = int(input("Enter the number : "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 2
avg = sum / n

print("Sum odd number 1 to", n, "is", sum)
print("Avg odd number 1 to", n, "is", avg)
