#!/usr/bin/env python
import random


class Deck(object):
    def __init__(self, deck_size=54):
        self._cards = []
        for card in range(1, deck_size+1):
            self._cards.append(card)

    def shuffle(self):
        random.seed()
        for card in range(0, len(self._cards)):
            swapcard = random.randrange(0, len(self._cards))
            self.swap_card(card, swapcard)

    def swap_card(self, card, swapcard):
        tmp = self._cards[card]
        self._cards[card] = self._cards[swapcard]
        self._cards[swapcard] = tmp

    def get(self):
        return self._cards

    def set(self, cards):
        self._cards = cards

    def get_card(self, card):
        return self._cards[card]

    def find_card(self, find_card):
        return self._cards.index(find_card)

    def move_card_down(self, original_position, distance):
        self._cards.insert((original_position+distance)%len(self._cards), self._cards.pop(original_position))

    def triple_cut(self, first_joker_position, second_joker_position):
        front = self._cards[0:first_joker_position]
        middle = self._cards[first_joker_position:second_joker_position+1]
        back = self._cards[second_joker_position+1:len(self._cards)]

        self._cards = back + middle + front

key_deck = Deck()
key_deck.shuffle()
key = key_deck.get()

print "------------------------------"
print "moving jokers:"
joker_a_position = key_deck.find_card(53)
print "'A' joker position: %d" % joker_a_position

key_deck.move_card_down(joker_a_position, 1)
joker_a_position = key_deck.find_card(53)
print "moved 'A' joker to: %d" % joker_a_position

joker_b_position = key_deck.find_card(54)
print "'B' joker position: %d" % joker_b_position

key_deck.move_card_down(joker_b_position, 2)
joker_b_position = key_deck.find_card(54)
print "moved 'B' joker to: %d" % joker_b_position

# CRITICAL: Must re-find 'A' joker as its position relative to 'B' joker has now changed
joker_a_position = key_deck.find_card(53)

print "------------------------------"
print "performing triple cut:"
if joker_a_position < joker_b_position:
    first_joker_position = joker_a_position
    second_joker_position = joker_b_position
    print "first joker is 'A' joker: %d" % first_joker_position
    print "second joker is 'B' joker: %d" % second_joker_position
else:
    first_joker_position = joker_b_position
    second_joker_position = joker_a_position
    print "first joker is 'B' joker: %d" % first_joker_position
    print "second joker is 'A' joker: %d" % second_joker_position

key_deck.triple_cut(first_joker_position, second_joker_position)
print "------------------------------"
print "------------------------------"
