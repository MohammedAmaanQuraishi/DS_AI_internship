#classs task 1
#creating dictionary
dictionary={"hello":"world","age":2,"date":"2feb"}

#access the value
print(dictionary["hello"]) 

#upadate
dictionary["hello"]="hi"
print(dictionary)

#classs task 2
# using get
print(dictionary.get("i","hello"))

#Iteration using item
for key, value in dictionary.items():
    print(key,value)
    
for key in dictionary:
    print(key,dictionary[key])
    




