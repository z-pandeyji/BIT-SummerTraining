#Question 1

a = int(input("Enter the number: "))
if a>0:
    print("The number is positive.")
elif a<0:
    print("The number is negative.")
else:    
    print("The number is zero.")

#Question 2
a = int(input("Enter the number: "))
if a%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

#Question 3
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    print(num)

#Question 4

def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average
print(calculate_average(10, 20, 30))

#Question 5

def grade_student(marks):
    if marks >= 90:
        print("A")
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    elif marks >= 60:
        print("D")  
    else:
        print("F")
grade_student(85)
