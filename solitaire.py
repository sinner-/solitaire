#!/usr/bin/env python
import random


class Deck(object):
    def __init__(self, deck_size=54):
        self._cards = []
        self._deck_size = deck_size
        for card in range(1, self._deck_size+1):
            self._cards.append(card)

    def shuffle(self):
        for card in range(0, len(self._cards)):
            random.seed()
            swapcard = random.randrange(0, self._deck_size)
            self.swap_card(card, swapcard)

    def swap_card(self, card, swapcard):
        tmp = self._cards[card]
        self._cards[card] = self._cards[swapcard]
        self._cards[swapcard] = tmp

    def get(self):
        return self._cards

    def get_card(self, card):
        return self._cards[card]

    def find_card(self, find_card):
        for card in range(0, len(self._cards)):
            if self._cards[card] == find_card:
                return card

    def move_card_down(self, original_position, distance):
        self._cards.insert(1+original_position+distance, self._cards[original_position])
        del(self._cards[original_position])

key_deck = Deck()
key_deck.shuffle()
key = key_deck.get()

first_joker_location = key_deck.find_card(53)
print "first_joker: %d" %first_joker_location

key_deck.move_card_down(first_joker_location, 1)
moved_joker_location = key_deck.find_card(53)
print "moved first_joker to: %d" % moved_joker_location

second_joker_location = key_deck.find_card(54)
print "second_joker: %d" % second_joker_location

key_deck.move_card_down(second_joker_location, 2)
moved_joker_location = key_deck.find_card(54)
print "moved second_joker to: %d" % moved_joker_location

