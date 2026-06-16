# 1. Create a list of 5 student names and print all names.
lst =["Aman","Prince","Nikhil ","Ashu","Anish"]
print("Students name : ",lst)

# 2. Add one new student name to the list.
lst.append("Aryan")
print("Students name : ",lst)


# 3. Create a tuple of 5 city names and print the second city.
cities =("Gorakhpur","Maharajganj","Delhi","Mau","Gurgaon")

print(cities[1])

# 4. Create a set of 5 course names and add one new course.

myset={"BCA","BA","Btech","BSc","Polytecnic"}

myset.add("Bpharma")
print(myset)

# 5. Create a dictionary for one student with name, branch, batch, and marks.

students= {
    "name":"Prince yadav",
    "branch":"Bca",
    "batch":"b",
    "marks":88
}
for key ,value in students.items():
    print(key,":",value)
