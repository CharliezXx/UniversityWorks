card =('A','1','2','3','4','5','6','7','8','9','10','J','Q','K')
club,daimond,heart,spade,deck =[],[],[],[],[]
for i in card:
    club.append(i+'\u2663')
    daimond.append(i+'\u2666')
    heart.append(i+'\u2665')
    spade.append(i+'\u2660')
deck = club+daimond+heart+spade
print('Club = ',club)
print('Daimon = ',daimond)
print('Heart = ',heart)
print('Spade = ',spade)
print('Deck = ',deck)
print('Total card in one deck = ',len(deck))
