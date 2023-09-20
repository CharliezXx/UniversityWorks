class Fac():
    def loop(x):
        result = x
        print('Calculate Factorial Using Loop\n{}! = '.format(x),end='')
        for i in range(x,0,-1):
            if i != 1:
                result = result*(i-1)
                print(i,'*',sep='',end='')
            else:
                print(i)
        print('{}! = {}'.format(x,result))
    def recursive(x,result=1,c=0):
        if result ==1 :
            print('Calculate Factorial Using Recursion\n{}! = '.format(x),end='')
        if x>1:
            result,c = result*(x) , c+1
            print(x,'*',sep='',end='')
            return(x*Fac.recursive(x-1,result,c))
        else:
            print('1 \n{}! = {}'.format((c+1),result))
            return 1