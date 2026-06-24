#day5 solution
#1:  Create and write data into student.txt
# Expected Output:File created successfully
file = open("student.txt", "w")
file.write("Name: Rahul\n")
file.write("Age: 20\n")
file.write("College: BIT")
file.close()
print("File created successfully")
print()


#2: Read a File
# Expected Output:
# Name: Rahul
# Age: 20
# College: BIT
with open("student.txt", "r") as file:
    print(file.read())
print()


#3: Append to a File
# Expected Output:
# Name: Rahul
# Age: 20
# College: BIT
# Course: Python Data AI
# City: Gorakhpur
with open("student.txt", "a") as file:
    file.write("\nCourse: Python Data AI")
    file.write("\nCity: Gorakhpur")
with open("student.txt", "r") as file:
    print(file.read())
print()


#4: Count Lines in a File
# Expected Output:Total lines: 5
with open("student.txt", "r") as file:
    lines = file.readlines()
print("Total lines:", len(lines))
print()


#5: Write Multiple Students
# Expected Output:
# Aman
# Priya
# Shalu
# Raj
# Ansh
students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
with open("students.txt", "w") as file:
    file.write("\n".join(students))
with open("students.txt", "r") as file:
    print(file.read())
print()


#6: Search a Name in File
# Example Input:Priya
# Expected Output:Found
name = input("Enter student name: ")
with open("students.txt", "r") as file:
    students = [line.strip() for line in file]
if name in students:
    print("Found")
else:
    print("Not Found")
print()


#7: Copy File Content
# Expected Output:Backup created successfully
source = open("students.txt", "r")
backup = open("students_backup.txt", "w")
backup.write(source.read())
source.close()
backup.close()
print("Backup created successfully")
print()


#8: Marks File Summary
# Expected Output:
# Total marks: 433
# Average marks: 86.6
# Create marks.txt
file = open("marks.txt", "w")
file.write("85\n90\n78\n92\n88")
file.close()
file = open("marks.txt", "r")
marks = [int(line.strip()) for line in file]
file.close()
total = sum(marks)
average = total / len(marks)
print("Total marks:", total)
print("Average marks:", average)