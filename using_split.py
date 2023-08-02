def Fac(x):
    """Heloooooooooo"""
    fac = 1
    for i in range(1,x+1):
        fac = fac*i
        
    return fac
    

y = int(input('Enter number :'))
result = Fac(y)
print(result)

