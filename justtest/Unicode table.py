for i in range (65,90+1):
    h,o = hex(i)  , oct(i)
    print('{} {} {} {}'.format(i,h[2:4],o[2:5],chr(i)))