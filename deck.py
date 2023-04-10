import random

suits = ('CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS')
numbers = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10' 'J', 'Q', 'K')

def create_deck():
    deck = []
    for suit in suits:
        for number in numbers:
            card = number + suit
            deck.append(card)

    return deck

def shuffle(deck):
    totalCards = len(deck)
    deckShuffle = []
    i = 0
    while i < totalCards:
        card = random.randint(0, totalCards - 1)
        while deck[card] in deckShuffle:
            card = random.randint(0, totalCards -1)
        deckShuffle.append(deck[card])
        i += 1
    deck = deckShuffle
    return deckShuffle

def deal(deck, numPlayer, numCards):
    hand = []
    for player in range(numPlayer):
        hand.append([])

    for indexCard in range(numCards):
        for indexPlayer in range(numPlayer):
            card = deck.pop(0)
            hand[indexPlayer].append(card)

    return hand