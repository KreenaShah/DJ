def vernamEncryption(pt,key):
    o = ""
    # for i in range(len(pt)):
    #     x = ord(pt[i])-ord('a')
    #     y = ord(key[i])-ord('a')
    #     z = x^y
    #     w = z%26
    #     print(x,y,z,w)
    #     o += chr(w + ord('a'))
    o = ''.join(chr(((ord(pt[i]) - ord('a')) ^ (ord(key[i]) - ord('a'))) + ord('a')) for i in range(len(pt)))
    return o

def vernamDecryption(ct,key):
    o = ""
    for i in range(len(ct)):
        x = ord(ct[i])-ord('a')
        y = ord(key[i])-ord('a')
        z = x^y
        w = z%26
        print(x,y,z,w)
        o += chr(w + ord('a'))
    # o = ''.join(chr(((ord(ct[i]) - ord('a')) ^ (ord(key[i]) - ord('a'))) + ord('a')) for i in range(len(ct)))
    return o

# len(key) == len(plainText)
# pt = input("Enter plaintext : ").lower().replace(" ","")
# key = input("Enter key (same as length of plain text) : ").lower().replace(" ","")
pt = "kcds"
key = "sdth"

if len(key) != len(pt):
    print("Length of plaintext and key should be the same")
else:
    encryptedText = vernamEncryption(pt,key)
    print("Encrypted Text : ",encryptedText)
    decryptedText = vernamDecryption(encryptedText,key)
    print("Decrypted Text : ",decryptedText)