# Manual Page 34
# def histogram(l):
#     list1 =[]
#     finalList = []
#     l_set = set(l)
#     for i in l_set:
#         list1.clear()
#         list1.append(i)
#         list1.append(l.count(i))
#         tuple1 = tuple(list1)
#         finalList.append(tuple1)
#     return finalList

# l = [13,12,11,13,14,13,7,7,13,14,12]
# partA = histogram(l)
# print(partA)

# for i in range(len(partA)):
#     print(partA[i][1])

# Manual Page 35
# def perf(n):
#     sum = 0
#     for i in range(1,n+1):
#         if n%i == 0:
#             if n!= i:
#                 sum += i
#     if sum != n:
#         return False
#     else:
#         return True

# n = int(input("Enter a number : "))
# print(perf(n))

# Tower of Hanoi
# def hanoi(n, source, auxiliary, target):
#     if (n == 1):
#         print("Move disk 1 from peg {} to peg {}".format(source, target))
#         return
#     hanoi(n - 1, source, target, auxiliary)
#     print("Move disk {} from peg {} to peg {}".format(n, source, target))
#     hanoi(n - 1, auxiliary, source, target)
# hanoi(int(input("Enter the number of disks: ")), 'A', 'B', 'C')

# map, filter, anonymous function
x = [1,2,3,4,5,6]
result = list(map(lambda a : a**2 if a%2 != 0 else a,x))
# print(result)

num1 = 4
num2 = 6
max = (lambda num1,num2 : num1 if num1 > num2 else num2)(num1,num2)
print(max)

y = ['a','b','c']

