# Task-2
# Goal: Practice structured data storage.

# usng a for appending the information
with open("students.csv",'w') as file:
    file.write("Name,Grade,Status\n")
    file.write("Alice,A,Pass\n")
    file.write("Bob,B,Pass\n")
    file.write("Charlie,F,Fail\n")
    
# usng r for reading the information
with open("students.csv", "r") as file:
    contents = file.read()
    print(contents)
    

import csv

with open("students.csv","r") as file:
    reader = csv.DictReader(file)
    print("The student who have passed:")
    for row in reader:
        if row["Status"] == "Pass":
            
            print(row["Name"])

