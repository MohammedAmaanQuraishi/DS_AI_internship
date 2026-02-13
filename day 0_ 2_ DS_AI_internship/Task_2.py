# Ask the total bill amount
Total_Bill_Amount=float(input("Enter the total amount"))

# Ask the no of friends
No_of_friends=int(input("Enter the no of friends"))

# Calculate the Share per Person (Bill / People)
Share_per_Person=(Total_Bill_Amount/No_of_friends)

#Displaing the amount
print(f"Total Bill: {Total_Bill_Amount}. Each person pays: {Share_per_Person}")