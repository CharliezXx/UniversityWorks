s = input('Enter a string: ')

def str_count(x):
    upper,lower=0,0
    
    for i in x:
        if i.isupper() == True:
            upper+=1
        elif i.islower() == True:
            lower +=1
    l=[lower,upper]
    return(l)

m = str_count(s)
print('Original string: ',s)
print('Total lower case characters: {}'.format(m[0]))
print('Total upper case characters: {}'.format(m[1]))