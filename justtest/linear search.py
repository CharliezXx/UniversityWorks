n = [10,20,31,21,32,5,64]
index = -1
j= -1
key = int(input('Enter key:'))
for i in n :
    j +=1
    if i == key:
        index = j
        break
if index == -1:
    print('cannot find {} in data'.format(key))
else:
    print('found {} on index {}'.format(key,index))