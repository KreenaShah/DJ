def bestFit(blockSize, m, processSize, n):
    allocation = [-1]*n
    for i in range(n):
        bestIndex = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIndex == -1:
                    bestIndex = j
                elif blockSize[bestIndex] > blockSize[j]:
                    bestIndex = j
        if bestIndex != -1:
            allocation[i] = bestIndex
            blockSize[bestIndex] -= processSize[i]
    print("Process ID","  |  Process Size |","Block Allocated")
    print("-------------------------------------------------")
    for i in range(n):
        if allocation[i] != -1:
            print(i+1,"           |",processSize[i],"          |",allocation[i] + 1)
        else:
            print(i+1,"           |",processSize[i],"          |","Not Allocated")

blockSize = [100, 500, 200, 300, 600] 
processSize = [212, 417, 112, 426] 
m = len(blockSize) 
n = len(processSize) 
bestFit(blockSize, m, processSize, n)
