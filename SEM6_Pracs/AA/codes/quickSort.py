import random
c = 0

def quickSort(arr):
    global c
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(len(arr)):
            if i!=0:
                c+=1
                if arr[i]<pivot:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
        return quickSort(left)+[pivot]+quickSort(right)
    
l = [1,2,3,4,5,6,7,8,9,10]
sorted_list = quickSort(l)
print(c)
print(sorted_list)