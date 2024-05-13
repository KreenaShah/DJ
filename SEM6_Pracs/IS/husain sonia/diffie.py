def isPriRoot(i, n):
    temp = set()
    for j in range(1, n):
        if (i**j) % n in temp:
            return False
        temp.add((i**j) % n)
    return True


def primitive_root(n):
    for i in range(2, n):
        if isPriRoot(i, n):
            return i


p = int(input("Enter a prime number p: "))
alpha = primitive_root(p)
print("Primitive root (alpha): ", alpha)
pri_key_A = int(input("Enter private key of A: "))
pri_key_B = int(input("Enter private key of B: "))

pub_key_A = (alpha**pri_key_A) % p
pub_key_B = (alpha**pri_key_B) % p

print("Public key of A: ", pub_key_A)
print("Public key of B: ", pub_key_B)

key_A = (pub_key_B**pri_key_A) % p
key_B = (pub_key_A**pri_key_B) % p

print("Key A: ", key_A)
print("Key B: ", key_B)

if key_A == key_B:
    print("Key exchange successful.")
else:
    print("Unsuccessful.")


# ----------------------------------

# g = int(input("Enter g: "))
# p = int(input("Enter p: "))
# a = int(input("For user 1, input a: "))
# b = int(input("For user 2, input b: "))
# xa = (g**a) % p
# xb = (g**b) % p
# print("User1 will send Xa = ",xa," to user2")
# print("User2 will send Xb = ",xb," to user1")
# Ak = (xb**a) % p
# Bk = (xa**b) % p
# print("Ak is found to be ",Ak)
# print("Bk is found to be ",Bk)
# if Ak==Bk:
#     print("Both can communicate further")
# else:
#     print("Communication cannot continue")