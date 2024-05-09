class BinaryCounter:
    def __init__(self):
        self.counter = [0]*4
        self.counterVal = 0
        self.actCost = 0 # no. of bits flipped
        self.totCost = 0 
        self.noOfIncrements = 0 # no. of bits flipped
    
    def increment(self):
        self.actCost = 0
        i = 0
        while(i<len(self.counter) and self.counter[i]==1):
            self.counter[i] = 0
            self.actCost += 1
            i+=1
        if(i<len(self.counter)):
            self.counter[i] = 1
            self.actCost += 1
        self.noOfIncrements += 1
        self.totCost += self.actCost
    
    def get_counter(self):
        return self.counter[::-1]

    def actualCost(self):
        return self.actCost
    
    def amortizedCost(self):
        return self.totCost/self.noOfIncrements

counter = BinaryCounter()
print("CounterValue  binaryNumber    Cost")
for i in range(1,9):
    counter.increment()
    print(f"{i}             {counter.get_counter()}     {counter.actualCost()}")
print("Amortized Cost : ",counter.amortizedCost())