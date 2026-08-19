# Quiz Advanced Functions
# 1. What is the purpose of the map() function in Python?
# a) To filter elements from an iterable
# b) To apply a function to each element of an iterable
# c) To reduce an iterable to a single value
# d) To sort elements of an iterable

#ans = b) To apply a function to each element of an iterable

# 2. Which of the following functions is NOT a part of the functools module?
# a)map()
# b)filter()
# c)reduce()
# d)partial()

# #ans= a&b

# 3. What does the filter() function do?
# a) Applies a function to each element of an iterable
# b) Reduces an iterable to a single value
# c) Filters elements from an iterable based on a condition(function returns True)
# d) Sorts elements of an iterable

# ans= c) Filters elements from an iterable based on a condition(function returns True)

# 4. In Python, what is the purpose of the reduce() function?
# a) To apply a function to each element of an iterable
# b) To filter elements from an iterable
# c) To concatenate strings or join lists
# d) To apply a function to pairs of elements in an iterable until it's reduced to a single value

#ans= d)

# Coding exercises:
# Write a Python function square_all(numbers) that takes a list of numbers as input
# and returns a new list containing the square of each number in the input list.
# Use the map() function with a lambda function to implement this.

list_1=[int(x) for x in input("Enter the list:").split()]
result=map(lambda a:a**2,list_1)
print(list(result))

# Write a Python function filter_positive(numbers) that takes a list of numbers as
# input and returns a new list containing only the positive numbers from the
# input list. Use the filter() function with a lambda function to implement this.

list_1=[int(x) for x in input("Enter the list:").split()]
result= filter(lambda a:a>=0,list_1)
print(list(result))

# Write a Python function calculate_factorial(n) that calculates the factorial of a
# given number n . Use the reduce() function with an appropriate lambda
# function to implement this.

from functools import reduce
z=int(input("Enter the number:"))
result=reduce(lambda a,b:a*b,range(1,z+1))
print(result)

# Write a Python function count_vowels(string) that takes a string as input and
# returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce()
# function with an appropriate lambda function to implement this.


string=input("Enter the string:")
from functools import reduce
result=reduce(lambda count,char: count + 1 if char.lower() in "aeiou" else count,string,0)
print(result)