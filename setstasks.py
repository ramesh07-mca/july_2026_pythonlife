# Sets Quiz
# Question 1:
# What is the output of the following code?
# my_set = {1, 2, 3, 4, 5}
# print(len(my_set))
# a) 1
# b) 5
# c) 4
# d) 0

#ans = b) 5

# Question 2:
# Which of the following methods is used to add an element to a set?
# a) add()
# b) insert()
# c) append()
# d) update()

#ans = a) add()

# Question 3:
# Consider the following sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Which method would you use to find the elements that are common in both
# sets?
# a) intersection()
# b) union()
# c) difference()
# d) symmetric_difference()

#ans= a) intersection()

# Question 4:
# Which of the following statements about sets in Python is true?
# a) Sets are ordered collections of elements.
# b) Sets allow duplicate elements.
# c) Sets are mutable.
# d) Sets support indexing.

#ans = c) sets are mutable.

# Task 1: Set Intersection
# Write Python code to find and print the intersection of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result= set1.intersection(set2)
print(result)
 # or
res= set1&set2
print(res)
# Your code here
# Output should be: {4, 5}

# Task 2: Set Union
# Write Python code to find and print the union of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
   #or
print(set1|set2)
# Your code here
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}

# Task 3: Set Difference
# Write Python code to find and print the elements present in set1 but not in
# set2 :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))
  #or 
print(set1-set2)
# Your code here
# Output should be: {1, 2, 3}

# Task 4: Set Symmetric Difference
# Write Python code to find and print the symmetric difference of the following
# two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.symmetric_difference(set2))
   #or 
print(set1^set2)
# Your code here
# Output should be: {1, 2, 3, 6, 7, 8}

# Task 5: Set Membership Test
# Write Python code to check if the element 3 is present in the set my_set :
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)
# Your code here
# Output should be: True

# Exercise 1: Set Intersection
# Write a Python script that finds and prints the intersection of two sets.

a={1,2,3,4,"Madhu",0.5}
b={4,57,8,"Madhu",0.5}
print(a.intersection(b))
#or
print(a&b)

# Exercise 2: Set Union
# Write a Python script that finds and prints the union of two sets.


a={1,2,3,4,"Madhu",0.5}
b={4,57,8,"Madhu",0.5}
print(a.union(b))
#or
print(a|b)

# Exercise 3: Set Difference
# Write a Python script that finds and prints the difference between two sets.

a={1,2,3,4,"Madhu",0.5}
b={4,57,8,"Madhu",0.5}
print(a.difference(b))
#or
print(a-b)

# Exercise 4: Set Symmetric Difference
# Write a Python script that finds and prints the symmetric difference between
# two sets.

a={1,2,3,4,"Madhu",0.5}
b={4,57,8,"Madhu",0.5}
print(a.symmetric_difference(b))
#or
print(a^b)