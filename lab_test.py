print('---Part 1 ---')
n = int(input('How many integer (5-10): '))
while n > 10 or n < 5:
    print('Must be 5 to 10')
    n = int(input('How many integer (5-10): '))
print('--- Part 2 ---')
num =[]
for i in range(1,n+1):
    x = int(input('Number {} = '.format(i)))
    num.append(x)
print('Number =',num)
print('--- Part 3 ---')
s=[]
for j in range(1,len(num)+1):
    print('Number {} ==> {}'.format(j,num[j-1]))
    if int(num[j-1]) % 2 == 1:
        print('	{} is an odd number and it is not added.'.format(num[j-1]))
    else:
        print('	{} added'.format(num[j-1]))
        s.append(num[j-1])
print('Sum of even numbers is {}.'.format(sum(s)))
