import random

# Number of trials
trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Total Trials:", trials)
print("Times Sum Was 7:", count_sum_7)
print("Experimental Probability:", experimental_probability)

# Theoretical probability
print("Theoretical Probability:", 1/6)
