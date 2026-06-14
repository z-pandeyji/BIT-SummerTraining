# QUESTION 1
num=int(input("enter a number"))
if num >0:
    print( num," is positive")
elif num<0:
    print(num,"is negative")   
else:
    print("number is zero")    
# QUESTION 2
num1 = int(input("enter a number"))  
if num1%2==0:
    print("number is even")
else:
    print("number is odd") 
# QUESTION 3       
list=[1,2,3,4,5,6,7,8,9,10] 
for i in list:
    print(i)   
# QUESTION 4 
maths=float(input("enter maths marks"))
physics=float(input("enter physics marks"))
chem=float(input("enter chemistry marks"))
average=round((maths+ physics+chem)/2,2)
print("average  of mark three subject is ",average)
 # QUESTION 5
ds=float(input("enter data structure marks"))
java=float(input("enter java  marks"))
pps=float(input("enter pps marks"))
dstl=float(input("enter descrete mathmatics marks"))
tafl=float(input("enter tafl marks"))
total_marks=ds+java+pps+dstl+tafl
per=(total_marks/500)*100
if per >=90:
    print("Grade A+")
elif per >=80:
    print("Grade A")
elif per >=70:
    print("Grade B")  
elif per >=60:
    print("Grade C")  
elif per >=50:
    print("Grade D") 
else:
    print("Grade F")           


