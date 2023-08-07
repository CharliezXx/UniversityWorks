club,daimond,heart,spade,deck =[],[],[],[],[]
for i in range(1,int((52/4))+1):
    if i==1:
        i= 'A'
    elif i== 11:
        i= 'J'
    elif i== 12:
        i= 'Q'
    elif i== 13:
        i= 'K'
    club.append('{}\u2663'.format(i))
    daimond.append('{}\u2666'.format(i))
    heart.append('{}\u2665'.format(i))
    spade.append('{}\u2660'.format(i))
deck = club+daimond+heart+spade
print('Club = ',club)
print('Daimon = ',daimond)
print('Heart = ',heart)
print('Spade = ',spade)
print('Deck = ',deck)
print('Total card in one deck = ',len(deck))


    