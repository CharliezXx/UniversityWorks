n = input('Enter numbers separated by a space: ')
l1 = list(n.split(' '))
l2 = set(l1)
n_l2 = list(l2)
if len(l1) != len(n_l2) :
    print(l1)
    print('Some numbers are repeated!!!')
else:
    print(l1)
    print('All number are different.')