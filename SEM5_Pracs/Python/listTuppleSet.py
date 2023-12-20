# list1 = [1,"kreena",True,9.9]
# tuple1 = (1,"kreena",True,9.9)
# set1 = {1,"kreena",True,9.9}

# print(list1,tuple1,set1)
# list1.append(12+7j)

# temp = list(tuple1)
# temp.append(12+7j)
# tuple1 = tuple(temp)

# set1.add(12+7j)
# print(list1,tuple1,set1)
# ------------------------------------------------
# n = int(input("Enter number of elements : ")) 
# # list1  tuple1  set1 
# list1 = list()
# set1 = set()
# tuple1 = tuple()
# for i in range(n):
#     x = input()
#     list1.append(x)
#     set1.add(x)

#     temp = list(tuple1)
#     temp.append(x)
#     tuple1 = tuple(temp)
# print(list1,set1,tuple1)
# ------------------------------------------------
l = int(input("Size of list: "))
print("Enter list elements:")
List = list(map(int, input().split()))[:l]
print(List)

s = int(input("Size of set: "))
print("Enter set elements:")
Set = set(list(map(int, input().split()))[:s])
print(Set)

t = int(input("Size of tuple: "))
print("Enter tuple elements:")
Tuple = tuple(list(map(int, input().split()))[:t])
print(Tuple)



