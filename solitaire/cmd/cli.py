from solitaire.deck.solitaire import SolitaireDeck
from json import loads
from json import dumps
import click

@click.command()
@click.option('--genkey', is_flag=True, help="Generate a key by shuffling the deck.")
@click.option('--keystream', is_flag=True, help="Generate a keystream.")
@click.option('--length', type=int, help="Desired keystream length.")
@click.option('--infile', help="Path to read key from.")
@click.option('--outfile', help="Path to write generated key to.")
def main(genkey, infile, outfile, keystream, length):
    if genkey:
        if not outfile:
            print("--outfile is required for generating a key.")
            exit(1)
        key_deck = SolitaireDeck()
        key_deck.shuffle()
        key = key_deck.get_deck()
        f = open(outfile, 'w')
        f.write(dumps(key))
        f.close()

    if keystream:
        if not infile:
            print("--infile is required for generating a keystream.")
            exit(1)
        if not length:
            print("--lengh is required for generating a keystream.")
            exit(1)
        key_deck = SolitaireDeck()
        f = open(infile, 'r')
        key_deck.set_deck(loads(f.readline()))
        keystream = key_deck.generate_keystream(length)
        print "Generated keystream of length %d:" % len(keystream)
        print keystream
