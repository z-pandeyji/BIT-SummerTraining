### Question 1: List Append

list1=["Aman","Priya","Shalu","Raj","Ansh"]     #list of students
list2=list1.append("Vivek")                     #adding another student to the list
print(list2)                                    #printing the list of students      

### Question 2: Tuple Indexing

cities=("Bangalore","Mumbai","Delhi","Chennai","Kolkata")   #tuple of cities
print(cities[2])                                            #printing the city at index 2, third city name

### Question 3: Set Add

cources={"Data Analytics", "Machine Learning", "Python", "SQL"}          #set of corces 
cources.add("Ai")                                                        # adding new cource to the set
cources_list=list(cources)                                               # typecasting cources to list
print(sorted(cources_list))                                               #printing the sorted list of cources

### Question 4: Dictionary Access

student_dict={                      #Create a dictionary with keys `name`, `course`, `batch`, and `city`
    "name":"Raj Singh",
    "cource":"Python Data Ai",
    "batch":"batch a",
    "city":"Gorakhpur",
}
print(student_dict["name"])         #printing name  
print(student_dict["cource"])       #printing cources



### Question 5: Filter Even Numbers

list1=[1,2,3,4,5,6,7,8,9,10]            #list of numbers 1 to 10
list2=[]                                
for i in list1:
    if i%2==0:                          #checking the number is even 
        list2.append(i)                 #adding the number to list to if even
    else:
        continue
print(list2)                            #printing the even number list


### Question 6: Count Word Frequency

words = ["python", "ai", "python", "data", "ai", "python"]
freq={}
for i in words:                 #itrating the words
    freq[i] = freq.get(i,0)+1   #checking the existence of word in dictionary
print(freq)                     #printing the frequency of word

### Question 7: Nested Student Dictionary

student={                   #creating a nested dictionary
    "name":"Raj singh",
    "marks":{
        "python":85,
        "Data":90,
    },
    "skill":["Python","SQL"]
}

student["skill"].append("Pandas") #adding a new skill to student
print(student)                       #printing updated dictionary

### Question 8: Common Elements

python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_student=[]                                            #creating empty list
for student in python_students:
    for student in ai_students:
        common_student.append(student)                       #appending common student to list1
print(sorted(common_student))                                #printing common sorted student
