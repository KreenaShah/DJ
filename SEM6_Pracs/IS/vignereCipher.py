# len(key) != len(plainText), we repeat characters of key
pt = input("Enter plaintext : ").lower().replace(" ","")
key = input("Enter key : ").lower().replace(" ","")

tempKey = key
i=0
while(len(tempKey)!= len(pt)):
    tempKey+=key[i]
    i += 1
    i %= len(key)

# print(tempKey)
o = ""
for i in range(len(pt)):
    n1 = ord(pt[i])- ord('a')
    n2 = ord(tempKey[i])- ord('a')
    # print(n1,n2)
    sum = (n1 + n2) % 26
    o+=chr(sum + ord('a'))
    
print(o)