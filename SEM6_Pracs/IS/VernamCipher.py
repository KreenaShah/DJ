# len(key) == len(plainText)
pt = input("Enter plaintext : ").lower().replace(" ","")
key = input("Enter key : ").lower().replace(" ","")
o = ""

if(len(key)!= len(pt)):
    print("Length of plain text and key should be of same length")
else:
    for i in range(len(pt)):
        b1 = bin(ord(pt[i]))
        b2 = bin(ord(key[i]))
        val = int(b1, 2) ^ int(b2, 2)
        o += chr(val)
    print(o)