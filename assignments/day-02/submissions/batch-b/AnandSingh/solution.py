# 1. check number is positive and negative or zero
nums=[12,34,56,-7,5,0,6,-4,-34]
print(nums)
for n in nums:
    if n>0:
        print("positive is:",n)
    elif n<0:
        print("negative is:",n)
    else:
        print("zero is:",n)
        
# 2. check number is even or odd
num=int(input("enter a number:"))
if num%2==0:
    print("even number:",num)
else:
    print("odd number:",num)

# 3. create a list of 10 numbers and print each number using loop
numbers=[1,2,3,4,5,6,7,8,9,10]
for n in numbers:
    print(n)
    
# 4. write a function name calculate_average 3 marks and return average
computer_marks=int(input("enter computer marks:"))
math_marks=int(input("enter math marks:"))
science_marks=int(input("enter science marks:"))

def calculate_average(computer_marks,math_marks,science_marks):
    average=(computer_marks+math_marks+science_marks)/3
    return average

avg=calculate_average(computer_marks,math_marks,science_marks)
print("average marks:",avg)

# 5. write a function name grade_student that print a grade based marks
marks=int(input("enter marks:"))
def grade_student(marks):
    if marks>=90:
        print("grade A")
    elif marks>=75:
        print("grade B")
    elif marks>=55:
        print("grade C")
    else:
        print("grade D")
grade_student(marks)

