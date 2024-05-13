def remove_spaces(text):
    return ''.join(text.split())

def pad_text(text, key_length):
    padding_length = key_length - (len(text) % key_length)
    if padding_length != key_length:
        text += 'X' * padding_length
    return text

def encrypt(plain_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cipher_text = ''
    plain_text = remove_spaces(plain_text)
    plain_text = pad_text(plain_text, len(key))
    for i in key_order:
        cipher_text += ''.join(plain_text[i::len(key)])
    return cipher_text

def decrypt(cipher_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cols = len(cipher_text) // len(key)
    plain_text = [''] * len(cipher_text)
    pos = 0
    for i in key_order:
        for j in range(cols):
            plain_text[i + j * len(key)] = cipher_text[pos]
            pos += 1
    return ''.join(plain_text)

# Example usage
plaintext = "hello"
key = "his"

cipher_text = encrypt(plaintext, key)
print("Cipher text:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)

# -------------------------------------------

# import math
# pt = input("Enter Plaintext: ").replace(' ', '').lower()
# key = input("Enter key: ")
# copy = key
# keylen = len(key)
# ptlen = len(pt)
# sortedkey = list(sorted(key))
# ind = []
# for i in range(keylen):
#     ind.append(sortedkey.index(key[i])+1)
#     if ind.count(ind[i])>1:
#         ind[i] += 1
# print(ind)
# fill = []
# ptr=0
# for i in range(math.ceil(ptlen/keylen)):
#     temp = []
#     for i in range(keylen):
#         if ptr >= ptlen:
#             break
#         temp.append(pt[ptr])
#         ptr += 1
#     if ptr >= ptlen:
#         while(ptr%keylen!=0):
#             temp.append('x')
#             ptr += 1
#         fill.append(temp)
#         break
#     fill.append(temp)
# print(fill)
# ans = ""
# check = [False]*keylen
# for x in range(keylen):
#     p = -1
#     min = 99999999
#     for i in range(keylen):
#         if ind[i]<min and not check[i]:
#             min = ind[i]
#             p = i
#     check[p] = True
#     for arr in fill:
#         ans += arr[p]
# print("Cipher text is: ", ans)
# mat = []
# ptr=0
# for i in range(keylen):
#     temp = []
#     for j in range(math.ceil(ptlen/keylen)):
#         temp.append(ans[ptr])
#         ptr += 1
#     mat.append(temp)
# print(mat)
# rest = ""
# for i in range(math.ceil(ptlen/keylen)):
#     for j in range(keylen):
#         rest += mat[ind[j]-1][i]
# print("Deciphered text is: ", rest)