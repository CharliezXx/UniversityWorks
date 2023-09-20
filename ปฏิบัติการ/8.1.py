s = input('Enter a string: ')
lst = list(s)
print('Original string :',s,'\nUsing function sorted():',sorted(s))
print('Convert string to list :',lst)
print('Using bubble sort')
temp =''
for i in range(0,len(lst)-1):
    print('After Round {}: {}'.format(i+1,lst))
    for j in range(0,len(lst)-i-1):
        if lst[j]>lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
print('Sorted List:',lst)