#!/usr/bin/env python
import random


class Deck(object):
    def __init__(self, deck_size=54):
        self._cards = []
        for card in range(1, deck_size+1):
            self._cards.append(card)

    def shuffle(self):
        for card in range(0, len(self._cards)):
            random.seed()
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

key_deck = Deck()
key_deck.shuffle()
key = key_deck.get()

print "------------------------------"
print "moving jokers:"
joker_a_location = key_deck.find_card(53)
print "'A' joker location: %d" % joker_a_location

key_deck.move_card_down(joker_a_location, 1)
joker_a_location = key_deck.find_card(53)
print "moved 'A' joker to: %d" % joker_a_location

joker_b_location = key_deck.find_card(54)
print "'B' joker location: %d" % joker_b_location

key_deck.move_card_down(joker_b_location, 2)
joker_b_location = key_deck.find_card(54)
print "moved 'B' joker to: %d" % joker_b_location

print "------------------------------"
print "performing triple cut:"
if joker_a_location < joker_b_location:
    first_joker_location = joker_a_location
    second_joker_location = joker_b_location
    print "first joker is 'A' joker: %d" % first_joker_location
    print "second joker is 'B' joker: %d" % second_joker_location
else:
    first_joker_location = joker_b_location
    second_joker_location = joker_a_location
    print "first joker is 'B' joker: %d" % first_joker_location
    print "second joker is 'A' joker: %d" % second_joker_location
temporary_deck = key_deck.get()
print temporary_deck
print temporary_deck[0:first_joker_location]
#TODO: THIS DOESN'T WORK RIGHT FOR SHORT MIDDLE BITS
print temporary_deck[first_joker_location:second_joker_location+1]
print temporary_deck[second_joker_location+1:len(temporary_deck)]
print "------------------------------"
