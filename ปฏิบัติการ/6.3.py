conversionTable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def dec_To_hex(n):
    if(n<=0):
        return ''
    remainder = n%16
    return  dec_To_hex(n//16)+conversionTable[remainder]
        
decimal = int(input("Enter an integer: "))
print("Decimal {} = {} Hexadecimal ".format(decimal,dec_To_hex(decimal)))