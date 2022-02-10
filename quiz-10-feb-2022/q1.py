a = []
print('input number')
for _ in iter(int,1):
    x = int(input())
    if x == -1:
        break
    a.append(x)

print('output is :',sum(a))