# 0 1 1 2 3 5 8 13
n = int(input("Kitne numbers of sequence chahiye bhaiiii : "))
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(n-2):
    temp = num1 + num2
    num1 = num2
    num2 = temp
    print(temp)
