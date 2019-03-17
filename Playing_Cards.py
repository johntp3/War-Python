from enum import Enum
from enum import IntEnum

full_deck = []
card_names = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
              "jack", "queen", "king", "ace")


# Card enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


# Suit enum for playing cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'


# Class to hold info for playing cards
class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

    def __str__(self):
        card_name = card_names[self.card.value - 1]
        return str(card_name) + " of " + self.suit.value


# function to deal full deck of cards
def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit)))
    return full_deck
