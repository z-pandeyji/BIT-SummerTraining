#1. Create a list of 5 student names and print all names.

student_names=["raj","rohit","nancy","deepika","priya"]
for name in student_names:
    print(name)

#2. Add one new student name to the list.

student_name=["raj","nisha"]
student_name.append("pushpa")
print(student_name)



#3. Create a tuple of 5 city names and print the second city.

cities=("Lucknow","Delhi","Mumbai","Kolkata","Chennai")
print(cities[1])


#4. Create a set of 5 course names and add one new course.



courses={"Python","Java","C++","Javascript","SQL"}
courses.add("data science")
print(courses)



#5. Create a dictionary for one student with name, branch, batch, and marks.

student={"name":"Raj",
         "branch":"Computer Science",
         "batch":"2024-2028",
         "marks":"1249"
         }
print(student)


#6. Print the student dictionary in a readable format.
student={"name":"Raj",
         "branch":"Computer Science",
         "batch":"2024-2028",
         "marks":"1249"
         }
print("Student Details")
print("Name:",student["name"])
print("Branch:",student["branch"])
print("Batch:",student["batch"])
print("Marks:",student["marks"])














    
