# vignere cipher
plainText = input("Enter plain text : ")
key = input("Enter key : ")
tempKey = key
i=0
while(len(tempKey)!= len(plainText)):
    tempKey+=key[i]
    i+=1
    i= i% (len(key)-1)

print(tempKey)

o = ""
for i in range(len(plainText)):
    n1 = ord(plainText[i])- ord('a')
    n2 = ord(tempKey[i])- ord('a')
    print(n1,n2)
    sum = (n1 + n2) % 26
    o+=chr(sum + ord('a'))
print(o)