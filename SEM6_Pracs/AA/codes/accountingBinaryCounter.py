class BinaryCounter:
    def __init__(self):
        self.counter = [0] * 4  # Initialize the counter with four zeros
        self.total_cost = 0
        self.act_cost = 0
        self.amor_cost = 0
        self.cred = 0

    def increment(self):
        self.act_cost = 0
        self.amor_cost = 0
        i = 0
        while i < len(self.counter) and self.counter[i] == 1:
            self.counter[i] = 0
            self.act_cost += 1
            self.amor_cost += 0
            i += 1
        if i < len(self.counter):
            self.counter[i] = 1
            self.amor_cost += 2
            self.act_cost += 1
        self.cred += self.amor_cost - self.act_cost

    def actual_cost(self):
        return self.act_cost
    
    def amortized_cost(self):
        return self.amor_cost
    
    def credit(self):
        return self.cred
    
    def get_counter(self):
        return self.counter[::-1]  # Reverse the counter before returning

counter = BinaryCounter()
print("CounterValue  binaryNumber    AmortizedCost      ActualCost      Credit")
for i in range(1,9):
    counter.increment()
    print(f"{i}             {counter.get_counter()}     {counter.amortized_cost()}                  {counter.actual_cost()}                  {counter.credit()}")