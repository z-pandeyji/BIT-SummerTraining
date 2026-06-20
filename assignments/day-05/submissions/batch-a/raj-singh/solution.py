data = open("student.txt", "w")
data.write("Name: Rahul\n")
data.write("Age: 20\n")
data.write("College: BIT\n")
data.close()
print("File created successfully")
print("_" * 45)

### Question 2: Read a File
data = open("student.txt", "r")
print(data.read())
data.close()
print("_" * 45)

### Question 3: Append to a File
with open("student.txt", "a") as data:  # open with with auto close the file
    data.write("Course: Python Data AI\n")
    data.write("City: Gorakhpur\n")
with open("student.txt", "r") as data:
    print(data.read())
print("_" * 45)

### Question 4: Count Lines in a File
with open("student.txt", "r") as data:
    line = data.readlines()
    print("total lines:-", len(line))
print("_" * 45)

### Question 5: Write Multiple Students
with open("students.txt", "w") as data:
    data.write("Aman\n")
    data.write("Priya\n")
    data.write("Shalu\n")
    data.write("Raj\n")
    data.write("Ansh\n")
with open("students.txt", "r") as data:
    print(data.read())
print("_" * 45)

### Question 6: Search a Name in File
search_name = input("enter name to search")
# try is use for unexpected error
try:
    with open("student.txt", "r") as data:
        for line in data.read():
            if line.strip() == search_name:
                print("found")
                break
            else:
                print("not found")
                break
except:
    print("file not found")
print("_" * 45)

### Question 7: Copy File Content
try:
    with open("students.txt", "r") as data:
        if len(data.readlines()) >= 0:  # checking if the file is not empty
            with open("students_backup.txt", "w") as student_backup_data:
                student_backup_data.write(data.read())  # writing content to backup file
            print("Backup created successfully")
        else:
            print("no data found in source file")
except:
    print("file not found")
print("_" * 45)

### Question 8: Marks File Summary

with open("marks.txt", "w") as marks:
    marks.write("85\n")
    marks.write("90\n")
    marks.write("78\n")
    marks.write("92\n")
    marks.write("88\n")
total_marks = 0
c = 0
for line in open("marks.txt"):
    c = c + 1
    total_marks += int(line)
print("Total marks:", total_marks)
print("Average marks:", total_marks / c)