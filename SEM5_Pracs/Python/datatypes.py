list1 = ["apple", "banana", "cherry", 12, 12.0, 44j]
tupple1 = ("apple", "banana", "cherry", 12, 12.0, 44j)

# print(list1[0])
# print(tupple1[0])

x = {"name" : "John", "age" : 36}
# print(x.keys())
# print(x.values())
# print(x.items())
# print(x["name"])

first_key = next(iter(x))
print(iter(x),"hhhh",next(iter(x)))
first_value = x[first_key]
print("First key-value pair:", {first_key: first_value})

# for key, val in x.items():
#     print(key,val)