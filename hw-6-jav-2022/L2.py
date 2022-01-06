inp_chest = int(input())

if inp_chest < 37:
    print('Your size is XS')
elif inp_chest>=37 and inp_chest<42:
    print('Your size is M')
elif inp_chest>=41 and inp_chest<43:
    print('Your size is L')
elif inp_chest>=43 and inp_chest<46:
    print('Your size is L')
else:
    print('Your size is XL')