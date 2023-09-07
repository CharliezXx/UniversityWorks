class Fac:
    def loop(x):
        n,temp=0,1
        print('Calculate Factorial Using loop\n{}! = '.format(x),end='')
        for i in range(1,x+1):
            if x-n == 1:
                print(x-n)
            else:
                print(x-n,'*',sep='',end='')
                temp = temp*(x-n)
            n+=1
        print('{}! = {}'.format(x,temp))
    def recursive(x,n=0):
        n+=1
        if x>1:
            print(x,'*',sep='',end='')
            return (x* Fac.recursive(x-1,n)) 
        else:  
            print(x,'\n{}! ='.format(n),end =' ')
            return 1