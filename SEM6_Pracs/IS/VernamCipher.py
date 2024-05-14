def encryption(pt,key):
    o = ""
    for i in range(len(pt)):
        x = ord(pt[i])-ord('a')
        y = ord(key[i])-ord('a')
        z = (x^y)%26
        o += chr(z + ord('a'))
    return o

def decryption(ct,key):
    o = ""
    for i in range(len(ct)):
        x = ord(ct[i])-ord('a')
        y = ord(key[i])-ord('a')
        z = (x^y)%26
        o += chr(z + ord('a'))
    return o

# pt = input("Enter plain text : ").lower().replace(" ","")
# key = input("Enter key (same as plaintext length) : ").lower().replace(" ","")
pt = "hey"
key = "sun"
ct = encryption(pt,key)
print("Encrypted Text : ",ct)
og = decryption(ct,key)
print("Decrypted Text : ",og)