# try:
#     x = 7
#     print(x)
# except:
#     print("An exception occurred")
# else:
#     print("else")
# finally:
#     print("finally")

# try:
#     print(x)
# except:
#     print("An exception occurred")
# else:
#     print("else")
# finally:
#     print("finally")

value = 29
class HighValueError():
    pass
class LowValueError():
    pass
try:
    n = int(input("Enter a number: "))

    if n > value:
        raise HighValueError
    elif n < value:
        raise LowValueError
except:
    LowValueError : print("low")
    HighValueError : print("high")
else : print("nice")

