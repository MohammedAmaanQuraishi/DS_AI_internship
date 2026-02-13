#Task 3
#Take the input frm the user
contents=input("Please enter the name of file with extension: ")

#using try keywords
try:
    with open(contents,'r') as file:
        contents=file.read()
        print(contents)
#using except keywords
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")
