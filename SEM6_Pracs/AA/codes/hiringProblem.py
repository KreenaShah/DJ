import random

candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
interviewed_candidates = []
hired_candidates = []

# Randomly select and interview candidates
for i in range(len(candidates)):
    selected_candidate = random.choice(candidates)
    interviewed_candidates.append(selected_candidate)
    candidates.remove(selected_candidate)

# Hire the best candidate so far
max=-1
for i in range(len(interviewed_candidates)):
    if interviewed_candidates[i] > max:
        max=interviewed_candidates[i]
        hired_candidates.append(interviewed_candidates[i])

# Calculate firing cost
firing_cost = len(hired_candidates) - 1

print("Interviewed candidates:", interviewed_candidates)
print("Hired candidates:", hired_candidates)
print("Number of candidates hired:", len(hired_candidates))
print("Firing cost:", firing_cost)