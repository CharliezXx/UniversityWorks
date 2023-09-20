class Low_Up_String():
    def lower(s):
        result=''
        for i in range(0,len(s)):
            if ord(s[i]) < 97 and not ord(s[i])==32:
                x = ord(s[i])+32
                result+=chr(x)
            else:
                result+=s[i]
        return result
    
    def upper(Z):
        result=''
        for i in range(0,len(Z)):
            if ord(Z[i]) >= 97 and not ord(Z[i])==32:
                x = ord(Z[i])-32
                result+=chr(x)
            else:
                result+=Z[i]
        return result
