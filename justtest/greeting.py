
if __name__ == '__main__':
    
    def add():
        x = int(input(""))
    def test():
        a = 20 
        b = 50
        print(a+b)
        def test_a():
            nonlocal a
            a = 100
            b = 200
            print(a+b)
        test_a()
        print(a)
    a = 5
    b = 5
    test()
    print(__name__)