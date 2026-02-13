# Class Task -1
# define student fuction
def student():
    print("Hello students") 
# calling student fuction
student()
# define teachers fuction
def teachers():
    print("Hello teachers")
# calling student fuction
teachers()

#Class Task -2

# writing the fuction

def remainder(a,b): 
    return a%b   # returning the value

#storing in variable
answer=remainder(5,3)

#resusing the variable
answer=answer+1

# displaying the value
print(answer)

#while using the fuction without the result
def remainder(a,b): 
    print(a%b)   # returning the value

#storing in variable
answer=remainder(5,3)

# displaying the value
print(answer)


# Class Task -3

# define variable
num=0
#define function
def student():
    num=1
    return num
student() 
print(num)

# define variable
num=0
#define function
def student():
    global num #using the global keyword for using it for global
    num=+1
    return num
student() 
print(num)


# Class Task -4

# importing math
import math
# importing sqrt from math
print(math.sqrt(9))


# importing randint from random
from random import randint
print(randint(1,100))



# Class Task -5
import utility

print("Addition:", utility.add(3, 2))
print("Multiplication:", utility.mul(3, 2))
print("Subtraction:", utility.sub(3, 2))
print("Division:", utility.div(3, 2))
print("Remainder:", utility.remainder(3, 2))
print("Square Root:", utility.square_root(9))












    
    