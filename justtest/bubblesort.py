n = [3,54,7,2,4,88,34,10,11]

print('Before bubble sort : {}'.format(n))
for i in range(0,len(n)-1):
    for j in range(0,len(n)-i-1):
        if n[j]> n[j+1]:
            temp = n[j]
            n[j] = n[j+1]
            n[j+1] = temp
    print('After bubble sort {} : {}'.format(i+1,n))