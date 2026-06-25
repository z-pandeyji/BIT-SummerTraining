#1 
file = open ("student.txt","w")
file.write("Name: Priyanshi Gupta\n")
file.write("Age: 19\n")
file.write("College: BIT")
file.close()
print("File create successfully")

#2
file = open("student.txt", "r")
content = file.read()
print(content)
file.close

#3
file = open("student.txt", "a")
file.write("\nCourse: Python Data AI")
file.write("\nCity: Gorkhpur")
file.close
file = open("student.txt", "r")
print(file.read())
file.close()


#4
file = open("student.txt", "r")
lines = file.readlines()
print("Total lines:", len(lines))
file.close()

#5
# Write 5 student names in students.txt

with open("students.txt", "w") as file:
    file.write("Aman\n")
    file.write("Priya\n")
    file.write("Shalu\n")
    file.write("Raj\n")
    file.write("Ansh\n")
with open("students.txt", "r") as file:
    for name in file:
        print(name.strip())

#6
name = input("Enter student name: ")

with open("students.txt", "r") as file:
    students = [line.strip() for line in file]

if name in students:
    print("Found")
else:
    print("Not Found")


#7
with open("students.txt", "r") as file:
    data = file.read()

# Write data to students_backup.txt

with open("students_backup.txt", "w") as file:
    file.write(data)

print("Backup created successfully")

#8
# Create marks.txt

with open("marks.txt", "w") as file:
    file.write("85\n")
    file.write("90\n")
    file.write("78\n")
    file.write("92\n")
    file.write("88\n")
with open("marks.txt", "r") as file:
    marks = [int(line.strip()) for line in file]

total = sum(marks)
average = total / len(marks)

print("Total marks:", total)
print("Average marks:", average)