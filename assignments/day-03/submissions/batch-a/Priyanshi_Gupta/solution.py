#1

Student = ["Priyanshi","Priya", "Nandini", "Neha", "Rohini"]
print("Student Name")
for name  in Student:
    print(name)

#2
Student.append("Kira")
print(Student)

#3
cities = ("Lucknow", "Delhi", "Jaypur","Mumbai","Kanpu")
print("\n second city")
print(cities[1])

#4
coures = {"C", "C+", "Java", "CSS", "Python"}
coures.add("HTML")
print(coures)


#5
Student_info = {
    "name" : "Priyanshi",
    "branch" : "AIML",
    "batch" : "2026",
    "marks" : 80
    }
print(Student_info)


#6
print("\n Student Details:")
print("Name:", Student_info["name"])
print("Branch:", Student_info["branch"])
print("Bacth:", Student_info["batch"])
print("Marks:", Student_info["marks"])