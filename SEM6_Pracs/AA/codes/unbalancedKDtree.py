class TreeNode:
    def __init__(self, val=None, depth=None):
        self.depth = depth
        self.val = val
        self.right = None
        self.left = None

def insertion(head, k):
    print("Creating a new node ")
    val = [int(x) for x in input().split()][:k]
    print(val,"value")
    newNode = TreeNode(val)
    print(" new node is created ")
    depth = 0
    temp = head
    if temp is None:
        head = newNode
        head.depth = 0
        print(" created head of tree at depth 0")
        return newNode
    while temp:
        compIndex = depth % k
        print(" comparing index is ", compIndex)
        if temp.val[compIndex] <= val[compIndex]:
            print(" going right at depth ", depth)
            if temp.right:
                temp = temp.right
            else:
                temp.right = newNode
                newNode.depth = depth + 1
                return newNode
        else:
            print(" going left at depth ", depth)
            if temp.left:
                temp = temp.left
            else:
                temp.left = newNode
                newNode.depth = depth + 1
                return newNode
        depth += 1
    return None

if __name__ == "__main__":
    head = None
    option = 1
    maxdepth = 0
    print("Enter the no. of dimensions ")
    k = int(input())
    while option != 4:
        print("enter the option ")
        option = int(input())
        if option == 1:
            print("calling node creation ")
            if not head:
                head = insertion(head, k)
            else:
                newNode = insertion(head, k)
        elif option == 2:
            print(maxdepth, " is the depth of the tree ")