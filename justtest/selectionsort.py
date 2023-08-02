n = [31,23,21,4,64,5,7,9,8]
for i in range (0,len(n)-1):
    key = i
    for j in range(i+1,len(n)):
        if n[key] > n[j]:
            key = j
    temp = n[i]
    n[i] = n[key]
    n[key] = temp
    print(n)           