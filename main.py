import deck

deck_1 = deck.create_deck()
deck_shuffle = deck.shuffle(deck_1)
hands = deck.deal(deck_shuffle, 4, 5)

print(hands)