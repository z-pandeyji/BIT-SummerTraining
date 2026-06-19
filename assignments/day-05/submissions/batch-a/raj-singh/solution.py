### Question 1: Create and Write a File
import collections
data=open("student.txt","w")
data.write("Name: Rahul\n")
data.write("Age: 20\n")
data.write("College: BIT\n")
data.close()
print("File created successfully")
print("_"*45)

### Question 2: Read a File
data=open("student.txt","r")
print(data.read())
data.close()
print("_"*45)

### Question 3: Append to a File
with open("student.txt","a") as data: #open with with auto close the file
    data.write("Course: Python Data AI\n")
    data.write("City: Gorakhpur\n")
with open("student.txt","r") as data:
    print(data.read())
print("_"*45)


### Question 4: Count Lines in a File
with open("student.txt","r") as data:
    line=data.readlines()
    print("total lines:-",len(line))
print("_"*45)




### Question 5: Write Multiple Students
with open("student.txt","w") as data:
    data.write("Aman\n")
    data.write("priya\n")
    data.write("shalu")
    data.write("raj\n")
    data.write("ansh")
with open("student.txt","r") as data:
    print(data.read())
print("_"*45)

### Question 6: Search a Name in File
search_name=input("enter name to search")
#try is use for unexpected error
try:
    with open("student.txt","r") as data:
        for line in data.read():    
            if search_name in line:
                print("found")
            else:
                print("not found")
except:
        print("file not found")
print("_"*45)


### Question 7: Copy File Content
try:
    with open("students.txt","r") as data:
        content=data.read()
        if len(data.readlines())>=0:   #checking if the file is not empty
            with open("student_backup.txt","w") as backup:
                backup.write(content)               #writing content to backup file
            print("Backup created successfully")
        else:
            print("no data found in source file")
except:
    print("file not found")
print("_"*45)

### Question 8: Marks File Summary

with open("marks.txt","w") as marks:
    marks.write(85)
    marks.write(90)
    marks.write(78)
    marks.write(92)
    marks.write(88)  #writing marks using loop
with open("marks.txt","r") as marks:
    print(marks.read())