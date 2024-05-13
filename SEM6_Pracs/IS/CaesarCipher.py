def caesarCipherEncryption(pt):
    ct = ""
    for i in pt:
        ct += chr(((ord(i)-ord('a')) + 3)%26 + ord('a'))
    return ct

def caesarCipherDecryption(ct):
    og = ""
    for i in ct:
        og += chr(((ord(i)-ord('a')) - 3)%26 + ord('a'))
    return og

# pt = input("Enter plaintext : ").lower()
pt = "meet"
print("Original Text : ",pt)
encryptedText = caesarCipherEncryption(pt)
print("Encrypted Text : ",encryptedText)
decryptedText = caesarCipherEncryption(pt)
print("Decrypted Text : ",caesarCipherDecryption(encryptedText))