# 1.create a list of 5 students name and print all name
students = ["anand", "rohit", "sachin", "vishal", "sandeep"]
for name in students:
    print(name)
    
# 2. add one new student name to list
students = ["anand", "rohit", "sachin", "vishal", "sandeep"]
print("before adding new student name:", students)
students.append("akash")
print("after adding new student name:", students)

# 3. create a tuple of 5 city names and print second city name
cities = ("delhi","mumbai","kolkata","gorakhpur","lucknow")
print("second city name is:", cities[1])

# 4. create a set of 5 courses names and add one new course
courses = {"python", "java", "c++", "javascript", "html"}
print("before adding new course:", courses)
courses.add("css")
print("after adding new course:", courses)

# 5. Create a dictionary for one student with name, branch, batch, and marks
student = {
    "name": "anand singh",
    "branch": "computer science",
    "batch": "B",
    "marks": 85
}
print("student dictionary:", student)

# 6. print the student dictionary in a readable format
for key, value in student.items():
    print(f"{key}: {value}")
print("_"*45)
