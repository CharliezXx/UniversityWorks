number = {'0','1','2','3','4','5','6','7','8','9'}
mobile_num = input('Mobile number: ')
print('Your mobile is '+mobile_num)
r = []
for i in range (0,10):
    r += mobile_num[i]
result = set(r)
print(r)
y = 'Missing digit.'+str((number-result)) if number - result != set() else'there is no any missing digit.'
print(y)