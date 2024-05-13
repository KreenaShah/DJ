import math

S = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
K = [int(2**32 * abs(math.sin(i + 1))) for i in range(64)]
print(K)
A0 = 0x01234567
B0 = 0x89ABCDEF
C0 = 0xFEDCBA98
D0 = 0x76543210
 
# Auxiliary functions
def F(x, y, z): return (x & y) | (~x & z)
def G(x, y, z): return (x & z) | (y & ~z)
def H(x, y, z): return x ^ y ^ z
def I(x, y, z): return y ^ (x | ~z)
funcs = [F, G, H, I]
 
# Left rotate function
def left_rotate(x, c): return (x << c) | (x >> (32 - c))
 
# MD5 main algorithm
def md5(message):
    message = bytearray(message, 'utf-8')  # Convert the message to bytes
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += orig_len_in_bits.to_bytes(8, byteorder='little')
 
    hash_pieces = [A0, B0, C0, D0]
 
    for chunk_ofst in range(0, len(message), 64):
        a, b, c, d = hash_pieces
        chunk = message[chunk_ofst:chunk_ofst+64]
        for i in range(64):
            f = funcs[i//16](b, c, d)
            g = (i*7 + 1) % 16 if i < 16 else (5*i + 1) % 16 if i < 32 else (3*i + 5) % 16 if i < 48 else (i * 3) % 16
            to_rotate = a + f + K[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
            new_b = (b + left_rotate(to_rotate, S[i])) & 0xFFFFFFFF
            a, b, c, d = d, new_b, b, c
        for i, val in enumerate([a, b, c, d]):
            hash_pieces[i] += val
            hash_pieces[i] &= 0xFFFFFFFF
 
    return ''.join(f'{piece:08x}' for piece in hash_pieces)
 
msg = input("Enter message: ")
print(md5(msg))