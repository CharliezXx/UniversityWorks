ln = '1372567489391'
temp=[]
for i in ln:
    temp.append(i)
ln = temp
print('List---> ',ln)
print('Set---> ',set(ln))
print('Sort---> ',sorted(set(ln)))

even = set({})

for j in sorted(set(ln)):
    if int(j) %2 == 0:
        even.add(j)
print('Even---> ',sorted(even))
    

