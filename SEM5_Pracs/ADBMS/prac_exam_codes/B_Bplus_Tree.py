from BTrees.IIBTree import IIBTree
import time

def print_menu():
    print("***BTree***")
    print("1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")
    return input("Enter your choice : ")

bTree = IIBTree(order = 2)

while True:
    choice = print_menu()

    if choice == "1":
        value = int(input("Enter the element to be inserted"))
        bTree.insert(value,value)
        print(f'Element {value} is inserted into B Tree')
    elif choice == "2":
        val = int(input("Enter the element to be searched : "))
        start = time.time()
        if val in bTree:
            print(f'{val} is found in the tree')
            end = time.time()
            searchTime = end - start
            print(f'Search took {searchTime} seconds')
        else:
            print("Value not found in tree")
    elif choice == "3":
        print("BTree")
        print(list(bTree.items()))
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")