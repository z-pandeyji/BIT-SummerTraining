# 1. Write a program to check whether a number is positive, negative, or zero.

number=int(input("Enter the number:"))

if number>0:
    print(f"{number} is positive")
elif number<0:
    print (f"{number} is negative")
else:
    print("number is zero")       