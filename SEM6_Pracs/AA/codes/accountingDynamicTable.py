class DynamicTable:
    def __init__(self):
        self.table = [] # list that stores the elements
        self.capacity = 0 # capacity of table
        self.size = 0 # current number of elements in the dynamic table
        self.insertion_cost = 0
        self.copying_cost = 0
        self.actual_cost = 0
        self.amortizedCost = 3
        self.credit = 0

    def resize(self, new_capacity):
        new_table = [None] * new_capacity
        for i in range(self.size):
            new_table[i] = self.table[i]
        self.table = new_table
        if self.capacity == 0:
            self.copying_cost = 0
        else:
            self.copying_cost += new_capacity - self.capacity
        self.capacity = new_capacity

    def insert(self, value):
        self.copying_cost = 0
        if self.size == self.capacity:
            self.resize(max(1, 2 * self.capacity))

        self.table[self.size] = value
        self.size += 1
        self.insertion_cost = 1
        self.actual_cost = self.insertion_cost + self.copying_cost
        self.credit += self.amortizedCost - self.actual_cost
        print(f"{value}         {self.capacity}         {self.insertion_cost}             {self.copying_cost}          {self.actual_cost}                   {self.amortizedCost}                  {self.credit}")

if __name__ == "__main__":
    table = DynamicTable()
    print(f"Value  Capacity  InsertionCost  CopyingCost  ActualCost      AmortizedCost      Credit")
    for i in range(1,11):
        table.insert(i)