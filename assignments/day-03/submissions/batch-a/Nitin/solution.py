
# 1. Create a list of 5 student names and print all names
students = ["Nitin", "Rahul", "Priya", "Aman", "Sneha"]

print("Student Names:")
for student in students:
    print(student)

# 2. Add one new student name to the list
students.append("Rohit")

print("\nUpdated Student List:")
for student in students:
    print(student)

# 3. Create a tuple of 5 city names and print the second city
cities = ("Gorakhpur", "Lucknow", "Delhi", "Kanpur", "Varanasi")

print("\nSecond City:", cities[1])

# 4. Create a set of 5 course names and add one new course
courses = {"Python", "Java", "C++", "HTML", "CSS"}

courses.add("JavaScript")

print("\nCourses:")
for course in courses:
    print(course)

# 5. Create a dictionary for one student
student = {
    "name": "Nitin Jaiswal",
    "branch": "Computer Science and Engineering",
    "batch": "Batch A",
    "marks": 87.5
}

# 6. Print the dictionary in a readable format
print("\nStudent Details:")
for key, value in student.items():
    print(f"{key}: {value}")