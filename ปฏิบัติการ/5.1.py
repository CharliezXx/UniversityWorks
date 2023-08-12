
def str_reverse(str):
    n= len(str)
    b =''
    while n !=0:
        n-=1
        b+=str[n]
    return(b)
s = input('Enter a string: ')
r_s = str_reverse(s)
print('Original string: {}\nReversed string: {}'.format(s,r_s))
        