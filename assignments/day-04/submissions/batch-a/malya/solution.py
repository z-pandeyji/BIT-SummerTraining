# Day 4 Assignment

#1: List Append
list=["malya","deependra","kirti","kuldeep","vanshika"]
updated_list=list.append("aryan")
print(list)
print()
# Expected Output-->["malya","deependra","kirti","kuldeep","vanshika","aryan"]


# 2: Tuple Indexing
tuple=("delhi","mumbai","agra","kanpur","banaras")
print("third city-->",tuple[2])
print()
# Expected Output:agra


#3: Set Add
course={"Data Analytics", "Machine Learning", "Python", "SQL"}
course.add("AI")
print(sorted(course))
print()
#excepted o/p->['AI', 'Data Analytics', 'Machine Learning', 'Python', 'SQL']


# 4: Dictionary Access
dict={
    "name":"Malya Srivastava",
    "course":"AIML",
    "batch":"2026",
    "city":"Gorakhpur"
}
print(f"Name-->{dict['name']}")
print(f"Course-->{dict['course']}")
print()
#excepted o/p->Name: Rahul
# Course: Python Data AI



## Medium Questions

#5: Filter Even Numbers
list=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for i in list:
    if i %2==0:
        new_list.append(i)
print(new_list)
print()
#excepted o/p->[2, 4, 6, 8, 10]


# 6: Count Word Frequency
words = ["python", "ai", "python", "data", "ai", "python"]
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
print()
# Expected Output: {'python': 3, 'ai': 2, 'data': 1}


# 7: Nested Student Dictionary
student = {
    "name": "Neha",
    "marks": {
        "python": 85,
        "data": 90
    },
    "skills": ["Python", "SQL"]
}
student["skills"].append("Pandas")
print(student)
print()
#  Expected Output:{'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': \['Python', 'SQL', 'Pandas']`


#8: Common Elements
# Create two sets:
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_students = python_students.intersection(ai_students)
print(sorted(common_students))
# Expected Output:['Neha', 'Raj']

