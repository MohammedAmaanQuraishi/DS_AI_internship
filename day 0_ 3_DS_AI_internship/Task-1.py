# Goal: Practice creating lists and using append(), remove(), and sort().
# Scenario: You are managing a small inventory system for a grocery store

# Practice creating lists and using append(), remove(), and sort().

# Creating a list named inventory containing: "Apples", "Bananas", "Carrots", "Dates"
Inventory=["Apples", "Bananas", "Carrots", "Dates"] 

# Print the current inventory.
print(Inventory)

# A shipment of "Eggs" has arrived
Inventory.append("Eggs")

# "Bananas" have been sold out
Inventory.pop(2)

# Organize the inventory alphabetically using
Inventory.sort()

# Print the final updated inventory.
print(Inventory)