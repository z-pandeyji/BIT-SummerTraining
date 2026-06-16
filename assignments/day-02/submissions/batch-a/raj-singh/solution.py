# 1. Write a program to check whether a number is positive, negative, or zero.
number=float(input("enter a number:"))
if number>0:
    print("the no. is positive")
elif number<0:
    print("the no. is negative")
else:
    print("the no. is zero")




# 2. Write a program to check whether a number is even or odd.
number=int(input("enter a number:"))
if number%2==0:
    print("the no. is even ")
else:
    print("the no. is odd ")



#3. Create a list of 10 numbers and print each number using a loop.
    num=[1,2,3,4,5,6,7,8,9,10]
    for i in num:
        print(i)



    #4. Write a function named `calculate_average` that takes 3 marks and returns the average.
    def calculate_average(mark1,mark2,mark3):
        average=(mark1 +mark2 +mark3)/3
        




# 5. Write a function named `grade_student` that prints a grade based on marks.
def grade_student(marks):
    if marks>=90:
        print("grade A")
    elif marks>=80:
        print("grade B")
    elif marks>=70:
        print("grade C")
    elif marks>=60:
        print("grade D")
    else:
        print("grade F")


        
    









