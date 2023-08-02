n = [20,10,3,2,1,32,40,59,60]
print('data: {}'.format(n))
index = -1
found = False
low = 0
high = len(n)-1
s_n = sorted(n)
print('sorted data: {}'.format(s_n))
key = int(input('enter key :'))
while low<=high and not found:
    mid = (low+high)//2
    if key == s_n[mid] :
        found = True
        index = mid
    elif key > s_n[mid]:
        low = mid + 1
    else:
        high = mid -1
if index == -1:
    print('cannot find {}'.format(key))
else:
    print('found {} at index {}'.format(key,index))
