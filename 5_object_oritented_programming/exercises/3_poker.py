# Uzupełnij poniższy program tak, aby klasa Card przyjmowała figurę (Figure) i kolor karciany (spade),
# a klasa Hand przyjmowała 5 kart i miała zaimplementowane metody has_pair (zwraca True, gdy mamy parę w
# ręce jednej figury), has_triple (zwraca True gdy mamy trzy karty o tej samej figurze) oraz has_flush
# (zwraca True, gdy mamy w ręce karty jednego koloru).
from enum import Enum


class Figure(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    KNIGHT = 11
    QUEEN = 12
    KING = 13


class Suite(Enum):
    SPADES = "SPADES"
    CLUBS = "CLUBS"
    DIAMONDS = "DIAMONDS"
    HEARTS = "HEARTS"


class Card:
    pass


class Hand:
    pass


if __name__ == '__main__':
    spades_ace: Card = Card(Figure.ACE, Suite.SPADES)
    spades_four: Card = Card(Figure.FOUR, Suite.SPADES)
    clubs_four: Card = Card(Figure.FOUR, Suite.CLUBS)
    hearts_five: Card = Card(Figure.FIVE, Suite.HEARTS)
    spades_six: Card = Card(Figure.SIX, Suite.SPADES)
    spades_seven: Card = Card(Figure.SEVEN, Suite.SPADES)
    hearts_seven: Card = Card(Figure.SEVEN, Suite.HEARTS)
    diamonds_seven: Card = Card(Figure.SEVEN, Suite.DIAMONDS)
    spades_king: Card = Card(Figure.KING, Suite.SPADES)

    random_flush_hand: Hand = Hand(spades_ace, spades_four, spades_seven, spades_six, spades_king)
    assert not random_flush_hand.has_pair()
    assert not random_flush_hand.has_triple()
    assert random_flush_hand.has_flush()

    full_house_hand: Hand = Hand(clubs_four, spades_four, diamonds_seven, hearts_seven, spades_seven)
    assert full_house_hand.has_pair()
    assert full_house_hand.has_triple()
    assert not full_house_hand.has_flush()
