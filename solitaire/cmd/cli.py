from solitaire.deck.solitaire import SolitaireDeck
from solitaire.util.key import save_key
from solitaire.util.key import load_key
from solitaire.util.crypt import encrypt_message
from solitaire.util.crypt import decrypt_message
import click

@click.command()
@click.option('--genkey', is_flag=True, help="Generate a key by shuffling the deck.")
@click.option('--keystream', is_flag=True, help="Generate a keystream.")
@click.option('--encrypt', is_flag=True, help="Encrypt a message.")
@click.option('--decrypt', is_flag=True, help="Decrypt a message.")
@click.option('--message', help="Message to encrypt or decrypt.")
@click.option('--length', type=int, help="Desired keystream length.")
@click.option('--keyfile', help="Path to read key from.")
@click.option('--outfile', help="Path to write generated key to.")
def main(genkey, keystream, encrypt, decrypt, message, length, keyfile, outfile):
    if genkey:
        if not outfile:
            print("--outfile is required for generating a key.")
            exit(1)
        key_deck = SolitaireDeck()
        key_deck.shuffle()
        save_key(outfile, key_deck.get_deck())

    if keystream:
        if not keyfile:
            print("--keyfile is required for generating a keystream.")
            exit(1)
        if not length:
            print("--length is required for generating a keystream.")
            exit(1)

        key_deck = SolitaireDeck()
        key_deck.set_deck(load_key(keyfile))
        keystream = key_deck.generate_keystream(length)

        print(keystream)

    if encrypt or decrypt:
        if not message:
            print("--message is required for message encryption/decryption.")
            exit(1)
        if not keyfile:
            print("--keyfile is required for message encryption/decryption.")
            exit(1)

        key_deck = SolitaireDeck()
        key_deck.set_deck(load_key(keyfile))
        keystream = key_deck.generate_keystream(len(message))

        if encrypt:
            print(encrypt_message(keystream, message))
        if decrypt:
            print(decrypt_message(keystream, message))
