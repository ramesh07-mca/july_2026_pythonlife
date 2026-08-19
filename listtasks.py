# Task 1:
# Reverse List:
# Write Python code to reverse the order of elements in the given list my_list .
# Print the reversed list.

my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()
print(my_list)

# Task 2:
# Common Elements:
# Given two lists list1 and list2 , find and print the common elements between
# them.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result=[i for i in list1 for j in list2 if i==j]
print(result)

# Task 3:
# Unique Elements:
# Create a new list unique_list containing only the unique elements from the
# given list original_list . Print the unique list.

original_list = [1, 2, 2, 3, 4, 4, 5]
empty=[]
for i in original_list:
    if i not in empty:
        empty.append(i)
print(empty)



# Task 4:
# Remove Duplicates:
# Remove duplicate elements from the given list duplicated_list and print the list
# without duplicates while preserving the order.

duplicated_list = [1, 2, 2, 3, 4, 4, 5]
set_res=set(duplicated_list)
print(list(set_res))

# Exercise 1: List Concatenation
# Write a Python script that concatenates two lists and prints the result.

a=[1,23,5456,5]
b=[2,4,67,67,8,9]
print(a+b)

# Exercise 2: List Repetition
# Write a Python script that repeats a list three times and prints the result.

a=[1,2,3,4,5]
print(a*3)

# Exercise 3: List Removal
# Write a Python script that removes the elements at even indices from a list.

numbers=[1,2,3,4,5,6,7,8,9]
print(numbers[1::2])

    
# Exercise 4: List Insertion
# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of
# a list

a=[1,2,3,5,6,7]
a.insert(0,10)
a.insert(1,11)
a.insert(2,12)
print(a)        

# List comprehensions
# 1. Square Numbers: Create a list of squares of numbers from 1 to 10.

result=[i**2 for i in range(1,11)]
print(result)

# 2. Even Numbers: Generate a list of even numbers from 1 to 20.

result=[i for i in range(21) if i%2==0]
print(result)

# 3. Words Lengths: Given a list of words, create a list containing the lengths of
# each word.

words = ["apple", "banana", "cherry", "date"]
result=[len(i) for i in words ]
print(result)