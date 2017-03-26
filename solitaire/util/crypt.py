def encrypt_message(keystream, text):
    output = []
    for k,t in zip(keystream, list(text)):
        output.append(chr(65 + ((k + (ord(t)-65)) % 26)))

    return ''.join(output)

def decrypt_message(keystream, text):
    output = []
    for k,t in zip(keystream, text):
        output.append(chr(65 + (((ord(t)-65) - k) % 26)))

    return ''.join(output)
