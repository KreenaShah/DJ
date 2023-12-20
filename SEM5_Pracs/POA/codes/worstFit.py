def worstFit(blockSize, m, processSize, n): 
    allocation = [-1] * n
    for i in range(n):
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1:
                    wstIdx = j
                elif blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
        if wstIdx != -1:
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i]
    print("Process ID","  |  Process Size |","Block Allocated")
    print("-------------------------------------------------")
    for i in range(n):
        if allocation[i] != -1:
            print(i+1,"           |",processSize[i],"          |",allocation[i]+1)
        else:
            print(i+1,"           |",processSize[i],"          |","Not Allocated")

blockSize = [100, 500, 200, 300, 600] 
processSize = [212, 417, 112, 426] 
m = len(blockSize) 
n = len(processSize) 
worstFit(blockSize, m, processSize, n)