# vernam cipher
plainText = input("Enter plain text : ")
key = input("Enter key : ")

if(len(key)!= len(plainText)):
    print("Length of plain text and key should be of same length")

o = ""
for i in range(len(plainText)):
    print(ord(plainText[i]),ord(key[i]))
    b1 = bin(ord(plainText[i]))
    b2 = bin(ord(key[i]))
    print(b1,b2,type(b1))
    val = int(b1, 2) ^ int(b2, 2)
    print("xor",val)
    o += chr(val)
    
print(o)