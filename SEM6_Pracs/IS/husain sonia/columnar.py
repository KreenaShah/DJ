def encrypt(plain_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cipher_text = ''
    padding_length = len(key) - (len(plain_text) % len(key))
    if padding_length != len(key):
        plain_text += 'X' * padding_length
    for i in key_order:
        cipher_text += ''.join(plain_text[i::len(key)])
    return cipher_text

def decrypt(cipher_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    plain_text = [''] * len(cipher_text)
    pos = 0
    for i in key_order:
        for j in range(len(key)-1):
            plain_text[i + j * len(key)] = cipher_text[pos]
            pos += 1
    return ''.join(plain_text)

pt = "wearediscoveredfleeatonce"
key = "zebras"

cipher_text = encrypt(pt, key)
print("Cipher text:", cipher_text)
decrypted_text = decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)