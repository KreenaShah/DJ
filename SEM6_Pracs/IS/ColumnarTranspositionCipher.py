def encryption(pt,key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    ct = ""
    if len(pt)%len(key)!=0:
        padding_length = len(key) - (len(pt) % len(key))
        pt += 'X' * padding_length
    for i in key_order:
        ct += ''.join(pt[i::len(key)])
    return ct

def decryption(ct,key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    plain_text = [''] * len(ct)
    pos = 0
    for i in key_order:
        for j in range(len(key)-1):
            plain_text[i + j * len(key)] = ct[pos]
            pos += 1
    return ''.join(plain_text)

# pt = input("Enter plain text : ").lower().replace(" ","")
# key = input("Enter key : ").lower().replace(" ","")
pt = "wearediscoveredfleeatonce"
key = "zebras"
ct = encryption(pt,key)
print("Encrypted Text : ",ct)
og = decryption(ct,key)
print("Decrypted Text : ",og)