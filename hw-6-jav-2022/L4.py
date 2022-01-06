tt = input().split(' ')
mmm = int(tt[0])
kkk = int(tt[1])-543

if mmm == 2:
     if kkk % 4 == 0 and (kkk % 100 != 0 or kkk % 400 == 0):
          print(29)
     else:
          print(28)
elif mmm == 1 or mmm == 3 or mmm == 5 or mmm == 8 or mmm == 10 or mmm == 12:
     print(31)
else:     
     print(30)