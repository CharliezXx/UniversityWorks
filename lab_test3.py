print('====Part1====')
n = int(input('Enter number(2-10):'))
while n<2 or n>10:
    n = int(input('Enter number(2-10):'))
print('====Part2====')
name =[]
lastname =[]
str_n=''
LNF=[]
for i in range(0,n):
    s = input('Enter String[{}]:'.format(i+1))
    name.append(s)
    s = s.split(' ')
    lastname.append(s[1])
    str_n=lastname[i]
    LNF.append(str_n[0])
print('====Part3====')
for j in range(0,len(name)):
    print('Name[{}]:{}'.format(j+1,name[j]))
    print('Last Name First char is \'{}\'.'.format(LNF[j]))
    print('ACII value is {}.\n'.format(ord(LNF[j])))