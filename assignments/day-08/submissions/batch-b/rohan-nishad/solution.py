import numpy as np

marks = np.array([85, 90, 78, 92, 88])
print(marks)
print(f"Shape: {marks.shape}")
print(f"Size: {marks.size}")
print(f"Total: {marks.sum()}")
print(f"Average: {marks.mean()}")
print(f"Maximum: {marks.max()}")
print(f"Minimum: {marks.min()}")

array_2d = np.array([[10, 20, 30], [40, 50, 60]])
print(array_2d)
print(array_2d[1, 1])
print(array_2d[0])

numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 10)

high_marks = marks[marks >= 90]
print(high_marks)

student_marks = np.array([[85, 78, 90], [92, 88, 95], [76, 82, 80]])
print(student_marks.mean(axis=1))
