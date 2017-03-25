from deck import Deck

class SolitaireDeck(Deck):
    def _triple_cut(self, first_joker_position, second_joker_position):
        front = self._cards[0:first_joker_position]
        middle = self._cards[first_joker_position:second_joker_position+1]
        back = self._cards[second_joker_position+1:len(self._cards)]

        self._cards = back + middle + front

    def _count_cut(self):
        last_card = self._cards[-1] if self._cards[-1] != 54 else 53

        front = self._cards[0:last_card]
        middle = self._cards[last_card:-1]
        back = self._cards[-1:len(self._cards)]

        self._cards = middle + front + back

    def _get_output_card(self):
        first_card = self._cards[0] if self._cards[0] != 54 else 53

        if self._cards[first_card] == 53 or self._cards[first_card] == 54:
            return None

        return self._cards[first_card]

    def _solitaire(self):
        joker_a_position = self._cards.index(53)
        self._move_card_down(joker_a_position, 1)

        joker_b_position = self._cards.index(54)
        self._move_card_down(joker_b_position, 2)

        joker_a_position = self._cards.index(53)
        joker_b_position = self._cards.index(54)

        if joker_a_position < joker_b_position:
            first_joker_position = joker_a_position
            second_joker_position = joker_b_position
        else:
            first_joker_position = joker_b_position
            second_joker_position = joker_a_position

        self._triple_cut(first_joker_position, second_joker_position)
        self._count_cut()

        return self._get_output_card()

    def generate_keystream(self, keystream_length):
        keystream = []

        for _ in xrange(keystream_length):
            output_card = None
            while output_card == None:
                output_card = self._solitaire()
            keystream.append(output_card)

        return keystream


