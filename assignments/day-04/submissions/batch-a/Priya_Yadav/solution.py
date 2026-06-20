#  1. Creating a list of student name
student_name=["Aman","Priya","Shalu","Raj","Ansh"]
# Adding a new student name
student_name.append("Vivek")

print(student_name)
# 2. Creating a tuple of 5 cities 
cities=("Gorakhpur","Mumbai","Delhi","Jaipur","Banglore")

print(cities[2])
# 3. Creating a set of 4 courses
courses={"Data Analytics","Machine Learning","Python","SQL"}
# Adding a new course AI 
courses.add("AI")


print(sorted(courses))
# 4. Creating a dictionary with keys `name`, `course`, `batch`, and `city`.
student_detail={"Name":"Rahul","Course":"Python data AI",
                "Batch":"A","City":"GKP"}

for key,val in student_detail.items():
    if key=="Name" or key=="Course":
        print(key,":",val)
# 5. Creatint a list of 1 to 10 numbers
num_list=[1,2,3,4,5,6,7,8,9,10]
even_num_list=[]
for i in num_list:
    if i%2==0:
        even_num_list.append(i)
      
print(even_num_list)
# 6. Creating a list of words
words = ["python", "ai", "python", "data", "ai", "python"]
# Creating a dictionary to count frequency
dict1={}
for item in words:
    if item in dict1:
        dict1[item]=dict1[item]+1
    else:
        dict1[item]=1
     
print(dict1)  
# 7. Creating a nested dictionary for one student with name, marks, and skills. 
student_record={"Name":"Neha",
                "Marks":{"Python":85,"Data":90},
                "Skills":["Python","SQL"]} 
# Adding a new skill pandas
student_record["Skills"].append("Pandas")
print(student_record)
# 8. Creating to sets 
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
# To find common students
c_st=[]
for items in python_students:
    if items in ai_students:
        c_st.append(items)
       
print(sorted(c_st))









       



