# 6)
from random import randint


# 3) will need a card class even though dont know what we are doing with it


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        # 4) ex of Poker, how to turn 13 into a King or 1 into ace
        if value == 11:
            self.rank = 'Jack'
        elif value == 12:
            self.rank = 'Queen'
        elif value == 13:
            self.rank = 'King'
        elif value == 1:
            self.rank = 'Ace'
        else:
            self.rank = str(value)
    # 6

    def __repr__(self):
        return f"{self.value}{self.suit[0]}"

    def __str__(self):
        return f"{self.rank} of {self.suit}"

        # 1) creating a stack or deck of cards


class Deck():

    def __init__(self):
        # 2) what is in a deck of cards: suits and values
        self.suits = ['hearts', 'spades', 'diamonds', 'clubs']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # 5) property to keep track of what is in the deck
        self.contents = []

        # for suit in self.suits:
        #     for value in self.values:
        #         self.contents.append(Card(suit, value))

        self.contents = [Card(suit, value)
                         for suit in self.suits for calue in values]

        # 7) swap deck of cards
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]


new_deck = Deck()

print(new_deck.contents)
print(new_deck.contents[0])
