#1. Create a list of 5 student names and print all names.


student_names=["raj","aryan","mangal","mintu","kallu"]
for name in student_names:
    print(name)




#2. Add one new student name to the list.
student_names=["raj","aryan"]
student_names.append("mangal")
print(student_names)




#3. Create a tuple of 5 city names and print the second city.
city_names=("Delhi","Mumbai","Kolkata","Chennai","Lucknow")
print(city_names[1])




#4. Create a set of 5 course names and add one new course.

course_names={"Python","C","C++","Java","SQL"}
course_names.add("Data Science")
print(course_names)




#5. Create a dictionary for one student with name, branch, batch, and marks.

students={"Name":"Raj",
          "Branch":"AIML",
          "Batch":"2024-2028",
          "Marks":"1249"
          }

print(students)


#6. Print the student dictionary in a readable format.

dict_students={"Name":"Raj",
          "Branch":"AIML",
          "Batch":"2024-2028",
          "Marks":"1249"
          }

print("Student Details")

for key,value in dict_students.items():
    print(f"{key}:{value}")
