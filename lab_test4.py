print('===Part1===')
isodd = False
vowels =['a','e','i','o','u','A','E','I','O','U']
NAME = []
proc = ''
temp = ''
count = 0
n = int(input('Enter number(odd number and 1-7):'))
while n<1 or n>7 or n%2 ==0:
    print('Not value want...')
    n = int(input('Enter number(odd number and 1-7):'))
print('===Part2===')
for i in range(0,n):
    s = input('Enter Name[{}]:'.format(i+1))
    NAME.append(s)
print('===Part3===')
for j in range(0,len(NAME)):
    temp = NAME[j]
    for k in range(0,len(temp)):
        if temp[k] != ' ':
            count +=1
        if temp[k] in vowels:
            proc+=temp[k].replace(temp[k],'*')
        else:
            proc += temp[k]
    print('{} and count is {}'.format(NAME[j],count))
    print('Process...==>{}'.format(proc))
    count =0
    proc = ''