lst = [4,1,7,9,2,6,8,3]
def odd_and_sum(x):
    l =[]
    for i in x:
        if i % 2 ==0:
            l.append(i)
    for j in l:
        x.remove(j)
    s=sum(x)
    return(x,s)
print('Original list: ',lst)
z = odd_and_sum(lst)
print('New odd list: {0}\nSum of all odd numbers: {1}'.format(z[0],z[1]))