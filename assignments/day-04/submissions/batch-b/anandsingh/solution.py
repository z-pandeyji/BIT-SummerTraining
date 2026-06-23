# question 1. list append
my_list = ["aman","priya","salu","raj","ansh"]
my_list.append("vivek")
print(my_list)

# question 2. tuple indexing
my_tuple = ("gorakhpur","lucknow","delhi","kanpur","varanasi")
print(my_tuple[2])

# Question 3. set add
my_set={"Data Analytics","Machine Learning","Python","SQL"}
my_set.add("AI")
print(my_set)

# question 4. dictionary access 
my_dict ={
    "name":"Anand Singh",
    "course":"Data Science",
    "Batch":"B",
    "City":"Gorakhpur"
}
print("Name:",my_dict["name"])
print("course:",my_dict["course"])

# question 5. filter even numbers
numbers =[1,2,3,4,5,6,7,8,9,10]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# question 6. count words frequency
text ="hello world hello data sciece"
word_freq = {}
for word in text.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)