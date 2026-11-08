import numpy as np


# Question 1: Create a NumPy Array
marks = np.array([85, 90, 78, 92, 88])
print("Marks:", marks)


# Question 2: Array Shape and Size
print("Shape:", marks.shape)
print("Size:", marks.size)


# Question 3: Basic Calculations
print("Total:", marks.sum())
print("Average:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())


# Question 4: Create a 2D Array
array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("2D Array:")
print(array_2d)


# Question 5: Indexing and Slicing
print(array_2d[1, 1])   # 50
print(array_2d[0])      # First row


# Question 6: Element-Wise Operations
numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 10)


# Question 7: Filter Values
filtered_marks = marks[marks >= 90]
print(filtered_marks)


# Question 8: Student Marks Matrix
student_marks = np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]
])

student_averages = student_marks.mean(axis=1)
print(np.round(student_averages, 2))



