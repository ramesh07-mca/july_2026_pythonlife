# Functions Quiz:
# Question 1:
# What is the purpose of using functions in Python?
# a) To organize code into logical blocks
# b) To improve code readability and maintainability
# c) To enable code reuse
# d) All of the above

#ans = d) All of the above

# Question 2:
# Which keyword is used to define a function in Python?
# a) def
# b) function
# c) define
# d) fun

#ans= a) def

# Question 3:
# Which of the following is a valid way to call a function named my_function with
# no arguments in Python?
# a) my_function()
# b) call my_function()
# c) function my_function()
# d) my_function

# ans= a) my_function()

# Question 4:
# What is the scope of a variable defined inside a function in Python?
# a) Local scope
# b) Global scope
# c) Enclosing scope
# d) Built-in scope

#ans= a) Local scope

# Task 1: Add Function
# Write a Python function named add that takes two arguments a and b and
# returns their sum.

def add(a,b):
    return a+b
obj=add(4,5)
print(obj)

# Task 2: Square Function
# Write a Python function named square that takes a number x as input and
# returns its square.

def squre(a):
    return a**2
a=int(input("Enter the number:"))
obj=squre(a)
print(obj)

# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as
# input and returns its factorial.
p=1
def facto(a):
    global p
    for i in range(1,a+1):
        p*=i
    return  p
a=int(input("Enter the number:"))
obj=facto(a)
print(obj)

# Task 4: Maximum Function
# Write a Python function named maximum that takes a list of numbers as input and
# returns the maximum value in the list.

def maximum(numbers):
    return max(numbers)
numbers=[1,3,4,5,6,8]
obj=maximum(numbers)
print(obj)

# Task 5: Reverse Function
# Write a Python function named reverse that takes a string s as input and
# returns its reverse.

def reverse(a):
    return a[::-1]
a=input("Enter the value:")
obj=reverse(a)
print(obj)

# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input
# and returns True if n is prime, otherwise False .

def prime(a):
    if a<=1:
        return False 
    else:
        for i in range(2,a):
            if a%i==0:
                return False
        return True           
a=int(input("Enter the number:"))
obj=prime(a)
print(obj)

# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n as
# input and returns the n th Fibonacci number.

def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
    return a
n=int(input("Enter the number:"))
print(fibonacci(n))

# Task 8: Palindrome Function
# Write a Python function named is_palindrome that takes a string s as input and
# returns True if s is a palindrome, otherwise False .

def palindrome(s):
    if s==s[::-1]:
        return True 
    else:
        return False
s=input("Enter the value:")
print(palindrome(s))

# Task 9: Sum of Squares Function
# Write a Python function named sum_of_squares that takes a list of numbers as
# input and returns the sum of the squares of those numbers.

def sum_of_squares(n):
    sum=0
    for i in n:
        sum+=i**2
    return sum

n = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(sum_of_squares(n))

# Task 10: Average Function
# Write a Python function named average that takes a list of numbers as input and
# returns the average value.

def average(n):
    sum=0
    for i in n:
        sum+=i 
    return sum/len(n)
n=[int(x) for x in input("Seperated by space:").split()]
print(average(n))