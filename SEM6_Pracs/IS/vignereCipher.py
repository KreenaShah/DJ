def encryption(pt,key):
    o = ""
    for i in range(len(pt)):
        x = ord(pt[i])-ord('a')
        y = ord(key[i])-ord('a')
        z = (x+y)%26
        o += chr(z+ord('a'))
    return o

def decryption(ct,key):
    o = ""
    for i in range(len(pt)):
        x = ord(ct[i])-ord('a')
        y = ord(key[i])-ord('a')
        z = (x-y)%26
        o += chr(z+ord('a'))
    return o

# pt = input("Enter plain text : ").lower().replace(" ","")
# key = input("Enter key : ").lower().replace(" ","")
pt = "wearediscoveredsaveyourself"
key = "deceptive"

tempKey = key
i=0
while(len(tempKey)!= len(pt)):
    tempKey+=key[i]
    i += 1
    i %= len(key)

ct = encryption(pt,tempKey)
print("Encrypted Text : ",ct)
og = decryption(ct,tempKey)
print("Decrypted Text : ",og)