
# 1. Create a list of 5 student names and print all names.
Students_names=["muskan","janu","surbhi","dimpy","omee"]
for name in Students_names:
    print(name)
# 2. Add one new student name to the list.
Students_names=["muskan","janu","surbhi","dimpy","omee"]
Students_names.append("raj")
print("updated list : ",Students_names)
# 3. Create a tuple of 5 city names and print the second city.
cities=("gorakhpur","varanasi","agra","kanpur","delhi")
print("second city",cities[1])
# 4. Create a set of 5 course names and add one new course.
courses={"btech","mtech","mba","bba","bca"}
courses.add("mca")
print(courses)
# 5. Create a dictionary for one student with name, branch, batch, and marks.
student={
    "name":"Muskan Verma",
    "branch":"Ealectronics and Communication Engineering",
    "batch":"A",
    "marks":"775"

}
print("student dictionary : ",student)
# 6. Print the student dictionary in a readable format.
student={
    "name":"Muskan Verma",
    "branch":"Ealectronics and Communication Engineering",
    "batch":"A",
    "marks":"775"

}
print("student details ")
print("name : ",student["name"])
print("branch : ",student["branch"])
print("batch : ",student["batch"])
print("marks : ",student["marks"])