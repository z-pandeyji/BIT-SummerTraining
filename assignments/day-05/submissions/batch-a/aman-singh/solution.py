### Question 1: Create and Write a File
with open("student . txt", "w") as f :
    f. write("Name: aman\n")
    f. write("Age: 20\n")
    f. write("College: Bit\n")
    print("File created successfully")


### Question 2: Read a File
print("\n Reading student.txt")
with open("student.txt", "r") as f:
    content = f . read()
    print(content)

### Question 3: Append to a File

with open("student.txt", "r") as f:
    f.write("coures:Python Data Ai\n")
    f.write("City:Gorakhpur\n")

print("upadated file content:")
with open("student.txt", "r") as f:
    lines =  f.readlines() 
    print("Total lines:", len(lines))



### Question 4: Count Lines in a File

with open("student.txt", "r") as f:
    lines = f.readlines()
    print("Total lines:",len(lines))


#Question 5: Write Multiple Students##
with open("student.txt", "r") as f:
    f.write("Aman\nPriya\nShalu\nRaj\nAnsh")
print("student list:")

with open("student.txt", "r") as f:
    print(f.read)

### Question 6: Search a Name in File

name =input("enter student name search:")
Found = False
with open("student.txt", "r") as f:
    for line in f:
        if line.strip().lower == name.lower():
            Found = True
            break
if Found:
    print("Found")
else:
    print("Not Found")

### Question 7: Copy File Content

with open("students.txt", "r") as f:
    data = f.read()

with open("students_backup.txt", "w") as f:
    f.write(data)

print("Backup created successfully")

### Question 8: Marks File Summary

with open("marks.txt", "w") as f:
    f.write("85\n90\n78\n92\n88\n")

total = 0
count = 0

with open("marks.txt", "r") as f:
    for line in f:
        mark = int(line.strip())
        total += mark
        count += 1

average = total / count

print("Total marks:", total)
print("Average marks:", average)


