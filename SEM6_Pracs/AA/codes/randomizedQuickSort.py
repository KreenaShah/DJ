import random
c=0 # To keep track of the number of comparisons made during the sorting process.
def quickSort(arr):
    global c
    if len(arr) <=1: # base case
        return arr
    else:
        p_index = random.randint(0,len(arr)-1)
        pivot = arr[p_index]
        left = []
        right = []
        for i in range(len(arr)):
            if i!=p_index: # condition to skip the pivot element.The pivot element has already been chosen and will be placed in its correct position in the final sorted list. Therefore, there is no need to compare the pivot element with itself or other elements during the partitioning process. If the pivot element were not skipped during the partitioning process, it would be included in either the left or right partition, violating the partitioning invariant
                c+=1
                if arr[i]<pivot:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
        return quickSort(left) + [pivot] + quickSort(right)

l = [1,2,3,4,5,6,7,8,9,10]
sorted_list = quickSort(l)
print(c)
print(sorted_list)

# Randomized quicksort is a variation of the classic quicksort algorithm, designed to mitigate the algorithm's worst-case performance in certain scenarios.In the standard quicksort implementation, the algorithm's performance can degrade to O(n^2) time complexity when the input array is already sorted or reverse-sorted. This is because the pivot element is always chosen as the first or last element of the partition, leading to highly unbalanced partitions.By introducing randomization in the choice of the pivot element, the algorithm ensures that the partitions are more balanced on average, reducing the likelihood of encountering the worst-case scenario.