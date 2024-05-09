class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.depth = None

def insertion(head,k):
    print("Calling Insertion Function")
    val = [int(x) for x in input().split()][:k]
    newNode = Node(val)
    temp = head
    depth = 0
    if not temp:
        head = newNode
        newNode.depth = 0
        print("Creating root node at depth 0")
        return head
    while temp:
        compIndex = depth % k
        print("Comparing using Index ",compIndex)
        if temp.val[compIndex] <= val[compIndex] :
            print(" going right at depth ", depth)
            if temp.right:
                temp = temp.right
            else:
                temp.right = newNode
                temp.depth = depth + 1
                return newNode
        else:
            print(" going left at depth ", depth)
            if temp.left:
                temp = temp.left
            else:
                temp.left = newNode
                temp.depth = depth + 1
                return newNode
        depth += 1
    return None

if __name__ == "__main__":
    k = int(input("Enter no. of dimensions : "))
    head = None
    option = 1
    while option!=2:
        option = int(input("Choose option :\n1. Insertion\n2. Exit\n"))
        if option == 1:
            if head is None:
                head = insertion(head,k)
            else:
                newNode = insertion(head,k)