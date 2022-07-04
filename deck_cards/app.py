# 3) will need a card class even though dont know what we are doing with it
class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.rank = rank


# 1) creating a stack or deck of cards
class Deck():

    def __init__(self):
        # 2) what is in a deck of cards: suits and values
        self.suits = ['hearts', 'spades', 'diamonds', 'clubs']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
