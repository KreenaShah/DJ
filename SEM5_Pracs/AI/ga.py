from random import randint
 
def selection(li):
  dec = list(map(lambda x : int(x, 2), li))
  fit = list(map(lambda x : x*x, dec))
  s = sum(fit)
  avg = s/n
  exe = list(map(lambda x : round(x/avg, 3), fit))
  ac = list(map(lambda x : round(x), exe))
  return dec, fit, exe, ac
 
def crossing(li):
    import random
    crossed = []
    random.shuffle(li) 
    for i in range(0, len(li), 2):
        temp1 = li[i]
        if i + 1 < len(li): 
            temp2 = li[i + 1]
            crosspoint = random.randint(1, len(temp1) - 1)  
            print("The crossover point for pair " + str(i) + " is " + str(crosspoint))
            temp3 = temp1[crosspoint:]
            temp4 = temp2[crosspoint:]
            temp1 = temp1[0:crosspoint] + temp4
            temp2 = temp2[0:crosspoint] + temp3
            crossed.append(temp1)
            crossed.append(temp2)
    return crossed
 
n = int(input("Enter number of samples: "))
sam = []
for i in range(n):
  sam.append(input("Enter gene: "))
 
m = int(input("Enter number of generations to be computed: "))
crossed = sam.copy()
for i in range(m):
  dec, fit, exe, ac = selection(crossed)
  s = sum(ac)
  if s < n:
    maxi = max(ac)
    k = ac.index(maxi - 1)
    ac[k] += 1
  if s > n:
    maxi = max(ac)
    k = ac.index(maxi)
    ac[k] -= 1
  print("\n----------------------------------------------- GENERATION ", i, "-----------------------------------------------")
  print("Initial Population\tX Value\t\tFitness Value\t\tExpected Count\t\tActual Count")
  for j in range(n):
    print(crossed[j], "\t\t", dec[j], "\t\t", fit[j],  "\t\t", exe[j], "\t\t\t", ac[j])
  crossed = crossing(crossed)
  print("\nCrossover - \n", crossed)
print("\nGENERATION ", (m + 1), " - ", crossed)