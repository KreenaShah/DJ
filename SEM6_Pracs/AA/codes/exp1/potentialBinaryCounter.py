class BinaryCounter:
    def __init__(self):
        self.counter = [0]*4
        self.counterVal = 0
        self.actCost = 0 # no. of bits flipped
        self.prevP = 0 
        self.currP = 0 # no. of 1's in the current binary number
        self.potentialDiff = 0 
        self.amortCost = 0
    
    def increment(self):
        self.actCost = 0
        self.currP = 0
        i = 0
        while(i<len(self.counter) and self.counter[i]==1):
            self.counter[i] = 0
            self.actCost += 1
            i+=1
        if(i<len(self.counter)):
            self.counter[i] = 1
            self.actCost += 1
        for i in range(len(self.counter)):
            if(self.counter[i]==1):
                self.currP += 1
        self.potentialDiff = self.currP - self.prevP
        self.prevP = self.currP
    
    def get_counter(self):
        return self.counter[::-1]

    def actualCost(self):
        return self.actCost
    
    def potentailDifference(self):
        return self.potentialDiff
    
    def amortizedCost(self):
        return self.actCost + self.potentialDiff

counter = BinaryCounter()
print("CounterValue  binaryNumber    ActualCost    PotentialDiff    AmortizedCost")
for i in range(1,9):
    counter.increment()
    print(f"{i}             {counter.get_counter()}         {counter.actualCost()}         {counter.potentailDifference()}                 {counter.amortizedCost()}")