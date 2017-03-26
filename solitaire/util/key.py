from json import loads
from json import dumps

def save_key(outfile, key):
    f = open(outfile, 'w')
    f.write(dumps(key))
    f.close()

def load_key(infile):
    f = open(infile, 'r')
    key = loads(f.readline())
    f.close()
    return key
