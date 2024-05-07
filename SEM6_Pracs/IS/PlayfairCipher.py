pt = input("Enter plaintext : ").lower().replace("j", "i") # Handling i/j part here itself
key = input("Enter key : ").lower().replace("j", "i")
# pt = "instruments"
# key = "monarchy"

m = []  #this array initially stores all the 25 characters required for the 5x5 matrix, but not in form of matrix

for el in key:
    if el not in m:  # Check if the character is not already in the list
        m.append(el)  # Append the unique character to the list

for i in range(97, 123):
  if chr(i) not in m and chr(i)!='j' and len(m)!=25:
    m.append(chr(i))
# print(m)

# Creating a 5x5 matrix from the user input key and remaining unique alphabets
matrix=[]
for i in range(0,len(m), 5):
    # print(m[i:i+5])
    matrix.append(m[i:i+5]) # slices the list m from index i to i+5, creating a sublist containing at most 5 elements, appending it to matrix ,representing rows of the matrix.
# print(matrix)

# Creating pair of 2 from start, to generate cipher text
# use bogus letters if any pair has similar words, if the last pair just has 1 character
pairs=[]
if len(pt)%2!=0:# odd length
  for i in range(0,len(pt)-1,2):
    if pt[i]!=pt[i+1]:
      pairs.append(pt[i:i+2])
    else:
      pairs.append(pt[i] + 'x')
      pairs.append(pt[i] + 'x')
  pairs.append(pt[-1] + 'x')
else: # even length
  for i in range(0,len(pt),2):
    if pt[i]!=pt[i+1]:
      pairs.append(pt[i:i+2])
    else:
      pairs.append(pt[i] + 'x')
      pairs.append(pt[i] + 'x')

ct=[]
for p in pairs:
    ind1=[0,0] # it will store the row and column indices of 1st character of the pair in the matrix.
    ind2=[0,0] # it will store the row and column indices of 2nd character of the pair in the matrix.
    for j in range(len(matrix)):
        if p[0] in matrix[j]:
            ind1=[j, matrix[j].index(p[0])]
        if p[1] in matrix[j]:
            ind2=[j, matrix[j].index(p[1])]
    if ind1[0] == ind2[0]:
        ct.append(matrix[ind1[0]][(ind1[1]+1)%5] + matrix[ind2[0]][(ind2[1]+1)%5])
    elif ind1[1] == ind2[1]:
        ct.append(matrix[(ind1[0]+1)%5][ind1[1]] + matrix[(ind2[0]+1)%5][ind2[1]])
    else:
        ct.append(matrix[ind1[0]][ind2[1]] + matrix[ind2[0]][ind1[1]])
        
print(''.join(ct))