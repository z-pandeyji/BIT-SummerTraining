# Question 1: List Append

students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
students.append("Vivek")
print(students)



# Question 2: Tuple Indexing

cities = ("Mumbai", "Kolkata", "Delhi", "Chennai", "Pune")
print(cities[2])



# Question 3: Set Add

courses = {"Python", "Data Analytics", "Machine Learning", "SQL"}
courses.add("AI")
print(sorted(courses))



# Question 4: Dictionary Access

student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "A",
    "city": "Lucknow"
}

print(f"Name: {student['name']}")
print(f"Course: {student['course']}")



# Question 5: Filter Even Numbers

numbers = list(range(1, 11))
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)



# Question 6: Word Frequency

words = ["python", "ai", "python", "data", "ai", "python"]

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)



# Question 7: Nested Dictionary

student2 = {
    "name": "Neha",
    "marks": {
        "python": 85,
        "data": 90
    },
    "skills": ["Python", "SQL"]
}

student2["skills"].append("Pandas")
print(student2)



# Question 8: Common Elements

python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}

common = sorted(python_students & ai_students)
print(common)