#Create a list of 5 student names. Add one new student name to the list and print the final list.
# Expected Output:
# ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh', 'Vivek']
import numpy as num
students =['Aman','Priya','Shalu','Raj','Ansh']
students.append('Vivek')
print(students)


#2.Tuple Indexing
cities =('Mumbai','Kolkata','Delhi','Lucknow','Chennai')
print(cities[2])

#3.Set add
courses ={'Python','SQL','Machine','Learning','Data Analytics'}
courses.add('AI')
print(sorted(courses))

#4.Dictionary Access
student = {
    'name':'Rahul',
   ' courses':'Python Data ai',
   'batch':'Batch',
   'city':'Noida'
}
print('Name:',student['name'])
print('Course:',student[' courses'])



#Question 5: Filter Even Numbers

numbers =list(range(1,11))
even_numbers=[]
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
        
print(even_numbers)


#Question 6: Count Word Frequency

words =['Python','ai','python','data','AI','python']
frequency ={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
        
print(frequency)


#Question 7: Nested Student Dictionary
students = {
    'name':'Neha',
    'marks':{
        'python':85,
        'data':90
    },
    'Skills':['Python','SQL']
}

student["Skills"].append('pandas')
print(students)



#Question 8: Common Elements
python_students ={"Aman","Priya","Raj","Neha"}
ai_students={"Raj","Neha","Vivek","Shalu"}

common_student=python_students.intersection(ai_students)
print(common_student)









