class MultiPopStack:
    def __init__(self):
        self.stack = []
        self.total_cost = 0  # Total cost of all operations
        self.operations = 0  # No of operations

    def push(self, val):
        print(val,"pushed in Stack")
        self.stack.append(val)
        self.total_cost += 1  # Increment total cost
        self.operations +=1  # Increment no of operations

    def pop(self):
        if not self.stack:
            return None  # Stack is empty
        popped_item = self.stack.pop()
        print(popped_item,"popped from Stack")
        self.total_cost += 1  # Increment total cost
        self.operations +=1 # Increment no of operations
        return popped_item

    def multipop(self, k):
        self.operations +=1 # Increment no of operations
        if k >= len(self.stack):
            popped_elements = self.stack[:]
            self.stack = []
            self.total_cost += len(popped_elements)  # Increment total cost
            return popped_elements
        else:
            popped_elements = self.stack[-k:]
            self.stack = self.stack[:-k]
            self.total_cost += k  # Increment total cost
            return popped_elements

    def amortized_cost(self):
        return self.total_cost / self.operations

# Example usage:
stack = MultiPopStack()
stack.push(1)
stack.push(2)
stack.pop()
stack.push(3)
stack.multipop(5)
stack.push(4)
stack.push(5)
stack.pop()
stack.push(6)
stack.push(7)
stack.push(8)
stack.pop()
stack.push(9)
stack.push(10)
stack.multipop(7)
stack.push(11)
stack.push(12)

print("Amortized cost:", stack.amortized_cost())
