row = int(input("Enter num = "))

i = 1
while i <= row :
    j = row
    while j >= i:
        print("*", end = "")
        j -= 1
    print()
    i += 1