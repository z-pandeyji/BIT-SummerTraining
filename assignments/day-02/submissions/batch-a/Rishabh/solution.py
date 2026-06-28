# Question 1: Check whether a number is positive, negative, or zero

number = 10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Question 2: Check whether a number is even or odd

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Question 3: Create a list of 10 numbers and print each number using a loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nNumbers in the list:")
for num in numbers:
    print(num)


# Question 4: Function to calculate average of 3 marks

def calculate_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3


average = calculate_average(80, 90, 85)
print("\nAverage Marks:", average)


# Question 5: Function to print grade based on marks

def grade_student(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    else:
        print("Grade D")


grade_student(average)