# Task -1

# Goal: Practice dictionary creation, updating, and safe data retrieval using .get().
# Scenario: You are building a simple digital rolodex to store contact information.

# creating a dictionary named contacts with at least three people.
contacts={"Amaan":"8317323013",
          "Asif":"8888888888",
          "Saqeeb":"9876543210"}

# Adding a new contact to the dictionary and  update the phone number of an existing contact.

# Adding
contacts["Ali"] = "1243567311"

# updating
contacts["Asif"] = "153666511"

# Safe Access
print(contacts.get("momin","Contact not found"))

# Iterating the value and printing them
for a, b in contacts.items():
    print(f" Contact: {a} | Phone: {b}")




