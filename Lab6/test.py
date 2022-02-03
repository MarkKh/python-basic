x = int(input())
sum = 0
while x!=0:
    if x%3 == 0 or x%5==0:
        sum+=x
    x = int(input())
print(sum)