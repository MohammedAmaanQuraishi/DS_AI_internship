# Task-2

# Independent Events
# Flip a coin (Heads) AND roll a 6

# Probability of Heads
P_heads = 1/2

# Probability of rolling a 6
P_six = 1/6

# Independent formula
P_independent = P_heads * P_six

print("Independent Event Probability (Heads AND 6):")
print("Fraction:", P_independent)
print("Percentage:", P_independent * 100, "%")


print("\n" + "-"*50 + "\n")

# Dependent Events
# 5 Red and 5 Blue marbles, pick 2 without replacement

red = 5
blue = 5
total = red + blue

# First red
P_first_red = red / total

# After removing one red
red_after = red - 1
total_after = total - 1

# Second red
P_second_red = red_after / total_after

# Dependent formula
P_dependent = P_first_red * P_second_red

print("Dependent Event Probability (Both Red):")
print("Fraction:", P_dependent)
print("Percentage:", P_dependent * 100, "%")

