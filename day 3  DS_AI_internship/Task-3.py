# Goal: Understand why Tuples cannot be changed (Immutability).

# Scenario: You are setting up the screen resolution for a game. This setting should not change during gameplay.

# Create a tuple named screen_res
screen_res=(1920, 1080)

# Printing Current Resolution
print("Current Resolution: 1920x1080")

# The Experiment: Try to change the width
# screen_res[0] = 1280 --->  We got error here

# printing the  final statement
print("Tuples cannot be modified!")

