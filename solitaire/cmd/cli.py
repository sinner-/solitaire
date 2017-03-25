from solitaire.deck.solitaire import SolitaireDeck
import click

@click.command()
def main():
    key_deck = SolitaireDeck()
    key_deck.shuffle()
    key = key_deck.get_deck()
    keystream = key_deck.generate_keystream(20)
    print keystream
    print len(keystream)
