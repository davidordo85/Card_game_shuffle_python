suits = ('CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS')
numbers = ('A', '2', '3', '4', '5', '6', '7', 'J', 'Q', 'K')

deck = []

for suit in suits:
    for number in numbers:
        card = number + suit
        deck.append(card)


print(deck) 