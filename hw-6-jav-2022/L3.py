x = []
a,b,c,d,e = input().split(' ')
x.append(a)
x.append(b)
x.append(c)
x.append(d)
x.append(e)

checkSorted = 0
if(x == sorted(x)):
    checkSorted = 1
      

if (checkSorted) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")