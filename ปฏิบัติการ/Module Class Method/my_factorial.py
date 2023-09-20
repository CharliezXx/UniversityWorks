class Fac:
    def loop(x):
        print('{}! = '.format(x),end='')
        for i in range(x+1,1,-1):
            x= x*(i-1)
            if i == 1:
                print(i-1)
            else:
                print(i-1,end='*')
        print(x,'! = ',x,sep='')
        return ''
    def recursive(c):
        if c > 0 :
            return c*Fac.recursive(c-1)
        return 1