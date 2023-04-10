import deck

# create deck
deck_1 = deck.create_deck()

# shuffle deck
deck_shuffle = deck.shuffle(deck_1)

# hands of the players, (deck to be dealt, number of players, number of decks)
hands = deck.deal(deck_shuffle, 4, 5)

print(hands)