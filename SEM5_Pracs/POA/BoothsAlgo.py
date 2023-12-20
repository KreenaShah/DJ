print("Booth's Algorithm (Signed Multiplication)")

num1 = int(input("Enter multiplicand(M) : "))
num2 = int(input("Enter multiplier(Q) : "))
# print(num1,num2)

# Converting decimal numbers to binary
bin1 = bin(num1).replace("0b", "")
bin2 = bin(num2).replace("0b", "")
# print(bin1,bin2)