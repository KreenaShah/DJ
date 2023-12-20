def fifo( pages, capacity):
    page_faults=0
    s=set()
    indexes=[]
    for i in pages:
        if len(s) < capacity:
            if i not in s:
                s.add(i)
                page_faults +=1
                indexes.append(i)
        else:
            if i not in s:
                s.remove(indexes[0])
                page_faults +=1
                indexes.pop(0)
                indexes.append(i)
                s.add(i)
    return page_faults

pages = [7,0,1,2,0,3,0,4,2,3,0,3,2]
capacity=4
print(fifo(pages,capacity))