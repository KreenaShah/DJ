def playFairEncryption(pt,matrix):
  pairs=[]
  if len(pt)%2!=0:# odd length
    for i in range(0,len(pt)-1,2):
      if pt[i]!=pt[i+1]:
        pairs.append(pt[i:i+2])
      else:
        pairs.append(pt[i] + 'x')
        pairs.append(pt[i+1] + 'x')
    pairs.append(pt[-1] + 'x')
  else: # even length
    for i in range(0,len(pt),2):
      if pt[i]!=pt[i+1]:
        pairs.append(pt[i:i+2])
      else:
        pairs.append(pt[i] + 'x')
        pairs.append(pt[i+1] + 'x')

  ct = ""

  for p in pairs:
    ind1=[0,0] # it will store the row and column indices of 1st character of the pair in the matrix.
    ind2=[0,0] # it will store the row and column indices of 2nd character of the pair in the matrix.
    for j in range(len(matrix)):
        if p[0] in matrix[j]:
            ind1=[j, matrix[j].index(p[0])]
        if p[1] in matrix[j]:
            ind2=[j, matrix[j].index(p[1])]
    if ind1[0] == ind2[0]: # same row
        ct += (matrix[ind1[0]][(ind1[1]+1)%5] + matrix[ind2[0]][(ind2[1]+1)%5])
    elif ind1[1] == ind2[1]: # same column
        ct += (matrix[(ind1[0]+1)%5][ind1[1]] + matrix[(ind2[0]+1)%5][ind2[1]])
    else:
        ct += (matrix[ind1[0]][ind2[1]] + matrix[ind2[0]][ind1[1]])
  return ct

def playFairDecryption(ct, matrix):
    pairs = [ct[i:i+2] for i in range(0, len(ct), 2)]  # Break ciphertext into digraphs
    pt = ""

    for p in pairs:
        ind1 = [0, 0]  # Store the row and column indices of the 1st character of the pair in the matrix
        ind2 = [0, 0]  # Store the row and column indices of the 2nd character of the pair in the matrix
        for j in range(len(matrix)):
            if p[0] in matrix[j]:
                ind1 = [j, matrix[j].index(p[0])]
            if p[1] in matrix[j]:
                ind2 = [j, matrix[j].index(p[1])]
        if ind1[0] == ind2[0]: # same row
            pt += matrix[ind1[0]][(ind1[1] - 1) % 5] + matrix[ind2[0]][(ind2[1] - 1) % 5]
        elif ind1[1] == ind2[1]:  # same column
            pt += matrix[(ind1[0] - 1) % 5][ind1[1]] + matrix[(ind2[0] - 1) % 5][ind2[1]]
        else:
            pt += matrix[ind1[0]][ind2[1]] + matrix[ind2[0]][ind1[1]]
    return pt

# pt = input("Enter plaintext : ").lower().replace("j", "i") # Handling i/j part here itself
# key = input("Enter key : ").lower().replace("j", "i")
pt = "instruments"
key = "monarchy"

m = []  #this array initially stores all the 25 characters required for the 5x5 matrix, but not in form of matrix
[m.append(el) for el in key if el not in m] # Check if the character is not already in the list 'm' & Append the unique character to the list
[m.append(chr(i)) for i in range(97, 123) if chr(i) not in m and chr(i) != 'j' and len(m) != 25] # Append remaining unique characters of alphabet

# Creating a 5x5 matrix from the user input key and remaining unique alphabets
matrix = [m[i:i+5] for i in range(0, len(m), 5)] # slices the list m from index i to i+5, creating a sublist containing at most 5 elements, appending it to matrix ,representing rows of the matrix.

encryptedText = playFairEncryption(pt,matrix)
print("Encrypted Text : ",encryptedText)
decryptedText = playFairDecryption(encryptedText,matrix)
print("Decrypted Text : ",decryptedText)