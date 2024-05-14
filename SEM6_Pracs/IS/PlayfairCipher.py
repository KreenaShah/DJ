def encryption(pt,m):
    pairs = []
    if len(pt)%2!=0:
        for i in range(0,len(pt)-1,2):
            if pt[i]!=pt[i+1]:
                pairs.append(pt[i:i+2])
            else:
                pairs.append(pt[i]+'x')
                pairs.append(pt[i+1]+'x')
        pairs.append(pt[-1]+'x')
    else:
        for i in range(0,len(pt),2):
            if pt[i]!=pt[i+1]:
                pairs.append(pt[i:i+2])
            else:
                pairs.append(pt[i]+'x')
                pairs.append(pt[i+1]+'x')
    o = ""
    for p in pairs:
        c1 = [0,0]
        c2 = [0,0]
        for j in range(len(m)):
            if p[0] in m[j]:
                c1 = [j,matrix[j].index(p[0])]
            if p[1] in m[j]:
                c2 = [j,matrix[j].index(p[1])]
        if c1[0]==c2[0]: # same row
            o += m[c1[0]][(c1[1]+1)%5] + m[c2[0]][(c2[1]+1)%5]
        elif c1[1]==c2[1]: # same column
            o += m[(c1[0]+1)%5][c1[1]] + m[(c2[0]+1)%5][c2[1]]
        else:
            o += m[c1[0]][c2[1]] + m[c2[0]][c1[1]]
    return o

def decryption(ct,m):
    pairs = []
    [pairs.append(ct[i:i+2]) for i in range(0,len(ct),2)]
    o = ""
    for p in pairs:
        c1 = [0,0]
        c2 = [0,0]
        for j in range(len(m)):
            if p[0] in m[j]:
                c1 = [j,matrix[j].index(p[0])]
            if p[1] in m[j]:
                c2 = [j,matrix[j].index(p[1])]
        if c1[0]==c2[0]: # same row
            o += m[c1[0]][(c1[1]-1)%5] + m[c2[0]][(c2[1]-1)%5]
        elif c1[1]==c2[1]: # same column
            o += m[(c1[0]-1)%5][c1[1]] + m[(c2[0]-1)%5][c2[1]]
        else:
            o += m[c1[0]][c2[1]] + m[c2[0]][c1[1]]
    return o

# pt = input("Enter plaintext : ").lower().replace("j", "i") # Handling i/j part here itself
# key = input("Enter key : ").lower().replace("j", "i")
pt = "instruments"
key = "monarchy"

m=[]
[m.append(el) for el in key if el not in m]
[m.append(chr(i)) for i in range(97,123) if chr(i) not in m and chr(i)!='j' and len(m)!=25]
matrix = [m[i:i+5] for i in range(0,len(m),5)]

ct = encryption(pt,matrix)
print("Encrypted Text : ",ct)
ct = "gatlmzclrqxa"
og = decryption(ct,matrix)
print("Decrypted Text : ",og)