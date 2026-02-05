# Task -2

# Goal: Understand how sets handle uniqueness and perform membership testing.

# Scenario: You have a raw list of User IDs collected from a website login page. Many users logged in multiple times, and you need a list of unique visitors.

# Creating a list named raw_logs containing several duplicate IDs

raw_logs= ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# Creating a set named unique_users by passing the raw_logs list into the set() function.

unique_users=set(raw_logs)
# displaying id
print("The unique set of IDs",unique_users)

# Membership Test

print("Is ID05 present?","ID05" in raw_logs)

#The original list versus the length of the set
print("The length of list is",len(raw_logs))
print("The length of set is",len(unique_users))

# duplicats present
duplicates = len(raw_logs) - len(unique_users)

# displaying 
print(f"{duplicates} Duplicates are removed")
