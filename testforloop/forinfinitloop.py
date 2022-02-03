a = []
for _ in iter(int,1):
    x = int(input())
    if x == -1:
        break
    a.append(x)

if sum(a) == 0:
    print('no data')
else:
    print(sum(a))