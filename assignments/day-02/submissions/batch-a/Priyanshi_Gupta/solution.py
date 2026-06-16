#1
from numpy import average


num =int(input("Enter the number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



#2
num= int(input("Enter the first number: "))
if num%2 == 0:
    print("The number is even.")        
else:
    print("The number is odd.")


#3
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list:
    print(num)




#4
def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average
avg = calculate_average(70, 80, 90)
print("average=", avg)



#5
def grade_student(marks):
    if marks >= 90:
        print("grade A")
    elif marks >= 80:
        print("grade B")
    elif marks >= 70:
        print("grade C")
    elif marks >= 60:
        print("grade D")
    else:
        print("grade F")
 

    