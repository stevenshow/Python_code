suits = ('\u2660','\u2665','\u2666','\u2663')
ranks =('2','3','4','5','6','7','8','9','10','J','Q','K','A')

cards = []

'''for rank in ranks:
    for suit in suits:
        cards.append((rank,suit))
print(cards)
'''
cards = [(rank,suit) for rank in ranks for suit in suits]
print(cards)