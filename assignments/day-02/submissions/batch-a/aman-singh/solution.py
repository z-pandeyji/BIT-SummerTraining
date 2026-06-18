# Question 1: Positive, Negative, or Zero
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# Question 2: Even or Odd
num2 = int(input("Enter another number: "))

if num2 % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Question 3: List of 10 numbers and print using loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Printing list elements:")
for n in numbers:
    print(n)


# Question 4: Function to calculate average
def calculate_average(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    return avg

# Calling function
average = calculate_average(80, 90, 85)
print("Average marks:", average)


# Question 5: Function to grade student
def grade_student(marks):
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")

# Calling function
grade_student(average)
