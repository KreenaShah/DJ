def VignereEncryption(pt,key):
    o = ""
    for i in range(len(pt)):
        n1 = ord(pt[i])- ord('a')
        n2 = ord(key[i])- ord('a')
        o+=chr((n1 + n2) % 26 + ord('a'))
    return o

def VignereDecryption(ct,key):
    o = ""
    for i in range(len(ct)):
        n1 = ord(ct[i])- ord('a')
        n2 = ord(key[i])- ord('a')
        o+=chr((n1 - n2) % 26 + ord('a'))
    return o

# len(key) != len(plainText), we repeat characters of key
pt = input("Enter plaintext : ").lower().replace(" ","")
key = input("Enter key : ").lower().replace(" ","")
# pt = "wearediscoveredsaveyourself"
# key = "deceptive"

tempKey = key
i=0
while(len(tempKey)!= len(pt)):
    tempKey+=key[i]
    i += 1
    i %= len(key)

encryptedText = VignereEncryption(pt,tempKey)
print("Encrypted Text : ",encryptedText)
decryptedText = VignereDecryption(encryptedText,tempKey)
print("Decrypted Text : ",decryptedText)