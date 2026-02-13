#Class task 1

#Reading the file
file=open("amaan.txt",'r')
contents=file.read()
print(contents)
file.close()

#Appending the file
file=open("amaan.txt",'a')
file.write("Crypotogrpahy and network security is my favouite subject")
file.close()



#Writing the file
file=open("amaan.txt",'w')
file.write("Crypotogrpahy and network security is my favouite subject")
file.close()

#Class task 2

with open("amaan.txt",'r') as file:
    contents=file.read()
    print(contents)

#Class task 3

import csv

with open("a.csv.csv") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        
#Class task 4
try:
    with open("amaa.txt",'r') as file:
        contents=file.read()
        print(contents)
except FileNotFoundError:
    print("Such file not exists")
