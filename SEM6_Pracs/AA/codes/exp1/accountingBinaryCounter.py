class BinaryCounter:
    def __init__(self):
        self.counter = [0]*4
        self.counterVal = 0
        self.actCost = 0 # no. of bits flipped
        self.amortCost = 0 # 2 for setting bit 1, 0 for setting bit 0
        self.cred = 0
    
    def increment(self):
        self.actCost = 0
        self.amortCost = 0
        i = 0
        while(i<len(self.counter) and self.counter[i]==1):
            self.counter[i] = 0
            self.actCost += 1
            self.amortCost += 0
            i+=1
        if(i<len(self.counter)):
            self.counter[i] = 1
            self.actCost += 1
            self.amortCost += 2
        self.cred += self.amortCost - self.actCost
    
    def get_counter(self):
        return self.counter[::-1]
    
    def amortizedCost(self):
        return self.amortCost

    def actualCost(self):
        return self.actCost
    
    def credit(self):
        return self.cred

counter = BinaryCounter()
print("CounterValue  binaryNumber    AmortizedCost    ActualCost      Credit")
for i in range(1,9):
    counter.increment()
    print(f"{i}             {counter.get_counter()}         {counter.amortizedCost()}           {counter.actualCost()}              {counter.credit()}")