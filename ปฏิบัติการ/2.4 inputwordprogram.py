condition = False
st = {}
while condition == False:
    n = int(input('How many word? (3-5): 1'))
    if n <3 or n>5:
        print('Invalid number !!!')
    else:
        for i in range(1,n+1):
            s = input('Word {}: '.format(i))
            st.update({s:len(s)})
        condition = True
print('Data in the dictionary: ',st)