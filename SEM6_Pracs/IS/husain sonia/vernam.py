def ascCon(ch):
    return ord(ch)-65

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        a1= ascCon(string[i])
        a2 = ascCon(key[i])       
        xor = a1 ^ a2
        if(xor > 25):
            ans = xor - 26 + 97
        else:
            ans = xor + 97
        cipher_text.append(chr(ans))
    return ("". join(cipher_text))

if __name__ == "__main__":
    plain_text = input("Enter plain text: ")
    keyword = input("Enter keyword: ") 
    if len(plain_text) == len(keyword):
        cipher_text = cipherText(plain_text, keyword)
        print("Ciphertext:", cipher_text)