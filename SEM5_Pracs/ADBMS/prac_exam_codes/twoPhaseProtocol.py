class Coordinator:
    def __init__(self):
        self.participants = []
        self.votes = []

    def register_participant(self, participant):
        self.participants.append(participant)

    def send_prepare(self):
        # Phase 1: Prepare
        for participant in self.participants:
            participant.receive_prepare()

    def start_voting(self):
        print("---------VOTING PHASE-----------------")
        for participant in self.participants:
            self.votes.append(participant.send_vote())

    def send_commit(self):
        print("---------INDIVIDUAL LOGS-----------------")
        # Phase 2: Commit
        for participant in self.participants:
            # print(participant)
            participant.receive_commit()
    
    def make_decision(self):
        print("---------DECISION PHASE-----------------")
        if 0 in self.votes:
            print("Transaction aborted as all participating sites not ready!")
        else:
            print("Transaction committed!")

class Participant:
    def __init__(self, name):
        # print(name)
        self.name = name
        self.prepared = False

    def receive_prepare(self):
        # Phase 1: Prepare
        # Perform any necessary checks or actions
        print(f"{self.name} is in Prepare Phase")

    def send_vote(self):
        vote  = int(input(f"Enter 1 if {self.name} is ready to commit \nEnter 0 if {self.name} is not ready to commit:\n"))
        if vote:
            self.prepared = True
        return vote

    def receive_commit(self):
        # Phase 2: Commit
        if self.prepared:
            print(f"{self.name} committed the transaction.")
        else:
            print(f"{self.name} cannot commit. Not prepared.")

num_participants = int(input("Enter the number of participants: "))
coordinator = Coordinator()

for i in range(num_participants):
    participant = Participant(f"Participant {i+1}")
    coordinator.register_participant(participant)

coordinator.send_prepare()
coordinator.start_voting() # phase 1
coordinator.send_commit()
coordinator.make_decision() #phase 2

print("Transaction Completed!")