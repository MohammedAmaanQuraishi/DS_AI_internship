import matplotlib.pyplot as plt

# Using the plot function 
a=[1,2,3,4]
b=[1,2,3,4]
plt.plot(a,b)
plt.show() #For output

# Using the scatter function 
a=[1,2,3,4]
b=[1,2,3,-4]
plt.scatter(a,b)
plt.show() #For output


# Using the barfunction 
names=["Amaan","sohail","asif"]
marks=[14,50,35]
plt.bar(names,marks)
plt.show()

# Sub ploting function

plt.subplot(1,3,1)
plt.plot([1,2,3],[1,2,3])
plt.title("line plot") 

plt.subplot(1,3,2)
plt.bar(["Amaan","sohail","asif"],[1,2,3])
plt.title("bar plot")

plt.subplot(1,3,3)
a=[1,2,3,4]
b=[1,2,3,-4]
plt.scatter(a,b)
plt.title("scatter plot")

plt.show()