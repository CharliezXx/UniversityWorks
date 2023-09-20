import my_low_up_string
s = input('Enter a string: ')
low = my_low_up_string.Low_Up_String.lower(s)
up = my_low_up_string.Low_Up_String.upper(s)
print(up,low,sep='\n')