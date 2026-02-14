# Task-1

#Goal: Analyze relationships between two numerical variables.

#Scenario: You want to see if there is a relationship between hours spent studying 
#and exam scores for a group of students.



import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

plt.xlabel("Study Hours") # lable of x axis 
plt.ylabel("Exam Scores") # lable of y axis 
plt.title("Study Hours vs Exam Scores") # title of graph

plt.scatter(study_hours,scores)
plt.show()