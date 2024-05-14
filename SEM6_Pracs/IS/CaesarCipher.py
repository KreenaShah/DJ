def encryption(pt):
    o = ""
    for i in range(len(pt)):
        o += chr((((ord(pt[i])-ord('a'))+3)%26)+ord('a'))
    return o

def decryption(ct):
    o = ""
    for i in range(len(pt)):
        o += chr((((ord(ct[i])-ord('a'))-3)%26)+ord('a'))
    return o

pt = input("Enter plain text : ").lower().replace(" ","")
ct = encryption(pt)
print("Encrypted Text : ",ct)
og = decryption(ct)
print("Decrypted Text : ",og)