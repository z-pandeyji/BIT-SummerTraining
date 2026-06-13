# 5. Write a function named `grade_student` that prints a grade based on marks.

def grade_student(maths,physics,chemistry,english,hindi):
    avg=(maths+physics+chemistry+english+hindi)/5
    
    if avg>=90:
        print("Grade A")
    elif avg>=80:
        print("Grade B")
    elif avg>=70:
        print("Grade C")        
    elif avg>=60:
        print("Grade D")
    else: 
        print("fail")   

grade_student(80,85,90,70,95)        