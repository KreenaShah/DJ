import random

candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
interview_cost = 0
hiring_cost = 0
interviewed_candidates = []
hired_candidates = []
max=-1

while candidates:
    selected_candidate = random.choice(candidates)
    interviewed_candidates.append(selected_candidate)
    interview_cost += 1
    if(selected_candidate > max):
        hired_candidates.append(selected_candidate)
        hiring_cost += 5
        max = selected_candidate
    candidates.remove(selected_candidate)

print("Total Cost : ", interview_cost + hiring_cost)