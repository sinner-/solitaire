import random

class Deck(object):
    def __init__(self, deck_size=54):
        self._cards = []
        for card in range(1, deck_size+1):
            self._cards.append(card)

    def _swap_card(self, card, swapcard):
        tmp = self._cards[card]
        self._cards[card] = self._cards[swapcard]
        self._cards[swapcard] = tmp

    def _move_card_down(self, original_position, distance):
        self._cards.insert((original_position+distance)%len(self._cards), self._cards.pop(original_position))

    def shuffle(self):
        random.seed()
        for card in range(0, len(self._cards)):
            swapcard = random.randrange(0, len(self._cards))
            self._swap_card(card, swapcard)

    def get_deck(self):
        return self._cards

    def set_deck(self, cards):
        self._cards = cards
