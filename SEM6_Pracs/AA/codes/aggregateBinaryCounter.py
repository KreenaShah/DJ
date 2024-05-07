class BinaryCounter:
    def __init__(self):
        self.counter = [0] * 4  # Initialize the counter with four zeros
        self.total_cost = 0
        self.noOfIncrements = 0
        self.bits_flipped = 0

    def increment(self):
        self.bits_flipped = 0
        i = 0
        while i < len(self.counter) and self.counter[i] == 1:
            self.counter[i] = 0
            self.bits_flipped += 1
            i += 1
        if i < len(self.counter):
            self.counter[i] = 1
            self.bits_flipped += 1
        self.noOfIncrements += 1
        self.total_cost += self.bits_flipped

    def cost(self):
        return self.bits_flipped
    
    def amortized_cost(self):
        print(self.total_cost, self.noOfIncrements)
        return self.total_cost / self.noOfIncrements
    
    def get_counter(self):
        return self.counter[::-1]  # Reverse the counter before returning

counter = BinaryCounter()

counter.increment()
print("Counter after 1st increment:",  counter.get_counter(),", Cost Of this operation: ",counter.cost())
counter.increment()
print("Counter after 2nd increment:",  counter.get_counter(),", Cost Of this operation: ",counter.cost())
counter.increment()
print("Counter after 3rd increment:",  counter.get_counter(),", Cost Of this operation: ",counter.cost())
counter.increment()
print("Counter after 4th increment:",  counter.get_counter(),", Cost Of this operation: ",counter.cost())
counter.increment()
print("Counter after 5th increment:",  counter.get_counter(),", Cost Of this operation: ",counter.cost())
counter.increment()
print("Counter after 6th increment:",  counter.get_counter(),", Cost Of this operation: ",counter.cost())
counter.increment()
print("Counter after 7th increment:",  counter.get_counter(),", Cost Of this operation: ",counter.cost())
counter.increment()
print("Counter after 8th increment:",  counter.get_counter(),", Cost Of this operation: ",counter.cost())

print("Amortized cost", counter.amortized_cost())
