## Day 4 Assignment
## Topic: Python Data Structures
## Question: 1 List Append
## Print("Create a list of 5 student names.Add one new student name to the list and print the final list.")
students = ["Ritu","Atul","Anmol","Ankita","Anu"] # create a list of 5 student names
students.append("Riya") # add one new student name
print("Final student list:",students) #print the final list

## Question: 2  Tuple Indexing
## Print("Create a tuple of 5 city name and print the third city.")
cities = ("Gorkhpur","Deoria","Salempur","Lar","Mau") # create a tuple of city names

print("Third city:", cities[2]) # print the third city

## Question: 3 Set Add
##Print("Create a set of 4 course names.Add "AI" to the set and print the sorted list of courses.")
courses = {"HTML","C","C++","Java"} # create a set of 4 course names
courses.add("AI") #Add "AI" to the set

print("Sorted courses:", sorted(courses)) # print the sorted list of courses

## Question: 4 Dictionary Access
## Print("Create a dictionary with keys name ,course, batch,and city.Print the student's name and course.")
student = { # create a dictionary
    "name": "Ritu",
    "course": "MCA",
    "batch": "2025",
    "city": "Gorkhpur"
}

print("Name:",student["name"]) # print the student's name 
print("Course:",student["course"]) # print the student's course

## Question: 5 Filter Even Numbers
##Print("Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.")
numbers = [1,2,3,4,5,6,7,8,9,10] # create a list of numbers from 1 to 10
even_numbers = [num for num in numbers if num % 2 == 0] # create a new list with only even numbers

print("Even numbers:",even_numbers) #Print the even numbers list

## Question: 6 Cout Word Frequency
## print("Create a list of words: Use a dictionary to count how many times each word appears and print the dictionary.")
words =["Mca","Bca","Mca","Data","Bca","Mca"] # create the list of words

word_count = {} # count word occurrences using a dictionary

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count) # print the dictionary

##Question: 7 Nested Student Dictionary
## print("Create a nested dictionary for one student with name, marks,and skills.Add one new skill "Pandas and print the updated dictionary.")
student = { # create a nested student dictionary
    "name": "Ritu",
    "marks":88,
    "skill":["java"]
    
}

student["skill"].append("Pandas") # add a new skill

print(student) # print the updated dictionary

## Question: 8 Common Elements
## print("Create two sets: Find the common students and print them as a sorted list.")
new_students = {"Ritu","Atul","Anmol","Ankita"} # create the one set
is_students = {"Rajan","Riya","Rohan","Shalu"}

new_students.intersection(is_students)
new=list(new_students)
print(new) # print as a sorted list
