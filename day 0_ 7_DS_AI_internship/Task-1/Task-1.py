# Task-1

#Goal: Understand the difference between w (write) and a (append).

#Take the input frm the user
contents=input("Please enter the user name and  dialy goal:")
# Using a for appending
with open("journal.txt",'a') as file:
    file.write(contents)
with open("journal.txt",'a') as file:
    file.write(contents)
with open("journal.txt",'a') as file:
    file.write(contents)

# Using r for reading
with open("journal.txt", "r") as file:
    contents = file.read()
    print(contents)

#Before applying this code please clear the remaining content 
# Using w instead of a (clear your file )


#use input fuction here

#w is for writing

with open("journal.txt",'w') as file:
    file.write(contents)
with open("journal.txt",'w') as file:
    file.write(contents)
with open("journal.txt",'w') as file:
    file.write(contents)
    


# Using r for reading
with open("journal.txt", "r") as file:
    contents = file.read()
    print(contents)

