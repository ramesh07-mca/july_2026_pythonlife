# Quiz Questions:
# 1. Question 1:
# What does the
# all() function return when applied to an empty tuple?
# A) True
# B) False
# C) Error

#ans= A) True

# Question 2:
# Which of the following statements correctly creates a tuple?
# A) my_tuple = [1, 2, 3]
# B) my_tuple = (1, 2, 3)
# C) my_tuple = {1, 2, 3}

#ans= B) my_tuple = (1, 2, 3)

#  Question 3:
# What is the output of the following code snippet?
# my_tuple = (1, 2, 3)
# print(len(my_tuple))
# A) 1
# B) 2
# C) 3

#ans = C) 3

#  Question 4:
# Which of the following statements about tuples in Python is true?
# A) Tuples are mutable.
# B) Tuples can only store elements of the same data type.
# C) Tuples use parenthesis ( ) for declaration.

#ans = C) Tuples use parenthesis ( ) for declaration.

# Coding Exercise:
# 1. Create a Tuple: Write a program that creates a tuple containing three
# elements: your name, your age, and your favorite color. Then print the tuple.

a=("Raghu",24,"green")
print(a)

# 2. Access Tuple Elements: Write a program that creates a tuple containing the
# days of the week. Then, print the third element of the tuple.

a=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(a[2])

# 3. Tuple Concatenation: Write a program that creates two tuples, one
# containing odd numbers from 1 to 5 and another containing even numbers
# from 2 to 6. Concatenate these two tuples and print the result.
a=(1,3,5)
b=(2,4,6)
result=a+b
print(result)

# 4. Tuple Unpacking: Write a program that defines a tuple containing the
# dimensions of a rectangle (length and width). Then, unpack this tuple into
# two variables and calculate the area of the rectangle.

a=[(2,3),(4,5)]
for i,j in a:
    print(f"length of rectangle: ",i*j)

#Output length of rectangle:  6
#       length of rectangle:  20 

# 5. Check if an Element Exists: Write a program that checks if a given element
# exists in a tuple.

a=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday") 
print("Monday" in a)

#True 

# 6. Write a Python program to generate a bill for a supermarket purchase. The
# program should store the items and their prices in a list of tuples. It should
# then iterate over this list to print out each item along with its price. Finally,
# calculate and print the total cost of all the items
# Sample Input:
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print(f"Item\tPrice")
print("_"*30)
sum=0
for i,j in items:
    print(f"{i}   {float(j)}")
    sum+=j
print("_"*30)
print(f"Total {float(sum)}")



# Sample Output:
# Item Price
# --------------------
# Apple 99.00
# Banana 99.00
# Milk 49.00
# --------------------
# Total 247.00