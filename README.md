# Solitaire Cipher

Python implementation of Solitaire Cipher from Cryptonomicon (book by Neal Stephenson, cipher by Bruce Schneier).

## Pre-requisites
 * python virtualenvwrapper

## Install
 * `mkvirtualenv solitaire`
 * `python setup.py install`

## Usage
 * `workon solitaire`
 * `solitaire --genkey --outfile /tmp/key`
 * ``ENCRYPTED_MSG=`solitaire --encrypt --keyfile /tmp/key --message DONOTUSEPC` ``
 * `echo $ENCRYPTED_MSG`
 * `solitaire --decrypt --keyfile /tmp/key --message $ENCRYPTED_MSG`
