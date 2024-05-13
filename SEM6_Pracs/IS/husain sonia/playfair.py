def enc_playfair(plain,matrix):
    plain += "0"
    plain = plain.replace('j', 'i')
    cipher = ""
    counter = 0
    while(True):
        if plain[counter] == "0":
            break
        if plain[counter] == plain[counter+1] or plain[counter+1] == "0":
            if plain[counter] == "x" and plain[counter+1] == "x":
                plain = plain[:counter+1] + "a" + plain[counter+1:]
            elif plain[counter] == 'x' and plain[counter+1] == '0':
                plain = plain[:counter+1] + "a" + plain[counter+1:]
            else:
                plain = plain[:counter+1] + "x" + plain[counter+1:]
        tp_st = ""
        pos = [0,0]
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == plain[counter]:
                    pos[0] = [i,j]
                elif matrix[i][j] == plain[counter+1]:
                    pos[1] = [i,j]
                else:
                    continue
        if pos[0][0] == pos[1][0]:
            if pos[0][1] == 4:
                pos[0][1] = -1
            if pos[1][1] == 4:
                pos[1][1] = -1
            tp_st +=  matrix[pos[0][0]][pos[0][1]+1]
            tp_st +=  matrix[pos[1][0]][pos[1][1]+1]
        elif pos[0][1] == pos[1][1]:
            if pos[0][0] == 4:
                pos[0][0] = -1
            if pos[1][0] == 4:
                pos[1][0] = -1
            tp_st +=  matrix[pos[0][0]+1][pos[0][1]]
            tp_st +=  matrix[pos[1][0]+1][pos[1][1]]
        else:
            tp_st +=  matrix[pos[0][0]][pos[1][1]]
            tp_st +=  matrix[pos[1][0]][pos[0][1]]
        cipher += tp_st
        counter += 2
    return cipher
 
def dec_playfair(plain,matrix,n):
    cipher = ""
    plain += "0"
    counter = 0
    while(True):
        if plain[counter] == "0":
            break
        tp_st = ""
        pos = [0,0]
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == plain[counter]:
                    pos[0] = [i,j]
                elif matrix[i][j] == plain[counter+1]:
                    pos[1] = [i,j]
                else:
                    continue
        if pos[0][0] == pos[1][0]:
            if pos[0][1] == 0:
                pos[0][1] = 5
            if pos[1][1] == 0:
                pos[1][1] = 5
            tp_st +=  matrix[pos[0][0]][pos[0][1]-1]
            tp_st +=  matrix[pos[1][0]][pos[1][1]-1]
        elif pos[0][1] == pos[1][1]:
            if pos[0][0] == 0:
                pos[0][0] = 5
            if pos[1][0] == 0:
                pos[1][0] = 5
            tp_st +=  matrix[pos[0][0]-1][pos[0][1]]
            tp_st +=  matrix[pos[1][0]-1][pos[1][1]]
        else:
            tp_st +=  matrix[pos[0][0]][pos[1][1]]
            tp_st +=  matrix[pos[1][0]][pos[0][1]]
        cipher += tp_st
        counter += 2
    des = len(cipher) - 1
    while(len(cipher) > n):
        if cipher[des] == "x":
            if des == len(cipher)-1:
                cipher = cipher[:des]
            elif cipher[des-1] == cipher[des+1]:
                cipher = cipher[:des]+cipher[des+1:]
        elif cipher[des] == "a":
            if des == len(cipher)-1:
                cipher = cipher[:des]
            elif cipher[des-1] == 'x' and cipher[des+1]=='x':
                cipher = cipher[:des]+cipher[des+1:]
        des -= 1
    return cipher

plain = input("Enter the plain text: ").lower()
# key = input("Enter the key: ").lower()
matrix =[['m','o','n','a','r'],
       ['c','h','y','b','d'],
       ['e','f','g','i','k'],
       ['l','p','q','s','t'],
       ['u','v','w','x','z']
       ]
print(matrix)
cipher = enc_playfair(plain, matrix)
print("The Ciper text is ", cipher)
dec = dec_playfair(cipher, matrix, len(plain))
print("The Decrypted text is ", dec)
if "i" in dec:
    dec = dec.replace("i","j")
    print("The Decrypted text is ", dec)
elif "j" in dec:
    dec = dec.replace("j","i")
    print("The Decrypted text is ", dec)
else:
    pass