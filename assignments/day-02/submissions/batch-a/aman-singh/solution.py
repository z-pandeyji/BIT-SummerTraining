# 1. Write a program to check whether a number is positive, negative, or zero.

num = int(input("enter a number"))
if num > 0:
    print("number is positive")
elif num < 0:

    print("number is negative")
else:
    print("Zero")

# 2. Write a program to check whether a number is even or odd.    

num = int(input("enter a number"))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# 3. Create a list of 10 numbers and print each number using a loop.

number = [1,4,6,8,9,3,5,9,6,1]
for num in number:
    print("num")


# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.
def calculate_average(m1,m2,m3):
    avg = (m1+m2+m3)/3
    return avg
print(calculate_average(12,50,60))


# 5. Write a function named `calculate_average` that takes 3 marks and returns the average.
def grade_student(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Fail")
    print (grade_student(82))                   
