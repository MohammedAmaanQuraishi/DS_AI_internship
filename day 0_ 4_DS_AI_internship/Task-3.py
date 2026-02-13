# Task-3
# Goal: Use mathematical set operations (Intersection and Union) to find commonalities.
# Scenario: You are building a basic recommendation engine that compares the interests of two friends to find things they can do together.

# Creating two sets:

friend_a= {"Python", "Cooking", "Hiking", "Movies"}
friend_b= {"Hiking", "Gaming", "Photography", "Python"}

shared_interests =friend_a & friend_b #intersection
all_interests =friend_a| friend_b    #union
unique_to_a =friend_a - friend_b      #Difference

# Displaying Intersection
print("Intersection of friend a and friend b are ",shared_interests)

#  Displaying Union:
print("Union of friend a and friend b are ", all_interests)

# Displaying Difference
print("Union of friend a and friend b are ", unique_to_a )
 

