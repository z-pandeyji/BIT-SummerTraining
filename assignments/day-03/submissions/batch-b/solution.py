
# 1 -> this program checks whether a number is positive, negative, or zero 
number=int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:   
    print("The number is zero.")

# 2 -> this program checks whether a number is even or odd  
number=int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")   
else:
    print("The number is odd.")

# 3 -> this program creates a list of 10 numbers and prints each number using a loop.
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)


# 4 -> this program defines a function named `calculate_average` that takes 3 marks and returns the average.
def average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average
mark1=int(input("Enter mark 1: "))
mark2=int(input("Enter mark 2: ")) 
mark3=int(input("Enter mark 3: "))
average_marks = average(mark1, mark2, mark3)
print(f"The average of the marks is: {average_marks}")

# 5 -> this program defines a function named `grade_student` that prints a grade based on marks.
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
marks=int(input("Enter marks: "))
student_grade = grade(marks)
print(f"The student's grade is: {student_grade}")
