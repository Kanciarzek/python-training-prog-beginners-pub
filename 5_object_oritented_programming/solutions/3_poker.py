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
    def __init__(self, figure: Figure, suite: Suite):
        self.figure = figure
        self.suite = suite


class Hand:

    def __init__(self, card1: Card, card2: Card, card3: Card, card4: Card, card5: Card):
        self._cards = (card1, card2, card3, card4, card5)

    def has_pair(self) -> bool:
        card_figures = [card.figure for card in self._cards]
        return len(set(card_figures)) < 5

    # alternatywne rozwiązanie
    # def has_pair(self) -> bool:
    #     card_figures = [card.figure for card in self._cards]
    #     return any(card.figure in card_figures[i + 1:] for i, card in enumerate(self._cards))

    def has_flush(self) -> bool:
        return all(x.suite == self._cards[0].suite for x in self._cards[1:])

    def has_triple(self) -> bool:
        card_figures = list(Figure)
        counter = dict()
        for figure in card_figures:
            counter[figure] = 0
        for card in self._cards:
            counter[card.figure] += 1
        return any(val >= 3 for val in counter.values())


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
