def twosComplement(num):
    onesComp="" 
    for i in num:
        if i == "0":
            onesComp += "1"
        else:
            onesComp +="0"
    return bin(int(onesComp,2) + int("1",2)).replace('0b',"")

# Taking input
num1 = int(input('Enter multiplier(M): '))
num2 = int(input('Enter multiplicand(Q): '))
print(num1,num2)

# Absolute lena padega, since yaha hum negative numbers ko handle nai kar rahe
binNum1 = bin(abs(num1)).replace("0b",'')
binNum2 = bin(abs(num2)).replace("0b",'')
print(binNum1,binNum2)

if len(binNum1) > len(binNum2):
    maxLen = len(binNum1)
else:
    maxLen = len(binNum2)
maxLen = maxLen+1
print("maxLen",maxLen)

binNum1 = binNum1.zfill(maxLen)
binNum2 = binNum2.zfill(maxLen)
print("Filling 0's to left to match lengths",binNum1,binNum2)

# Handling negative numbers
if num1 < 0:
    binNum1 = twosComplement(binNum1)
elif num2 < 0:
    binNum2 = twosComplement(binNum2)
print("If any negative input values, then we are taking it's complement",binNum1,binNum2)

# Since we need complement(M) in the algorithm, we'll take 2's complement of binNum1
binCompNum1 = twosComplement(binNum1)
binCompNum1 = binCompNum1.zfill(maxLen)

count = maxLen
m = binNum1
minusM = binCompNum1
q = binNum2
q1 = 0
a = '0'
a = a.zfill(maxLen)
